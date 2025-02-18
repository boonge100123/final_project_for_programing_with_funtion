#python 

import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_setup import setup_driver

WEBSIGHT_INDEX = 0  # Column index for the website in the CSV file
URL_INDEX = 1  # Column index for the URL in the CSV file

def get_data_from_csv(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip the header row safely
        return [(row[WEBSIGHT_INDEX].strip().lower(), row[URL_INDEX].strip()) 
                for row in reader if len(row) > URL_INDEX and row[WEBSIGHT_INDEX].strip() and row[URL_INDEX].strip()]

def scrape_newegg_product(driver, url):
    driver.get(url)
    time.sleep(5)

    
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
    
def scrape_amazon_product(driver, url):
    driver.get(url)
    time.sleep(5)  # Allow time for the page to load

    try:
        # Extract product title
        title_element = driver.find_element(By.XPATH, "//span[@id='productTitle']")
        title = title_element.text.strip()

        # Extract price (Amazon has multiple formats, so we try different XPaths)
        try:
            price_element = driver.find_element(By.XPATH, "//span[@class='a-price-whole']")
            price = price_element.text.strip()
        except:
            price_element = driver.find_element(By.XPATH, "//span[contains(@class, 'a-price')]")
            price = price_element.text.strip()

        print(f"Amazon Product: {title}, Price: {price}")
        return title, price

    except Exception as e:
        print(f"Error scraping Amazon {url}: {e}")
        return None, None

def write_to_csv(data, file_path):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Website", "URL", "Product Name", "Price"])  # Write header
        writer.writerows(data)  # Write scraped data

def main():
    driver = setup_driver()
    urls = get_data_from_csv('user_data_request.csv')

    scraped_data = []
    for website, url in urls:
        print(f"Scraping: {url} from {website}")

        if website == "newegg":
            title, price = scrape_newegg_product(driver, url)
        elif website == "amazon":
            title, price = scrape_amazon_product(driver, url)  # New logic for Amazon

        if title and price:
            scraped_data.append((website, url, title, price))  # Store results
    
    driver.quit()  # Close the browser when done
    write_to_csv(scraped_data, 'scraped_data.csv')

if __name__ == "__main__":
    main()

