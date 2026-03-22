# Prishtina Air Pollution, Weather and Energy Production Pipeline (2023–2026)

<table>
  <tr>
    <td width="150" align="center" valign="center">
      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/University_of_Prishtina_logo.svg/1200px-University_of_Prishtina_logo.svg.png" width="120" alt="University Logo" />
    </td>
    <td valign="top">
      <p><strong>Universiteti i Prishtinës</strong></p>
      <p>Fakulteti i Inxhinierisë Elektrike dhe Kompjuterike</p>
      <p>Inxhinieri Kompjuterike dhe Softuerike – Programi Master</p>
      <p><strong>Projekti nga lënda:</strong> Përgatitja dhe vizualizimi i të dhënave</p>
      <p><strong>Profesor:</strong> Dr. Sc. Lule Ahmedi</p>
      <p><strong>Profesor:</strong> Dr. Sc. Mërgim H. Hoti</p>
      <p><strong>Studentët:</strong></p>
      <ul>
        <li>Diellza Përvetica</li>
        <li>Fatjeta Gashi</li>
        <li>Festina Klinaku</li>
      </ul>
    </td>
  </tr>
</table>

---

## Permbajtja

1. [Permbledhje e projektit](#permbledhje-e-projektit)
2. [Qellimi i punimit](#qellimi-i-punimit)
3. [Burimet e te dhenave](#burimet-e-te-dhenave)
4. [Pershkrimi i dataset-eve hyrse](#pershkrimi-i-dataset-eve-hyrse)
5. [Struktura e repository-t](#struktura-e-repository-t)
6. [Topologjia e pipeline-it](#topologjia-e-pipeline-it)
7. [Pershkrimi i detajuar i cdo skripte](#pershkrimi-i-detajuar-i-cdo-skripte)
   - [Data collection](#data-collection)
   - [Integration](#integration)
   - [Distinct values](#distinct-values)
   - [Data cleaning](#data-cleaning)
   - [Feature engineering](#feature-engineering)
   - [Preprocessing](#preprocessing)
8. [Artefaktet dhe output-et e krijuara](#artefaktet-dhe-output-et-e-krijuara)
9. [Vizualizimet e gjeneruara](#vizualizimet-e-gjeneruara)
10. [Teknikat e zbatuara dhe lidhja me lenden](#teknikat-e-zbatuara-dhe-lidhja-me-lenden)
11. [Ekzekutimi i projektit](#ekzekutimi-i-projektit)
12. [Rezultati final i pipeline-it](#rezultati-final-i-pipeline-it)
13. [Permiresime te mundshme ne vazhdim](#permirsime-te-mundshme-ne-vazhdim)

---

## Permbledhje e projektit

Ky projekt implementon një pipeline të plotë, modular dhe të riprodhueshëm për ndërtimin e një dataset-i analitik dhe model-ready për analizën dhe parashikimin e ndotjes së ajrit në Prishtinë, me fokus të veçantë te `PM2.5`.

Pipeline-i ndërtohet mbi integrimin e tre burimeve të ndryshme të të dhënave, të mbledhura për periudhën 2023–2026:

1. të dhënat për prodhimin e energjisë elektrike nga termocentralet e Kosovës,
2. të dhënat meteorologjike për Prishtinën,
3. të dhënat për ndotjen e ajrit në Prishtinë.

Më pas, këto burime:
- harmonizohen në nivel kohor orë-pas-ore,
- pastrohen,
- validohen,
- plotësohen për vlerat mungesë,
- pasurohen me karakteristika të reja,
- trajtohen për outlier-a dhe skewness,
- standardizohen,
- dhe në fund reduktohen në një subset tiparesh më të qëndrueshëm për modelim.

Ky projekt demonstron të gjithë ciklin e përgatitjes së të dhënave: nga kolektimi, integrimi dhe kontrolli i cilësisë, deri te feature engineering, transformimi statistikor dhe feature selection.

---

## Qellimi i punimit

Qëllimi kryesor i këtij projekti është të ndërtojë një dataset të pastër dhe analitikisht të qëndrueshëm për të studiuar marrëdhëniet ndërmjet:

- prodhimit të energjisë elektrike,
- kushteve meteorologjike,
- dhe ndotësve atmosferikë në Prishtinë,

me fokus të veçantë në përdorimin e këtyre të dhënave për parashikimin e `PM2.5`.

Objektivat kryesore janë:

- të integrohen burime heterogjene të të dhënave në një bosht të përbashkët kohor;
- të kontrollohet cilësia e të dhënave dhe të korrigjohen vlera të pasakta;
- të trajtohen mungesat pa humbur informacion të vlefshëm;
- të krijohen tipare të reja kohore, meteorologjike dhe ndërvepruese;
- të zbutet ndikimi i outlier-ave dhe shpërndarjeve shumë të shtrembëruara;
- të standardizohet dataset-i për përdorim në modele statistikore dhe machine learning;
- të eliminohet multikolineariteti i tepërt përmes VIF-based feature selection.

---

## Burimet e te dhenave

Ky projekt bazohet në tre burime kryesore të të dhënave:

### 1. Prodhimi i energjise elektrike nga termocentralet e Kosoves
Dataset-i përmban prodhimin orar të njësive energjetike:
- `A3_MW`
- `A4_MW`
- `A5_MW`
- `B1_MW`
- `B2_MW`

Nga këto është ndërtuar edhe:
- `total_generation_mw`

Të dhënat janë marrë nga KOSTT dhe janë harmonizuar në nivel orar.

### 2. Te dhenat meteorologjike per Prishtinen
Dataset-i meteorologjik përmban atribute si:
- temperatura,
- reshjet,
- bora,
- lagështia relative,
- drejtimi i erës,
- shpejtësia e erës.

Këto të dhëna janë përdorur për të modeluar kushtet atmosferike që ndikojnë në përhapjen ose stagnimin e ndotjes.

### 3. Te dhenat e ndotjes se ajrit ne Prishtine
Dataset-i i cilësisë së ajrit përmban matje të ndotësve:
- `co`
- `no2`
- `o3`
- `pm10`
- `pm25`
- `so2`

Këto të dhëna janë mbledhur dhe konsoliduar për Prishtinën përmes burimeve të tipit OpenAQ / arkivave përkatëse / notebook-ut të kolektimit të përdorur në projekt.

### Shtrirja kohore
Burimet hyrëse mbulojnë periudhën 2023–2026. Megjithatë, dataset-i i integruar final ruan vetëm intervalin ku të tre burimet kanë mbulim të përbashkët orar, prandaj output-i i parë i integruar ruhet si:

- `1A_merged_data_hourly_2023_2025.csv`

Kjo e bën integrimin kohor të saktë dhe shmang boshllëqet e krijuara nga mungesa e përbashkët midis burimeve.

---

## Pershkrimi i dataset-eve hyrse

Pipeline-i përdor tre skedarë bruto të ruajtur në `data/raw/`:

- `prishtina_air_quality_2023_2025.csv`
- `prishtina_weather_2023_2026.csv`
- `prishtina_energy_production_2023_2026.csv`

### Dataset-i i ndotjes se ajrit
Përmban kolonën `datetime` dhe ndotësit kryesorë atmosferikë:
- `co`
- `no2`
- `o3`
- `pm10`
- `pm25`
- `so2`

### Dataset-i meteorologjik
Përmban kolonën kohore dhe atributet:
- `temperature_2m (°C)`
- `rain (mm)`
- `snowfall (cm)`
- `relative_humidity_2m (%)`
- `wind_direction_10m (°)`
- `wind_speed_10m (km/h)`

### Dataset-i i energjise
Përmban:
- kolonën e datës,
- kolonën e orës,
- prodhimin për secilën njësi termocentrali,
- dhe totalin e gjenerimit të energjisë.

Gjatë leximit, ky dataset kërkon pastrim shtesë të header-it, sepse struktura e tij fillestare nuk është menjëherë tabulare në formën standarde CSV.

---

## Struktura e repository-t

```text
TEST/
│
├── src/
│   ├── data_cleaning/
│   │   ├── 2A_datetime_and_duplicates.py
│   │   ├── 2B_data_quality_cleaning.py
│   │   ├── 2C_missing_values_handling.py
│   │   └── 2D_validate_final_dataset.py
│   │
│   ├── data_collection/
│   │   ├── get_kosova_air_quality_data.ps1
│   │   └── get_prishtina_air_quality_data.ipynb
│   │
│   ├── distinct_values/
│   │   └── 1B_distinct_values.py
│   │
│   ├── feature_engineering/
│   │   ├── 3A_target_analysis.py
│   │   └── 3B_feature_engineering.py
│   │
│   ├── integration/
│   │   └── 1A_merge_data.py
│   │
│   └── preprocessing/
│       ├── 4A_outlier_treatment.py
│       ├── 4B_skewness_treatment.py
│       ├── 4C_visualization_before_after.py
│       ├── 4D_feature_scaling.py
│       └── 4E_feature_selection.py
│
├── data/
│   ├── raw/
│   ├── 1B_distinct_values/
│   ├── 1A_merged_data_hourly_2023_2025.csv
│   ├── 2A_cleaned_no_duplicates.csv
│   ├── 2B_quality_checked.csv
│   ├── 2C_missing_values_handled.csv
│   ├── 2D_validated_final_dataset.csv
│   ├── 3B_engineered_dataset.csv
│   ├── 4A_outliers_handled.csv
│   ├── 4B_skewness_handled.csv
│   ├── 4D_scaled_dataset.csv
│   └── 4E_selected_dataset.csv
│
├── models/
│   └── scaler.pkl
│
├── pictures/
│   ├── pollutant_correlation_heatmap.png
│   ├── pollutant_vs_predictors_heatmap.png
│   └── 4C_visualization_before_after/
│       ├── pm25_distribution_comparison.png
│       ├── pollution_stagnation_index_distribution_comparison.png
│       ├── rain_mm_distribution_comparison.png
│       ├── temp_wind_interact_distribution_comparison.png
│       └── total_generation_mw_distribution_comparison.png
│
└── README.md
```

---

## Topologjia e pipeline-it

Pipeline-i është ndërtuar si një sekuencë hapash modularë, ku secili skript:

- lexon një output të fazës paraprake,
- kryen një transformim të caktuar,
- dhe shkruan një output të ri të versionuar.

Rrjedha logjike është kjo:

1. **Mbledhja e të dhënave**  
   Shkarkimi / përgatitja e burimeve bruto.

2. **Integrimi i të dhënave**  
   Bashkimi i ndotjes, motit dhe energjisë në një dataset të përbashkët orar.

3. **Distinct value profiling**  
   Nxjerrja e vlerave unike për atribute kyçe numerike.

4. **Data cleaning dhe quality checks**  
   Heqja e duplikateve, korrigjimi i vlerave jo-logjike, plotësimi i mungesave, validimi kronologjik dhe fizik.

5. **Target analysis dhe exploratory correlation analysis**  
   Analiza statistikore fillestare e ndotësve dhe lidhjeve me tiparet shpjeguese.

6. **Feature engineering**  
   Krijimi i tipareve kohore, lag-ve, rolling windows, ndërveprimeve dhe vektorëve të erës.

7. **Outlier handling**  
   Kufizimi i vlerave ekstreme me quantile capping.

8. **Skewness handling**  
   Transformime `log1p` dhe `Yeo-Johnson` për kolonat e shtrembëruara.

9. **Before/after visualization**  
   Krahasime histogramash para dhe pas transformimeve.

10. **Scaling**  
    Standardizimi i të gjitha kolonave numerike.

11. **Feature selection**  
    Heqja e tipareve problematike dhe reduktimi i multikolinearitetit me VIF.

---

## Pershkrimi i detajuar i cdo skripte

## Data collection

### `get_kosova_air_quality_data.ps1`
Ky skript PowerShell përdoret për shkarkimin e të dhënave arkivore nga OpenAQ për disa `location IDs` të lidhura me Prishtinën ose pikat përkatëse të matjes.

#### Cfare ben skripta
- krijon folder-in bazë të ruajtjes në disk,
- iteron mbi një listë `location IDs`,
- për secilin lokacion përdor komandën `aws s3 cp` për të shkarkuar skedarët `.csv.gz` nga arkiva publike e OpenAQ,
- ruan të dhënat në nënfolderë të ndarë sipas `location ID`.

#### Qellimi
Ky hap siguron mbledhjen e të dhënave bruto të ndotjes / matjeve për përpunim të mëtejshëm.

#### Lokacionet e përdorura
Në versionin aktual përdoren:
- `2536`
- `7674`
- `7931`
- `7933`
- `9337`

#### Output
Skedarët bruto ruhen lokalisht në strukturë të ndarë sipas lokacionit.

---

### `get_prishtina_air_quality_data.ipynb`
Ky notebook shërben si mjedis interaktiv për mbledhje, eksplorim, filtrime dhe/ose konsolidim të të dhënave të cilësisë së ajrit për Prishtinën.

Meqë logjika e plotë e notebook-ut nuk është përfshirë këtu në README, roli i tij në projekt është:
- të ndihmojë në eksplorimin fillestar të të dhënave,
- të përgatisë ose eksportojë skedarët bruto/finalë të përdorur më pas në pipeline,
- të shërbejë si hap ndërmjetës midis burimeve online dhe CSV-ve në `data/raw/`.

---

## Integration

### `1A_merge_data.py`
Ky është hapi themelor i integrimit të të tre burimeve.

#### Input
- `data/raw/prishtina_air_quality_2023_2025.csv`
- `data/raw/prishtina_weather_2023_2026.csv`
- `data/raw/prishtina_energy_production_2023_2026.csv`

#### Hapat kryesorë
1. Lexon dataset-in e ndotjes së ajrit.
2. Lexon dataset-in meteorologjik, duke anashkaluar rreshtat hyrës jo-standardë.
3. Lexon dataset-in e energjisë pa header standard dhe e zbulon automatikisht rreshtin e header-it.
4. Normalizon emrat e kolonave të energjisë:
   - `Ora Hour` → `hour`
   - `DATA Date` → `date`
   - `A3 (MW)` → `A3_MW`
   - `A4 (MW)` → `A4_MW`
   - `A5 (MW)` → `A5_MW`
   - `B1 (MW)` → `B1_MW`
   - `B2 (MW)` → `B2_MW`
5. Konverton kolonat kohore në `datetime`.
6. Harmonizon timezone-in e ndotjes dhe motit në `Europe/Belgrade`, pastaj i kthen në naive timestamps.
7. Pastron duplikatet sipas `datetime`.
8. Për dataset-in e energjisë:
   - konverton `date`,
   - konverton `hour`,
   - krijon `datetime`,
   - llogarit `total_generation_mw`.
9. Zgjedh vetëm kolonat relevante nga secili burim.
10. Kryen dy merge-e me `how="inner"`:
    - ndotja + moti,
    - pastaj rezultati + energjia.
11. Krijon kolonat:
    - `date`
    - `hour`
    - `interval_start`

#### Output
- `data/1A_merged_data_hourly_2023_2025.csv`

#### Roli ne pipeline
Ky skript krijon dataset-in e parë të integruar orar, që shërben si bazë për të gjitha hapat pasues.

---

## Distinct values

### `1B_distinct_values.py`
Ky skript bën profilizimin e vlerave unike për një grup kolonash kryesore.

#### Input
- `data/1A_merged_data_hourly_2023_2025.csv`

#### Kolonat e përfshira
- ndotësit: `co`, `no2`, `o3`, `pm10`, `pm25`, `so2`
- atributet meteorologjike:
  - temperatura
  - reshjet
  - bora
  - lagështia relative
  - drejtimi i erës
  - shpejtësia e erës
- kolonat e energjisë:
  - `A3_MW`
  - `A4_MW`
  - `A5_MW`
  - `B1_MW`
  - `B2_MW`
  - `total_generation_mw`


#### Cfare ben
- lexon dataset-in e integruar,
- për secilën kolonë nxjerr vlerat unike jo-null,
- i rendit,
- dhe i ruan si CSV të ndarë në folderin `data/1B_distinct_values/`.

#### Output
Folderi `1B_distinct_values/` përmban një skedar të veçantë për secilin atribut, p.sh.:
- `distinct_co.csv`
- `distinct_no2.csv`
- `distinct_o3.csv`
- `distinct_pm10.csv`
- `distinct_pm25.csv`
- `distinct_so2.csv`
- `distinct_a3_mw.csv`
- `distinct_a4_mw.csv`
- `distinct_a5_mw.csv`
- `distinct_b1_mw.csv`
- `distinct_b2_mw.csv`
- `distinct_total_generation_mw.csv`
- si dhe skedarët për atributet meteorologjike të pastruara sipas emërtimit.


#### Roli ne pipeline
Ky hap mbështet eksplorimin fillestar të shpërndarjeve dhe kontrollin e domenit të vlerave.

---

## Data cleaning

### `2A_datetime_and_duplicates.py`
Ky skript kryen pastrimin fillestar të dimensionit kohor dhe duplikateve.

#### Input
- `data/1A_merged_data_hourly_2023_2025.csv`

#### Cfare ben
- konverton `datetime` në format korrekt,
- heq rreshtat ku `datetime` është invalid,
- rendit dataset-in sipas kohës,
- numëron duplikatet,
- heq duplikatet e plota.

#### Output
- `data/2A_cleaned_no_duplicates.csv`

#### Roli ne pipeline
Siguron që dataset-i i integruar të ketë rend kronologjik korrekt dhe të mos ketë rreshta të përsëritur.

---

### `2B_data_quality_cleaning.py`
Ky skript zbaton rregulla të cilësisë së të dhënave.

#### Input
- `data/2A_cleaned_no_duplicates.csv`

#### Cfare ben
1. Për ndotësit:
   - zëvendëson vlerat negative me `NaN`, sepse fizikisht nuk kanë kuptim.
2. Për drejtimin e erës:
   - normalizon këndet me operatorin `% 360`.
3. Për reshjet dhe borën:
   - kufizon vlerat minimale në `0`.
4. Për kolonat e energjisë:
   - kufizon vlerat negative në `0`.
5. Për lagështinë relative:
   - kufizon vlerat në intervalin `[0, 100]`.
6. Për `total_generation_mw`:
   - e rillogarit nga `A3_MW + A4_MW + A5_MW + B1_MW + B2_MW`
   - dhe korrigjon mospërputhjet me totalin ekzistues.
7. Rrumbullakon kolonat numerike në 3 shifra dhjetore.

#### Output
- `data/2B_quality_checked.csv`

#### Roli ne pipeline
Ky hap vendos validim fizik dhe konsistencë numerike mbi të dhënat.

---

### `2C_missing_values_handling.py`
Ky skript trajton vlerat mungesë.

#### Input
- `data/2B_quality_checked.csv`

#### Strategjia e trajtimit
- `pm10` dhe `pm25`: plotësohen me `backfill`
- `co`, `no2`, `o3`, `so2`: plotësohen me `forward fill`
- në fund aplikohet kombinimi `ffill().bfill()` për gjithë dataset-in

#### Cfare ben
- llogarit mungesat për kolonë dhe përqindjen e tyre,
- raporton sa vlera janë plotësuar për secilin ndotës,
- plotëson vlerat mungesë sipas logjikës së përcaktuar,
- verifikon sa `NULL` mbeten në fund.

#### Output
- `data/2C_missing_values_handled.csv`

#### Roli ne pipeline
Ky hap shmang humbjen e rreshtave dhe prodhon një dataset të plotë për analizat pasuese.

---

### `2D_validate_final_dataset.py`
Ky skript bën validimin final të dataset-it pas trajtimit të mungesave.

#### Input
- `data/2C_missing_values_handled.csv`

#### Cfare ben
1. Kontrollon raportin fizik ndërmjet:
   - `pm25`
   - `pm10`
   
   dhe korrigjon rastet kur `pm25 > pm10` duke vendosur `pm25 = pm10`.

2. Kontrollon gaps kohore:
   - konverton `datetime`,
   - llogarit diferencën ndërmjet rreshtave,
   - numëron boshllëqet më të mëdha se 1 orë.

3. Kontrollon nëse kanë mbetur `NULL`.

#### Output
- `data/2D_validated_final_dataset.csv`

#### Roli ne pipeline
Ky është dataset-i final i pastruar dhe validuar, mbi të cilin kryhen analiza dhe inxhinierim tiparesh.

---

## Feature engineering

### `3A_target_analysis.py`
Ky skript kryen analizën fillestare të target-it dhe marrëdhënieve të tij me tiparet shpjeguese.

#### Input
- `data/2D_validated_final_dataset.csv`

#### Cfare ben
1. Gjeneron statistika përmbledhëse për ndotësit:
   - `co`
   - `no2`
   - `o3`
   - `pm10`
   - `pm25`
   - `so2`

2. Formon një subset me:
   - ndotësit,
   - kolonat e energjisë,
   - kolonat meteorologjike.

3. Llogarit matricën e korrelacionit.

4. Krijon dy heatmap-a:
   - korrelacioni i ndotësve me energjinë dhe motin,
   - korrelacioni mes vetë ndotësve.

#### Output
- `pictures/pollutant_vs_predictors_heatmap.png`
- `pictures/pollutant_correlation_heatmap.png`

#### Roli ne pipeline
Ky hap ndihmon në identifikimin e lidhjeve lineare fillestare dhe në justifikimin e tipareve të përdorura më pas në feature engineering.

---

### `3B_feature_engineering.py`
Ky skript ndërton dataset-in e pasuruar me tipare të reja.

#### Input
- `data/2D_validated_final_dataset.csv`

#### Target
- `pm25`

#### Cfare ben

##### 1. Pergatitje kohore
- konverton `datetime`,
- rendit dataset-in kronologjikisht,
- nxjerr:
  - `hour`
  - `day_of_week`
  - `month`

##### 2. Encodim ciklik
Krijon:
- `hour_sin`
- `hour_cos`
- `month_sin`
- `month_cos`

Qëllimi është të përfaqësojë natyrën ciklike të orës dhe muajit.

##### 3. Lag features
Për kolonat:
- `total_generation_mw`
- `wind_speed_10m (km/h)`
- `temperature_2m (°C)`

krijohen lag-e:
- `lag_1h`
- `lag_3h`
- `lag_6h`

##### 4. Rolling features
Krijohen:
- `total_gen_rolling_sum_12h`
- `total_gen_rolling_sum_24h`

##### 5. Interaction features
Krijohen:
- `temp_wind_interact`
- `generation_humidity_interact`

##### 6. Stagnation proxy
Krijohet:
- `pollution_stagnation_index = total_generation_mw / (wind_speed + 0.1)`

Ky indikator përpiqet të përfaqësojë situatat kur ka prodhim të lartë dhe erë të ulët, pra kushte më të favorshme për grumbullim ndotjesh.

##### 7. Wind vector decomposition
Nga shpejtësia dhe drejtimi i erës krijohen:
- `wind_x_vector`
- `wind_y_vector`

##### 8. Heqja e rreshtave me `NaN`
Pas krijimit të lag-eve dhe rolling windows hiqen rreshtat fillestarë që mbeten pa vlera të plota.

#### Output
- `data/3B_engineered_dataset.csv`

#### Roli ne pipeline
Ky është dataset-i i parë i pasuruar me tipare që modelojnë dinamikat kohore, ndikimet meteorologjike dhe ndërveprimet me prodhimin e energjisë.

---

## Preprocessing

### `4A_outlier_treatment.py`
Ky skript trajton outlier-at me quantile capping.

#### Input
- `data/3B_engineered_dataset.csv`

#### Strategjia
Për secilën kolonë numerike kandidate:
- kufiri i poshtëm = quantile `0.5%`
- kufiri i sipërm = quantile `99.5%`

Vlerat jashtë këtij intervali nuk fshihen, por priten në kufijtë përkatës.

#### Kolonat e përjashtuara
- `datetime`
- `date`
- disa tipare ciklike dhe vektorë strukturorë si:
  - `hour_sin`
  - `hour_cos`
  - `month_sin`
  - `month_cos`
  - `wind_x_vector`
  - `wind_y_vector`

#### Cfare ben
- identifikon kolonat numerike kandidate,
- llogarit kufijtë e poshtëm dhe të sipërm,
- numëron sa vlera u cap-en në secilin krah,
- krijon një raport për tiparet me më shumë vlera të kufizuara.

#### Output
- `data/4A_outliers_handled.csv`

#### Roli ne pipeline
Ky hap redukton ndikimin e vlerave ekstreme pa humbur rreshta.

---

### `4B_skewness_treatment.py`
Ky skript trajton shtrembërimin e shpërndarjes së kolonave numerike.

#### Input
- `data/4A_outliers_handled.csv`

#### Strategjia
Për secilën kolonë numerike:
- llogaritet skewness,
- nëse `|skew| > 1.0`, zbatohet transformim.

#### Llojet e transformimit
- nëse kolona ka vetëm vlera jo-negative:
  - përdoret `log1p`
- ndryshe:
  - përdoret `PowerTransformer(method="yeo-johnson")`

#### Cfare ben
- krahason skewness para dhe pas transformimit,
- ruan metodën e përdorur për secilën kolonë,
- raporton mean absolute skewness dhe median absolute skewness para/pas.

#### Output
- `data/4B_skewness_handled.csv`

#### Roli ne pipeline
Ky hap i bën shpërndarjet më të përshtatshme për standardizim, analiza lineare dhe modele machine learning.

---

### `4C_visualization_before_after.py`
Ky skript gjeneron histogramat krahasuese para dhe pas trajtimit të outlier-ave dhe skewness.

#### Input
- `data/3B_engineered_dataset.csv`
- `data/4A_outliers_handled.csv`
- `data/4B_skewness_handled.csv`

#### Tiparet e vizualizuara
- `pm25`
- `total_generation_mw`
- `pollution_stagnation_index`
- `rain (mm)`
- `temp_wind_interact`

#### Cfare ben
Për secilin atribut:
- vizaton tre histogramë në të njëjtën figurë:
  - para trajtimit,
  - pas trajtimit të outlier-ave,
  - pas trajtimit të skewness.

#### Output
Folderi:
- `pictures/4C_visualization_before_after/`

me figurat:
- `pm25_distribution_comparison.png` :

<img width="4470" height="1191" alt="image" src="https://github.com/user-attachments/assets/353ee2de-dee3-4b2e-973c-a8ac3f2a7825" />

  
- `total_generation_mw_distribution_comparison.png` :

<img width="4468" height="1191" alt="image" src="https://github.com/user-attachments/assets/053639ff-459b-4811-baef-55489f941ead" />

- `pollution_stagnation_index_distribution_comparison.png` :

<img width="4470" height="1191" alt="image" src="https://github.com/user-attachments/assets/65d5d6de-60ce-443f-a699-1de5b5714a0e" />

- `rain_mm_distribution_comparison.png` :

<img width="4467" height="1191" alt="image" src="https://github.com/user-attachments/assets/9c1eed28-1d22-49a2-bc64-ca4436cf0df9" />

- `temp_wind_interact_distribution_comparison.png` :

<img width="4470" height="1191" alt="image" src="https://github.com/user-attachments/assets/662d5921-854e-49bf-a7ba-8358c1249d51" />


#### Roli ne pipeline
Ky hap dokumenton vizualisht efektin e transformimeve statistikore.

---

### `4D_feature_scaling.py`
Ky skript standardizon të gjitha kolonat numerike.

#### Input
- `data/4B_skewness_handled.csv`

#### Cfare ben
- ndan kolonat jo-numerike:
  - `datetime`
  - `date`
- standardizon të gjitha kolonat e tjera me `StandardScaler`,
- rikombinon kolonat kohore me kolonat e shkallëzuara,
- ruan scaler-in e trajnuar.

#### Output
- `data/4D_scaled_dataset.csv`
- `models/scaler.pkl`

#### Roli ne pipeline
Ky hap siguron që tiparet numerike të jenë në të njëjtën shkallë dhe gati për feature selection ose modelim.

---

### `4E_feature_selection.py`
Ky skript kryen reduktimin final të tipareve.

#### Input
- `data/4D_scaled_dataset.csv`

#### Target
- `pm25`

#### Strategjia e seleksionimit

##### 1. Heqje manuale e kolonave jo të dëshiruara
Hiqen:
- ndotësit e tjerë si variabla hyrëse:
  - `co`
  - `no2`
  - `o3`
  - `pm10`
  - `so2`
- kolona strukturore:
  - `A3_MW`
  - `A4_MW`
  - `A5_MW`
  - `B1_MW`
  - `B2_MW`
  - `hour`
  - `month`
  - `day_of_week`
- të gjitha kolonat me `lag` në emër
- çdo kolonë tjetër që përmban `pm25` përveç target-it

##### 2. Heqje e kolonave konstante ose pothuaj konstante
- kolona me vetëm 1 vlerë unike
- kolona me devijim standard pothuaj zero

##### 3. VIF-based elimination
Për kolonat e mbetura:
- llogaritet `Variance Inflation Factor (VIF)`
- hiqet iterativisht kolona me VIF më të lartë derisa:
  - VIF maksimal të jetë më i vogël ose i barabartë me `7.0`

##### 4. Raportim
Në fund raportohet:
- madhësia e dataset-it fillestar,
- madhësia e dataset-it final,
- numri i tipareve finale,
- tiparet e mbajtura, të renditura sipas korrelacionit absolut me `pm25`.

#### Output
- `data/4E_selected_dataset.csv`

#### Roli ne pipeline
Ky është dataset-i final i reduktuar, i përgatitur për modelim statistikor ose machine learning me target `pm25`.

---

## Artefaktet dhe output-et e krijuara

### Dataset-et e ruajtura ne `data/`
- `1A_merged_data_hourly_2023_2025.csv`  
  Dataset-i i parë i integruar orar.

- `2A_cleaned_no_duplicates.csv`  
  Versioni pa duplikate dhe me `datetime` të validuar.

- `2B_quality_checked.csv`  
  Versioni pas rregullave të cilësisë.

- `2C_missing_values_handled.csv`  
  Versioni pas imputimit dhe plotësimit të mungesave.

- `2D_validated_final_dataset.csv`  
  Dataset-i final i pastruar dhe validuar.

- `3B_engineered_dataset.csv`  
  Dataset-i me tipare të reja.

- `4A_outliers_handled.csv`  
  Dataset-i pas outlier capping.

- `4B_skewness_handled.csv`  
  Dataset-i pas transformimeve kundër skewness.

- `4D_scaled_dataset.csv`  
  Dataset-i i standardizuar.

- `4E_selected_dataset.csv`  
  Dataset-i final i reduktuar për modelim.

### Artefakte shtese
- `models/scaler.pkl`  
  Objekti i `StandardScaler` për ripërdorim në inferencë ose pipeline të mëtejshme.

- `data/1B_distinct_values/`  
  Folder me vlera unike për atributet kryesore.

---

## Vizualizimet e gjeneruara

### 1. Heatmap-at nga analiza fillestare
#### `pictures/pollutant_vs_predictors_heatmap.png`
Paraqet korrelacionin ndërmjet ndotësve dhe tipareve të energjisë + motit.

#### `pictures/pollutant_correlation_heatmap.png`
Paraqet korrelacionin ndërmjet vetë ndotësve atmosferikë.

### 2. Histogramat krahasuese para/pas
Folderi `pictures/4C_visualization_before_after/` përmban figura që krahasojnë shpërndarjen:
- para trajtimit,
- pas trajtimit të outlier-ave,
- pas trajtimit të skewness.

#### Figurat aktuale
- `pm25_distribution_comparison.png`
- `pollution_stagnation_index_distribution_comparison.png`
- `rain_mm_distribution_comparison.png`
- `temp_wind_interact_distribution_comparison.png`
- `total_generation_mw_distribution_comparison.png`

### Vend per figurat ne README
Këtu mund të shtohen më vonë figurat me sintaksë si:

Pollutant vs Predictors Heatmap:

<img width="2702" height="2072" alt="image" src="https://github.com/user-attachments/assets/e02dfac3-c9f8-44ef-847e-efbefa69936c" />

Pollutant Correlation Heatmap:

<img width="1911" height="1580" alt="image" src="https://github.com/user-attachments/assets/926df5ae-7a6b-43c5-a9be-b2030dc6a7c7" />


---

## Teknikat e zbatuara dhe lidhja me lenden

Ky projekt përmbush në mënyrë të drejtpërdrejtë temat kryesore të lëndës “Përgatitja dhe vizualizimi i të dhënave”.

### 1. Data collection
- Shkarkim dhe konsolidim i të dhënave nga burime të ndryshme.
- Përdorim i PowerShell, notebook-ut dhe CSV-ve bruto.

### 2. Data integration
- Bashkim i tre burimeve heterogjene mbi bosht kohor të përbashkët.
- Harmonizim i formateve të kohës dhe timezone.

### 3. Data cleaning
- Heqja e duplikateve.
- Korrigjimi i vlerave jo-logjike.
- Kufizim i vlerave fizike jashtë intervaleve të pranueshme.

### 4. Missing value handling
- Forward fill
- Backfill
- Plotësim i të dhënave pa heqje agresive të rreshtave

### 5. Validation
- Kontrolli fizik `PM2.5 <= PM10`
- Kontrolli i gaps kohore
- Kontrolli final i `NULL`

### 6. Exploratory data analysis
- Statistika përmbledhëse
- Matrica korrelacioni
- Heatmap-a për target-in dhe predictor-at

### 7. Feature engineering
- Encodim ciklik i kohës
- Lag features
- Rolling features
- Interaction terms
- Wind decomposition
- Domain-inspired stagnation index

### 8. Outlier handling
- Quantile capping me kufijtë `0.5%` dhe `99.5%`
- Qasje robuste pa fshirje të rreshtave

### 9. Skewness handling
- `log1p`
- `Yeo-Johnson`
- Krahasim para/pas me statistika dhe vizualizime

### 10. Scaling
- Standardizim i kolonave numerike me `StandardScaler`

### 11. Feature selection
- Heqje manuale e kolonave jorelevante ose problematike
- Heqje e kolonave konstante
- Reduktim i multikolinearitetit përmes `VIF`

---

## Ekzekutimi i projektit

### Parakushtet
- Python 3.10+ ose më i ri
- `pip`
- mjedis virtual i rekomanduar
- për skriptin PowerShell: qasje në `aws cli` nëse përdoret shkarkimi nga OpenAQ archive

### Instalimi i librarive
```bash
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels
```

### Ekzekutimi i pipeline-it
Skriptat ekzekutohen sipas rendit logjik:

```bash
python src/integration/1A_merge_data.py
python src/distinct_values/1B_distinct_values.py

python src/data_cleaning/2A_datetime_and_duplicates.py
python src/data_cleaning/2B_data_quality_cleaning.py
python src/data_cleaning/2C_missing_values_handling.py
python src/data_cleaning/2D_validate_final_dataset.py

python src/feature_engineering/3A_target_analysis.py
python src/feature_engineering/3B_feature_engineering.py

python src/preprocessing/4A_outlier_treatment.py
python src/preprocessing/4B_skewness_treatment.py
python src/preprocessing/4C_visualization_before_after.py
python src/preprocessing/4D_feature_scaling.py
python src/preprocessing/4E_feature_selection.py
```

### Renditja e varësive
Çdo skript varet nga output-i i mëparshëm. Prandaj rekomandohet ekzekutimi në rend strikt.

---

## Rezultati final i pipeline-it

Produkti final i këtij projekti është:

- një dataset i integruar, i pastër dhe i validuar,
- një dataset i pasuruar me tipare domethënëse kohore dhe meteorologjike,
- një version i trajtuar për outlier-a dhe skewness,
- një version i standardizuar,
- dhe në fund një subset final tiparesh me multikolinearitet të reduktuar.

Dataset-i final:
- `data/4E_selected_dataset.csv`

është forma më e përshtatshme për:
- modelim prediktiv të `PM2.5`,
- regresion,
- krahasim modelesh machine learning,
- analiza statistikore të marrëdhënieve mes energjisë, motit dhe ndotjes.

---

## Permirsime te mundshme ne vazhdim

Në vazhdim, ky projekt mund të zgjerohet me:

- modele regresioni për parashikimin e `PM2.5`,
- krahasim modelesh si Linear Regression, Random Forest, XGBoost, SVR, LSTM,
- validim temporal `train/validation/test split` sipas kohës,
- shtim të më shumë stacioneve ose lokacioneve,
- ndërtim dashboard-i interaktiv për monitorim dhe interpretim,
- analizë më të avancuar të rëndësisë së tipareve,
- krahasim të performancës para dhe pas feature selection.

---

## Kontributi i anetareve

Ky seksion mund të plotësohet sipas ndarjes reale të punës, për shembull:

- **Data collection dhe integrimi fillestar**
- **Data cleaning dhe validation**
- **Feature engineering**
- **Preprocessing, scaling dhe feature selection**
- **Dokumentimi dhe përgatitja e README**

---

## Acknowledgments

- Universiteti i Prishtinës
- Fakulteti i Inxhinierisë Elektrike dhe Kompjuterike
- Dr. Sc. Mërgim H. Hoti
- Burimet publike dhe institucionale të përdorura për ndërtimin e dataset-eve hyrëse
- Të gjithë anëtarët e grupit që kontribuan në ndërtimin e pipeline-it

