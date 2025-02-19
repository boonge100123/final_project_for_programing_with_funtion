import time
import pandas as pd
import matplotlib.pyplot as plt
from scrape_raw_data import call_scraper

def read_from_csv(filename='scraped_data.csv'):
    df = pd.read_csv(filename)  # Read the CSV file into a DataFrame
    return df

def create_graph():
    df = read_from_csv()  # Read data from the CSV file
    
    # Convert 'date' to datetime for proper plotting
    df['date'] = pd.to_datetime(df['date'])
    
    # Create a line plot
    plt.figure(figsize=(12, 6))
    
    # Plot each product's price over time
    products = df['Product Name'].unique()  # Get unique product names
    for product in products:
        product_data = df[df['Product Name'] == product]
        plt.plot(product_data['date'], product_data['Price'].replace({'\$': '', '': ''}, regex=True).astype(float), 
                 marker='o', linestyle='-', label=product)

    # Update layout
    plt.title('Product Prices Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.xticks(rotation=45)  # Rotate date labels for better visibility
    plt.yticks()  # Display y-axis ticks
    plt.legend(title='Products')  # Add a legend to differentiate products
    plt.tight_layout()

    # Show the plot
    plt.show()

def main():
    # while True:
    #     call_scraper()  # Call the scraper to save data to CSV
    #     create_graph()  # Create a graph from the CSV data
    #     time.sleep(3600)  # Sleep for 1 hour
    create_graph()

if __name__ == "__main__":
    main()
