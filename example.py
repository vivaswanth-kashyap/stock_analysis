from stock_analysis import StockAnalyzer

# Create an analyzer instance
analyzer = StockAnalyzer('AAPL', '2020-01-01', '2023-12-31')

# Calculate indicators with explicit MA windows
analyzer.calculate_indicators(ma_windows=[20, 50])

# Show dashboard
analyzer.plot_all()