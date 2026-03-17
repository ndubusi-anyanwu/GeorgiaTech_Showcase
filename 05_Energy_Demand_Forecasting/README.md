# U.S. Energy Demand Forecasting with CNN-LSTM and Interactive Visualization

**Subject Area:** Deep Learning · Time Series Forecasting · Data Visualization · Energy Analytics · Team Research

---

## What It Does

This project forecasts five-year U.S. electricity generation by state using a hybrid **CNN-LSTM** deep learning architecture trained on a decade of historical EIA generation data (2015–2024). The CNN layers extract local temporal patterns while the LSTM layers model long-range sequential dependencies — a combination well-suited to the cyclical, trend-driven nature of energy demand. Results are visualized through an interactive **D3.js choropleth map** that allows users to explore projected generation levels across all 50 states by year.

The project also includes an **R-based statistical forecasting model** as a baseline comparison, and a full data cleaning and preprocessing pipeline in Python.

## Problem Addressed

Electricity grid planning requires reliable multi-year forecasts of regional generation capacity. Traditional statistical methods (ARIMA, regression) struggle to capture nonlinear seasonality and state-specific consumption patterns simultaneously. This project investigates whether a deep learning approach can produce more accurate and geographically granular forecasts than the baseline, and makes those forecasts accessible through an interactive visual interface.

## Practical Relevance

Energy demand forecasting has direct applications in grid infrastructure planning, renewable energy investment decisions, and climate policy modeling. The CNN-LSTM architecture used here is generalizable to other multivariate time series problems: financial forecasting, cybersecurity anomaly detection (e.g., detecting unusual traffic patterns over time), and industrial IoT sensor monitoring.

## Project Artifacts

| File | Description |
|------|-------------|
| `CNN_LSTM_model.py` | Model architecture definition (CNN + LSTM layers) |
| `CNN_LSTM_Forecast.py` | Training loop, evaluation, and forecast generation |
| `LSTM_preprocessing.py` | Feature engineering and sequence preparation |
| `Data_Clean_Code_04182025.py` | Raw data ingestion and cleaning pipeline |
| `modelGenerator.R` | R-based statistical baseline model |
| `maps.html` | Interactive D3.js choropleth visualization |
| `us_states.json` | GeoJSON for state-level map rendering |
| `2015_2024_Elec_Net_Gen_Data.csv` | Historical EIA electricity generation data |
| `Forecast_5Years_AllStates.csv` | Model output: 5-year state-level projections |
| `team201report.pdf` | Full technical report |
| `team201poster.pdf` | Conference-style project poster |
| `team201slides.pdf` | Presentation deck |

## Tools, Languages, and Libraries

Python · TensorFlow/Keras · NumPy · pandas · scikit-learn · R · D3.js · HTML/CSS · EIA open data

## Skills Demonstrated

- Deep learning for time series: hybrid CNN-LSTM architecture design and tuning
- Data engineering: multi-year CSV ingestion, feature normalization, and sequence windowing
- Interactive data visualization: building geographic choropleth maps with D3.js
- Statistical baseline modeling in R for comparison against deep learning approach
- Team research project management: proposal, implementation, report, and poster delivery
- Communicating technical findings to non-specialist audiences through visual storytelling

## Extension Ideas

- Incorporate weather data (temperature, precipitation) as exogenous features to improve forecast accuracy
- Extend to renewable energy mix forecasting (solar, wind, hydro) at the state level
- Deploy the D3.js visualization as a hosted web application for public access
- Apply transfer learning from this model to a related domain (e.g., water demand forecasting)

---

*Georgia Institute of Technology — MS Computer Science · CSE 6242: Data and Visual Analytics*
*Team Project — Team 201*
