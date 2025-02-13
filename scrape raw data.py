#python 

import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_setup import setup_driver

URL_INDEX = 1  # Column index for the URL in the CSV file

def get_data_from_csv(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip the header row safely
        return [row[URL_INDEX] for row in reader if len(row) > URL_INDEX and row[URL_INDEX].strip()]  # Skip empty rows

def scrape_newegg_product(driver, url):
    driver.get(url)
    time.sleep(5)  # Allow page to load (adjust based on speed)
    
    try:
        # Extract product title
        title_element = driver.find_element(By.XPATH, "//h1[@class='product-title']")
        title = title_element.text.strip()

        # Extract price (this might vary, so be ready to adjust the selector)
        price_element = driver.find_element(By.XPATH, "//li[@class='price-current']")
        price = price_element.text.strip()

        print(f"Product: {title}, Price: {price}")
        return title, price
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None, None

def main():
    driver = setup_driver()
    urls = get_data_from_csv('user_data_request.csv')

    scraped_data = []
    for url in urls:
        print(f"Scraping: {url}")
        title, price = scrape_newegg_product(driver, url)
        if title and price:
            scraped_data.append((url, title, price))  # Store results
    
    driver.quit()  # Close the browser when done
    
    # Save the scraped data to a new CSV file
    with open('scraped_newegg_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["URL", "Product Name", "Price"])  # Write header
        writer.writerows(scraped_data)  # Write scraped data

if __name__ == "__main__":
    main()

