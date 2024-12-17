import yfinance as yf
import pandas as pd

class StockDataLoader:
    """Class for loading stock data from Yahoo Finance."""
    
    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date

    def load_data(self):
        """
        Load stock data from Yahoo Finance.
        
        Returns:
        --------
        pandas.DataFrame
            Stock data with columns: Date, Open, High, Low, Close, Volume
        
        Raises:
        -------
        ValueError
            If no data is found for the ticker or date range
        """
        try:
            data = yf.download(self.ticker, start=self.start_date, end=self.end_date)
            if data.empty:
                raise ValueError(f"No data found for ticker '{self.ticker}'")
            data.reset_index(inplace=True)
            return data
        except Exception as e:
            raise ValueError(f"Error loading data: {str(e)}")