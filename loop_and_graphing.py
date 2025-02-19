import time
import pandas as pd
import matplotlib.pyplot as plt
from scrape_raw_data import call_scraper

def read_from_csv(filename='scraped_data.csv'):
    df = pd.read_csv(filename)  # Read the CSV file into a DataFrame
    df.columns = df.columns.str.strip().str.lower()  # Normalize column names
    print("Column names:", df.columns.tolist())  # Debugging output
    return df

def create_graph():
    df = read_from_csv()  # Read data from the CSV file
    
    # Ensure 'date' column is in datetime format
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Convert 'price' column to numeric (handling any currency symbols)
    df['price'] = df['price'].astype(str).str.replace(r'[^\d.]', '', regex=True).astype(float)

    # Shorten product names (keeping only the first 3 words)
    df['short_name'] = df['product name'].apply(lambda x: ' '.join(x.split()[:3]))

    # Create a line plot
    plt.figure(figsize=(12, 6))

    # Plot each product's price over time
    products = df['short_name'].unique()
    for product in products:
        product_data = df[df['short_name'] == product]
        plt.plot(product_data['date'], product_data['price'], 
                 marker='o', linestyle='-', label=product)

    # Update layout
    plt.title('Product Prices Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.xticks(rotation=45)  # Rotate date labels for better visibility
    plt.legend(title='Products')  # Add a legend to differentiate products
    plt.tight_layout()

    # Show the plot
    plt.show()

def main():
    # while True:
    #     call_scraper()  # Call the scraper to save data to CSV
    #     create_graph()  # Create a graph from the CSV data
    #     time.sleep(86,400)  # Sleep for 1 hour
    create_graph()

if __name__ == "__main__":
    main()
