import matplotlib.pyplot as plt

class Plotter:
    """Class for creating analysis visualizations."""
    
    def __init__(self, data):
        self.data = data

    def plot_all(self):
        """Plot all analyses in a single figure with subplots."""
        fig, axs = plt.subplots(4, 1, figsize=(15, 20))
        fig.suptitle('Stock Analysis Dashboard', fontsize=16)
        
        # Plot 1: Price and Returns
        axs[0].plot(self.data['Date'], self.data['Close'], label='Close Price')
        if 'Cumulative Return' in self.data.columns:
            ax2 = axs[0].twinx()
            ax2.plot(self.data['Date'], self.data['Cumulative Return'], 
                    label='Cumulative Return', color='green', alpha=0.7)
            ax2.set_ylabel('Cumulative Return', color='green')
        axs[0].set_title('Price and Returns')
        axs[0].set_xlabel('Date')
        axs[0].set_ylabel('Price')
        axs[0].legend(loc='upper left')
        if 'Cumulative Return' in self.data.columns:
            ax2.legend(loc='upper right')
        
        # Plot 2: Moving Averages
        axs[1].plot(self.data['Date'], self.data['Close'], label='Close Price', color='blue')
        
        # Explicitly plot both moving averages
        if '20-Day MA' in self.data.columns:
            axs[1].plot(self.data['Date'], self.data['20-Day MA'], 
                       label='20-Day MA', color='red')
        if '50-Day MA' in self.data.columns:
            axs[1].plot(self.data['Date'], self.data['50-Day MA'], 
                       label='50-Day MA', color='green')
            
        axs[1].set_title('Moving Averages')
        axs[1].set_xlabel('Date')
        axs[1].set_ylabel('Price')
        axs[1].legend(loc='upper left')
        axs[1].grid(True)
        
        # Plot 3: RSI
        if 'RSI' in self.data.columns:
            axs[2].plot(self.data['Date'], self.data['RSI'], label='RSI', color='purple')
            axs[2].axhline(70, color='red', linestyle='--', label='Overbought (70)')
            axs[2].axhline(30, color='green', linestyle='--', label='Oversold (30)')
            axs[2].set_title('Relative Strength Index (RSI)')
            axs[2].set_xlabel('Date')
            axs[2].set_ylabel('RSI')
            axs[2].legend()
        
        # Plot 4: Volatility
        vol_column = '20-Day Volatility'
        if vol_column in self.data.columns:
            axs[3].plot(self.data['Date'], self.data[vol_column], 
                       label='Volatility', color='orange')
            axs[3].set_title('Volatility Analysis')
            axs[3].set_xlabel('Date')
            axs[3].set_ylabel('Volatility')
            axs[3].legend()
        
        plt.tight_layout()
        plt.show()
