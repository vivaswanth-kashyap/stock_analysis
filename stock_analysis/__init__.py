"""
Stock Analysis Package
=====================

A Python package for analyzing stock market data using technical indicators,
trend analysis, and visualization tools.

Features:
---------
- Data loading from Yahoo Finance
- Technical analysis indicators (RSI, Moving Averages)
- Trend analysis (returns, volatility)
- Visualization tools for analysis

Example:
--------
>>> from stock_analysis import StockAnalyzer
>>> analyzer = StockAnalyzer('AAPL', '2020-01-01', '2023-12-31')
>>> analyzer.calculate_indicators()
>>> analyzer.plot_trends()
"""

from .data.loader import StockDataLoader
from .analysis.trends import TrendAnalyzer
from .analysis.indicators import TechnicalIndicators
from .visualization.plots import Plotter

class StockAnalyzer:
    """Main class for stock analysis."""
    
    def __init__(self, ticker, start_date, end_date):
        """Initialize stock analyzer with ticker and date range."""
        self.loader = StockDataLoader(ticker, start_date, end_date)
        self.data = self.loader.load_data()
        self.trends = TrendAnalyzer(self.data)
        self.indicators = TechnicalIndicators(self.data)
        self.plotter = Plotter(self.data)

    def calculate_indicators(self, ma_windows=[20, 50], rsi_window=14, volatility_window=20):
        """Calculate all technical indicators."""
        # Calculate returns first (needed for other indicators)
        self.trends.calculate_returns()
        
        # Calculate all indicators
        self.trends.calculate_volatility(window=volatility_window)
        self.indicators.calculate_moving_averages(windows=ma_windows)
        self.indicators.calculate_rsi(window=rsi_window)
        return self.data

    def plot_all(self):
        """Create all visualizations in a single dashboard."""
        self.plotter.plot_all()
