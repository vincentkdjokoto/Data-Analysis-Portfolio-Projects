"""
E-Commerce Sales Analysis
Author: [Your Name]
Description: Comprehensive analysis of online retail sales data
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

class EcommerceSalesAnalyzer:
    def __init__(self, filepath):
        """Initialize the analyzer with data filepath"""
        self.df = None
        self.filepath = filepath
        
    def load_data(self):
        """Load and perform initial data inspection"""
        print("Loading data...")
        self.df = pd.read_csv(self.filepath)
        print(f"Data loaded: {self.df.shape[0]} rows, {self.df.shape[1]} columns")
        return self.df
    
    def clean_data(self):
        """Clean and preprocess the data"""
        print("\nCleaning data...")
        
        # Convert date columns
        self.df['order_date'] = pd.to_datetime(self.df['order_date'])
        
        # Remove duplicates
        initial_rows = len(self.df)
        self.df = self.df.drop_duplicates()
        print(f"Removed {initial_rows - len(self.df)} duplicate rows")
        
        # Handle missing values
        print(f"\nMissing values before cleaning:")
        print(self.df.isnull().sum())
        
        # Remove rows with missing critical data
        self.df = self.df.dropna(subset=['customer_id', 'product_id', 'quantity'])
        
        # Fill missing values for other columns
        self.df['discount'] = self.df['discount'].fillna(0)
        
        # Calculate revenue
        self.df['revenue'] = self.df['quantity'] * self.df['unit_price'] * (1 - self.df['discount'])
        
        # Create time-based features
        self.df['year'] = self.df['order_date'].dt.year
        self.df['month'] = self.df['order_date'].dt.month
        self.df['quarter'] = self.df['order_date'].dt.quarter
        self.df['day_of_week'] = self.df['order_date'].dt.day_name()
        self.df['year_month'] = self.df['order_date'].dt.to_period('M')
        
        print(f"\nData cleaning complete. Final shape: {self.df.shape}")
        return self.df

def main():
    """Main execution function"""
    analyzer = EcommerceSalesAnalyzer('data/ecommerce_data.csv')
    analyzer.load_data()
    analyzer.clean_data()
    print("\nAnalysis complete!")

if __name__ == "__main__":
    main()
