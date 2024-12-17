from setuptools import setup, find_packages

setup(
    name="stock_analysis",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'yfinance'
    ],
    description="A stock market analysis package - Group Project",
)