
# 21cm.chops

*This project is ongoing and subject to continuous advancements and modifications.*

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg) ![License](https://img.shields.io/badge/license-MIT-blue.svg)  

This repository contains the code to generate the Brightness Temperature cube of 21 cm emission of HI for the redshift range \( 5.5 < z < 14 \).

## Features

- Simulates the 21 cm emission of neutral hydrogen (HI) over a range of redshifts.
- Outputs a Brightness Temperature cube for visualization and analysis.

## Prerequisites

- Python 3.x
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AkbarAC/21cm.chops.git
   cd 21cm.chops
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

   ```

## Usage

Run the main script to generate the Brightness Temperature cube:
```bash
python main.py
```

Modify configuration parameters (e.g., redshift range, resolution) in `config.yaml` as needed.

## Output

The generated Brightness Temperature cube will be saved in the `output/` directory. Visualizations can be enabled in the configuration.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

