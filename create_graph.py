import pandas as pd
import matplotlib.pyplot as plt

def read_from_csv(filename='scraped_data.csv'):
    df = pd.read_csv(filename)  # Read the CSV file into a DataFrame
    df.columns = df.columns.str.strip().str.lower()  # Normalize column names
    print("Column names:", df.columns.tolist())  # Debugging output
    return df

def create_graph():
    df = read_from_csv()  # Read data from the CSV file
    
    # Ensure 'date' is in the correct format
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Convert 'price' to a number. or strip non number characters and convert to float
    df['price'] = df['price'].astype(str).str.replace(r'[^\d.]', '', regex=True).astype(float)

    # Shorten product names (keeping only the first 3 words)
    df['short_name'] = df['product name'].apply(lambda x: ' '.join(x.split()[:3]))

    #  Remove duplicate entries with the same date, product name, and price
    df.drop_duplicates(subset=['date', 'short_name', 'price'], inplace=True)

    # Create a line plot
    plt.figure(figsize=(12, 6))

    # Plot each product's price over time
    products = df['short_name'].unique()
    for product in products:
        product_data = df[df['short_name'] == product]
        plt.plot(product_data['date'], product_data['price'], 
                 marker='o', linestyle='-', label=product)

        # Add price labels to each point
        for _, row in product_data.iterrows():
            plt.text(row['date'], row['price'], f"${row['price']:.2f}", 
                     fontsize=9, ha='right', va='bottom', color='black')

    # Update how it looks when the plot is oppened
    plt.title('Product Prices Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.xticks(rotation=45)  # Rotate date labels makes it a bit more readable
    plt.legend(title='Products')  # Add a legend to differentiate products
    plt.tight_layout()  # Adjust plot to fit labels
    plt.show() # Display the plot

def main():
    create_graph()  # Initial graph creation

if __name__ == "__main__":
    main()
