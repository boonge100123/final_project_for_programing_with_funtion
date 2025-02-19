#python 

import time
import csv
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    try:
        # Wait until the product title is present on the page
        title_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h1[@class='product-title']"))
        )
        title = title_element.text.strip()

        # Wait until the price element is present (try the specific format first)
        price_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@class='price-current']"))
        )
        price = price_element.text.strip()

        print(f"Newegg Product: {title}, Price: {price}")
        return title, price

    except Exception as e:
        print(f"Error scraping Newegg {url}: {e}")
        return None, None
    
def scrape_amazon_product(driver, url):
    driver.get(url)
    
    try:
        # Wait until the product title is present on the page
        title_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@id='productTitle']"))
        )
        title = title_element.text.strip()

        # Wait until the price element is present
        price_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='a-price-whole']"))
        )
        price_whole = price_element.text.strip()

        # Now, find the fractional part if it exists
        try:
            price_fraction_element = driver.find_element(By.XPATH, "//span[@class='a-price-symbol']")
            price_fraction = price_fraction_element.text.strip()
        except:
            price_fraction = "00"  # Default to "00" if no fraction is found

        # Combine whole and fractional parts
        price = f"{price_whole}.{price_fraction}"

        print(f"Amazon Product: {title}, Price: {price}")
        return title, price

    except Exception as e:
        print(f"Error scraping Amazon {url}: {e}")
        return None, None
    
def scrape_walmart_product(driver, url):
    driver.get(url)

    try:
        # Wait until the product title is present on the page
        title_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h1[@class='prod-ProductTitle-no-margin']"))
        )
        title = title_element.text.strip()

        # Wait until the price element is present
        price_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='price-group']"))
        )
        price = price_element.text.strip()

        print(f"Walmart Product: {title}, Price: {price}")
        return title, price

    except Exception as e:
        print(f"Error scraping Walmart {url}: {e}")
        return None, None

def scrape_other_websights(driver, url):
    driver.get(url)

    try:
        # Wait until the product title is present on the page
        title_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h1"))  # Adjust the XPath as needed for the specific website
        )
        title = title_element.text.strip()

        # Wait until the price element is present
        price_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='price']"))  # Adjust the XPath as needed
        )
        price = price_element.text.strip()

        print(f"Other Product: {title}, Price: {price}")
        return title, price

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None, None

def write_to_csv(data, file_path):
    file_exists = os.path.isfile(file_path)  # Check if the file already exists

    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        # Write header only if the file did not exist before
        if not file_exists:
            writer.writerow(["Website", "URL", "Product Name", "Price", "Date"])  # Write header
        writer.writerows(data)  # Write scraped data

def scrape_all_products(driver, urls):
    scraped_data = []
    
    for website, url in urls:
        date = datetime.now().strftime("%Y-%m-%d")
        print(f"Scraping: {url} from {website}")
        
        try:
            if website == "newegg":
                title, price = scrape_newegg_product(driver, url)
            elif website == "amazon":
                title, price = scrape_amazon_product(driver, url)
            elif website == "walmart":
                title, price = scrape_walmart_product(driver, url)
            else:
                title, price = scrape_other_websights(driver, url)
            
            if title and price:
                scraped_data.append((website, url, title, price, date))
                print(f"Successfully scraped: {title} for {price} from {website}")
            else:
                print(f"No title or price found for: {url}")

        except Exception as e:
            print(f"Error scraping {url}: {e}")

    driver.quit()  # Close the browser when done
    print('-------------------------------')
    print(scraped_data)
    print('-------------------------------')
    return scraped_data

def main():
    driver = setup_driver()
    urls = get_data_from_csv('user_data_request.csv')
    scraped_data = scrape_all_products(driver, urls)
    write_to_csv(scraped_data, 'scraped_data.csv')

if __name__ == "__main__":
    main()

