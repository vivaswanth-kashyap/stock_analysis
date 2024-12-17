import numpy as np

class TrendAnalyzer:
    """Class for analyzing stock price trends."""
    
    def __init__(self, data):
        self.data = data

    def calculate_returns(self):
        """Calculate daily and cumulative returns."""
        try:
            self.data['Daily Return'] = self.data['Close'].pct_change()
            self.data['Cumulative Return'] = (1 + self.data['Daily Return']).cumprod() - 1
            return self.data
        except Exception as e:
            raise ValueError(f"Error calculating returns: {str(e)}")

    def calculate_volatility(self, window=20):
        """Calculate rolling volatility."""
        try:
            # Calculate daily volatility and annualize it
            daily_std = self.data['Daily Return'].rolling(window=window).std()
            self.data['20-Day Volatility'] = daily_std * np.sqrt(252)  # Annualized
            return self.data
        except Exception as e:
            raise ValueError(f"Error calculating volatility: {str(e)}")