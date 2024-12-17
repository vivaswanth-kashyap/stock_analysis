import pandas as pd

class TechnicalIndicators:
    """Class for calculating technical indicators."""
    
    def __init__(self, data):
        self.data = data

    def calculate_moving_averages(self, windows=[20, 50]):
        """
        Calculate simple moving averages.
        
        Parameters:
        -----------
        windows : list
            List of periods for moving averages
        """
       
        try:
            for window in windows:
                column_name = f'{window}-Day MA'
                self.data[column_name] = self.data['Close'].rolling(window=window).mean()
            return self.data
        except Exception as e:
            raise ValueError(f"Error calculating moving averages: {str(e)}")

    def calculate_rsi(self, window=14):
        """
        Calculate Relative Strength Index (RSI).
        
        Parameters:
        -----------
        window : int
            RSI calculation period
        """
        try:
            delta = self.data['Close'].diff()
            gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
            rs = gain / loss
            self.data['RSI'] = 100 - (100 / (1 + rs))
            return self.data
        except Exception as e:
            raise ValueError(f"Error calculating RSI: {str(e)}")
