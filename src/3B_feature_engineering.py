import pandas as pd
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT = BASE_DIR / "data" / "2D_validated_final_dataset.csv"
OUTPUT = BASE_DIR / "data" / "3B_engineered_dataset.csv"

TARGET = "pm25"
ENERGY_COLS = ["A3_MW", "A4_MW", "A5_MW", "B1_MW", "B2_MW", "total_generation_mw"]
WEATHER_COLS = [
    "temperature_2m (°C)",
    "rain (mm)",
    "snowfall (cm)",
    "relative_humidity_2m (%)",
    "wind_direction_10m (°)",
    "wind_speed_10m (km/h)",
]
POLLUTANT_COLS = ["co", "no2", "o3", "pm10", "so2"]


def create_lag_features(df: pd.DataFrame, target_col: str, lags: list) -> pd.DataFrame:
    for lag in lags:
        df[f"{target_col}_lag_{lag}h"] = df[target_col].shift(lag)
    return df


def create_rolling_features(df: pd.DataFrame, target_col: str, windows: list) -> pd.DataFrame:
    for window in windows:
        df[f"{target_col}_rolling_{window}h"] = (
            df[target_col].rolling(window=window, min_periods=1).mean()
        )
    return df


def create_temporal_features(df: pd.DataFrame) -> pd.DataFrame:
    df["datetime"] = pd.to_datetime(df["datetime"], errors="coerce")
    df["day_of_week"] = df["datetime"].dt.dayofweek
    df["month"] = df["datetime"].dt.month
    df["hour"] = df["datetime"].dt.hour
    df["hour_sin"] = np.sin(2 * np.pi * df["hour"] / 24)
    df["hour_cos"] = np.cos(2 * np.pi * df["hour"] / 24)

    return df


def create_interaction_features(df: pd.DataFrame) -> pd.DataFrame:
    df["temp_wind_interact"] = df["temperature_2m (°C)"] * df["wind_speed_10m (km/h)"]

    df["generation_humidity_interact"] = (
        df["total_generation_mw"] * df["relative_humidity_2m (%)"]
    )

    return df


def drop_features_with_nans(df: pd.DataFrame) -> pd.DataFrame:
    initial_rows = len(df)
    df = df.dropna()
    final_rows = len(df)
    dropped = initial_rows - final_rows

    print(f"Rreshtat me NaN u hoqën: {dropped} ({100*dropped/initial_rows:.1f}%)")
    print(f"Rreshtat që mbeten: {final_rows}")

    return df


df = pd.read_csv(INPUT)
print(f"Dataset fillestar: {df.shape} (rreshta, kolona)")

df = create_temporal_features(df)
df = create_lag_features(df, TARGET, lags=[1, 24])
df = create_rolling_features(df, TARGET, windows=[24])
df = create_interaction_features(df)

df = drop_features_with_nans(df)

final_cols = [col for col in df.columns if col in (
    ["datetime", "date", "hour", "day_of_week", "month", "hour_sin", "hour_cos"] +
    [c for c in df.columns if "lag_" in c] +
    [c for c in df.columns if "rolling_" in c] +
    [c for c in df.columns if "interact" in c] +
    ENERGY_COLS + WEATHER_COLS + POLLUTANT_COLS + [TARGET]
)]
df = df[final_cols]

df.to_csv(OUTPUT, index=False)
print(f"Engineered dataset i ruajtur: {OUTPUT.name}, Shape: {df.shape}")