# HkTxGNN - 香港藥品老藥新用預測系統

Hong Kong Drug Repurposing Predictions using TxGNN

## Overview

This project uses TxGNN (Therapeutic Genomics Neural Network) to predict potential new uses for drugs registered in Hong Kong.

## Data Sources

- **Drug Data**: Hong Kong Department of Health - Drug Office
  - Source: https://data.gov.hk/en-data/dataset/hk-dh-dh_do-hk-dh-do-pharmaceutical-product

## Features

- Knowledge Graph (KG) based drug repurposing predictions
- Deep Learning (DL) based TxGNN predictions
- FHIR R4 compatible API
- SMART on FHIR application support

## Usage

```bash
# Install dependencies
uv sync

# Run KG prediction
uv run python scripts/run_kg_prediction.py

# Generate FHIR resources
uv run python scripts/generate_fhir_resources.py
```

## License

MIT License

## Disclaimer

This project is for research purposes only and does not constitute medical advice.
Drug repurposing candidates require clinical validation before application.
