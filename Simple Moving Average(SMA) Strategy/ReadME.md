# Simple Moving Average (SMA) Strategy Quant Project

Welcome to the Simple Moving Average (SMA) Strategy Quant project! This repository is designed for educational purposes and does not encourage contributions. Please note that the project does not include backtesting and is not intended as financial advice.

## Table of Contents

1. [Introduction](#introduction)
2. [Strategy Overview](#strategy-overview)
3. [Project Structure](#project-structure)
4. [Getting Started](#getting-started)
5. [Usage](#usage)
6. [Disclaimer](#disclaimer)
7. [License](#license)

## Introduction

Quantitative trading involves using mathematical models, data analysis, and automated trading systems to make investment decisions. The SMA strategy is a popular and straightforward trading strategy that leverages Simple Moving Averages to identify potential buy and sell signals in financial markets.

This project provides a practical implementation of an SMA-based trading strategy and serves as an educational resource for those interested in quantitative finance and algorithmic trading.

## Strategy Overview

The SMA strategy involves calculating Simple Moving Averages for a given financial instrument (e.g., a stock or cryptocurrency) over different time periods. These moving averages are used to generate trading signals, such as:

- **Golden Cross**: When a shorter-term SMA (e.g., 50-day) crosses above a longer-term SMA (e.g., 200-day), it may signal a potential buy opportunity.
- **Death Cross**: When a shorter-term SMA crosses below a longer-term SMA, it may signal a potential sell opportunity.

## Project Structure

The project is organized as follows:

- **`data/`**: Contains historical price data for the financial instrument you want to analyze.
- **`strategies/`**: Includes Python scripts for implementing the SMA strategy.

## Getting Started

To get started with this SMA Strategy Quant project, follow these steps:

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/your-username/SMA-Strategy-Quant.git
   ```

2. Set up your Python environment with the necessary dependencies. You can use a virtual environment to manage dependencies.

   ```
   pip install -r requirements.txt
   ```

3. Prepare historical price data for the financial instrument you want to analyze. This data should be placed in the `data/` directory.

4. Customize the strategy parameters in the configuration files located in the `config/` directory.

## Usage

Once you've set up the project and configured the strategy parameters, you can run the strategy implementation scripts found in the `strategies/` directory. These scripts will generate trading signals based on the SMA strategy.

Make sure to import the required libraries at the beginning of your Python scripts:

```python
import datetime as dt
import matplotlib.pyplot as plt
import yfinance as yf
```

## Disclaimer

This project is for educational purposes only and should not be considered financial advice. The use of quantitative trading strategies involves risks, and past performance is not indicative of future results. Always conduct thorough research and consider seeking advice from a qualified financial professional before making any investment decisions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

Please remember that this project is intended for educational purposes and does not encourage contributions or provide financial advice.
