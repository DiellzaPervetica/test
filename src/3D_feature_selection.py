import pandas as pd
from pathlib import Path
from statsmodels.stats.outliers_influence import variance_inflation_factor

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT = BASE_DIR / "data" / "3C_scaled_dataset.csv"
OUTPUT = BASE_DIR / "data" / "3D_selected_dataset.csv"

TARGET = "pm25"
MIN_CORRELATION = 0.05
VIF_THRESHOLD = 5.0
KEEP_COLS = ["datetime", "date"]


def calculate_vif(df_numeric):
    vif_data = pd.DataFrame()
    vif_data["Feature"] = df_numeric.columns
    vif_data["VIF"] = [
        variance_inflation_factor(df_numeric.values, i)
        for i in range(df_numeric.shape[1])
    ]
    return vif_data.sort_values("VIF", ascending=False)


df = pd.read_csv(INPUT)

df_datetime = df[KEEP_COLS].copy()
df_numeric = df.drop(columns=KEEP_COLS)

correlations = df_numeric.corr()[TARGET].drop(TARGET).abs()
selected_by_corr = correlations[correlations >= MIN_CORRELATION].index.tolist()

df_for_vif = df_numeric[selected_by_corr].copy()

try:
    vif_results = calculate_vif(df_for_vif)
    features_with_acceptable_vif = vif_results[vif_results["VIF"] <= VIF_THRESHOLD][
        "Feature"
    ].tolist()
except Exception:
    features_with_acceptable_vif = selected_by_corr

final_features = features_with_acceptable_vif + [TARGET]
df_selected = df_numeric[final_features].copy()
df_final = pd.concat([df_datetime, df_selected], axis=1)

df_final.to_csv(OUTPUT, index=False)

print("FEATURE SELECTION REPORT - PM2.5 PREDICTION\n")
print(f"Dataset fillestar: {df.shape}")
print(f"Dataset përfundimtar: {df_final.shape}\n")
print("FEATURES TË ZGJEDHURA:")
for feat in final_features[:-1]:
    corr_val = correlations[feat]
    print(f"  [SELECTED] {feat:30s} | Korrelacion: {corr_val:7.4f}")
print(f"\nTarget variable: {TARGET}")