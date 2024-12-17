# Stock Analysis Package
A Python package for analyzing stock market data using technical indicators and visualization tools.

## Installation
Clone or download this repository, then install in development mode:
```bash
# Navigate to the project directory
cd stock_analysis

# Install in development mode
pip install -e .
```

## Requirements
- pandas
- numpy
- matplotlib
- yfinance

## Features
- Load stock data from Yahoo Finance
- Calculate technical indicators (RSI, Moving Averages)
- Analyze trends and volatility
- Create visualization plots

## Quick Start
```python
from stock_analysis import StockAnalyzer

# Initialize analyzer (example using Apple stock)
analyzer = StockAnalyzer('AAPL', '2020-01-01', '2023-12-31')

# Calculate indicators
analyzer.calculate_indicators()

# Create analysis dashboard
analyzer.plot_all()
```

## Project Structure
```
stock_analysis/
├── __init__.py         # Main package initialization
├── data/               # Data loading utilities
├── analysis/           # Technical analysis functions
└── visualization/      # Plotting and visualization tools
```

## Authors
- Vivaswanth Kashyap Madhusudhana
- Mythreya Namilikonda
- Ankith Tircovala

## Course Information
- Course: FE 520
- Semester: Fall 2024
```