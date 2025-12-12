"""
Generate sample e-commerce data for analysis
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_ecommerce_data(n_records=10000):
    """Generate synthetic e-commerce data"""
    
    np.random.seed(42)
    random.seed(42)
    
    # Generate date range
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2024, 12, 31)
    date_range = pd.date_range(start_date, end_date, freq='H')
    
    # Product data
    products = [
        ('Laptop', 'Electronics', 899.99),
        ('Smartphone', 'Electronics', 699.99),
        ('Headphones', 'Electronics', 149.99),
        ('T-Shirt', 'Clothing', 19.99),
        ('Jeans', 'Clothing', 49.99)
    ]
    
    data = []
    customer_ids = [f'CUST{i:05d}' for i in range(1, 2001)]
    
    for i in range(n_records):
        order_id = f'ORD{i+1:06d}'
        customer_id = random.choice(customer_ids)
        order_date = random.choice(date_range)
        
        product_name, category, unit_price = random.choice(products)
        product_id = f'PROD{products.index((product_name, category, unit_price))+1:03d}'
        
        quantity = np.random.choice([1, 2, 3, 4, 5], p=[0.5, 0.25, 0.15, 0.07, 0.03])
        discount = np.random.choice([0, 0.05, 0.10, 0.15, 0.20], p=[0.6, 0.2, 0.1, 0.07, 0.03])
        
        data.append({
            'order_id': order_id,
            'customer_id': customer_id,
            'order_date': order_date,
            'product_id': product_id,
            'product_name': product_name,
            'category': category,
            'quantity': quantity,
            'unit_price': unit_price,
            'discount': discount
        })
    
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    print("Generating sample e-commerce data...")
    df = generate_ecommerce_data(10000)
    df.to_csv('data/ecommerce_data.csv', index=False)
    print(f"Generated {len(df)} records")
