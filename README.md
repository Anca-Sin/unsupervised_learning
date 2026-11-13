# The Police Arrive Last: Data Analysis of Equity in US Fatal Encounters, 2015-2021

The project groups the fatal police encounters recorded by Mapping Police Violence (MPV) in the US, 2015-2021 (7,867 deaths), by the **situation** each death happened in: what brought police and the person together, whether police were called, armed status, weapon, threat level, fleeing, mental state, and the forces used. 

Topologically Integrated Geographic Encoding and Referencing (TIGER) gives tracts which help join MPV with the American Community Survey (ACS). Tracts are county subdivisions of generally 1,200-8,000 residents. ACS provides demographic and socioeconomic details per tract.

- **Latent class analysis** (StepMix; categories with missing values) finds **8 classes**, chosen from BIC, the SABIC curve and the classes together. Relative entropy is at 0.774 and 9 out of 10 refits from new seeds reach the same solution (ARI 0.978-0.994)
- **MDS** draws the deaths in 2D on the study's own dissimilarity, which compares two deaths only on the indicators both have recorded
- **Classes read through their descriptors:** age, gender, race, less-lethal also, poverty, population density. Race is corrected for classification error (three-step BCH)
- **Benchmarks:** deaths ÷ residents with bootstrap intervals, locally per race, gender and age band, and nationally per tract quintile of poverty and race segregation
- **Comparison slicer:** officer charged, read through race, armed status, mental state, gender, less-lethal also and class

## Repository layout

```
data/
├── 0_raw/{1_1_mpv, 1_2_tiger, 1_3_acs}/
├── 1_data_notebooks/{1_1_mpv, 1_2_tiger, 1_3_acs}/   # what each database's notebook saves, and its handmade decision files
└── 2_join_and_roles/                 # the five role tables, and the columns selected per role
notebooks/
├── 1_1_mpv.ipynb                     
├── 1_2_tiger.ipynb                   
├── 1_3_acs.ipynb                     
├── 2_join_and_roles.ipynb            # joins the saved files from the previous notebooks and builds the five role tables
├── 3_1_clustering.ipynb              # latent class analysis and its checks, MDS
└── 3_2_results_interpretations.ipynb # class descriptions, benchmarks, comparison slicer
outputs/                              
shared/                               
```

## Setup

Requires Python 3.12 and [uv](https://docs.astral.sh/uv/) (or plain pip/venv). From this folder:

```
uv venv --python 3.12
uv pip install -r requirements.txt
uv pip install -e .
```

## Running

The notebooks come **with executed outputs**: every result can be read without running anything.

To rerun, run the notebooks in their number order.

Data files are included except the TIGER tract file and the tract table `1_2_tiger` saves from it because they are too large (about 700 MB each).

Fixed seeds make every result reproducible.

## Data sources

| Source | Role | Access |
|---|---|---|
| Mapping Police Violence (MPV) | the deaths | downloaded by hand, 6 May 2026 |
| TIGER/Line 2022 | census-tract outlines and land area | not shipped, too large (713 MB): `1_2_tiger` downloads it with pygris |
| Census cartographic boundary file 2020, states (1:500,000) | state outlines: MPV's state check, the maps | downloaded with pygris, 10 October 2026 |
| ACS 5-year 2018-2022, Data Profiles DP05 and DP03 | tract demographics and poverty | downloaded by hand from data.census.gov, 29 October 2026 |

MPV states that its data is meant to be public, free to access and owned by no platform ([methodology](https://mappingpoliceviolence.org/methodology)). Credit: [Mapping Police Violence](https://mappingpoliceviolence.org/).
