#python 

import csv
import os
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_setup import setup_driver

WEBSIGHT_INDEX = 0  # Column index for the website in the CSV file
URL_INDEX = 1  # Column index for the URL in the CSV file

#! this is a csv reader function that reads the data from the csv file and returns the data in a list
def get_data_from_csv(file_path):
    with open(file_path, mode='r') as file: #open you csv file in read mode
        reader = csv.reader(file) #give the file to csv.reader
        next(reader, None)  # Skip the header row safely
        return [(row[WEBSIGHT_INDEX].strip().lower(), row[URL_INDEX].strip()) 
                for row in reader if len(row) > URL_INDEX and row[WEBSIGHT_INDEX].strip() and row[URL_INDEX].strip()] # go through each row and get the data in the first column
    
#! this function scrapes the data from the amazon website
#! i used chat gpt to figure out how to scrape data from amazon
def scrape_amazon_product(driver, url):
    driver.get(url)
    
    try:
        # Wait until the product title is present on the page
        title_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@id='productTitle']"))
        )
        title = title_element.text.strip() # strip the product title

        # Wait until the price element is present
        price_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='a-price-whole']"))
        )
        price_whole = price_element.text.strip() #strip the price from the website

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

#! this function writes the data to the csv file
def write_to_csv(data, file_path):
    file_exists = os.path.isfile(file_path)  # Check if the file already exists

    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        # Write header only if the file did not exist before
        if not file_exists:
            writer.writerow(["Website", "URL", "Product Name", "Price", "Date"])  # Write header
        writer.writerows(data)  # Write scraped data

#! this function scrapes all the products from the website
def scrape_all_products(driver, urls):
    scraped_data = []
    
    for website, url in urls:
        date = datetime.now().strftime("%Y-%m-%d")
        print(f"Scraping: {url} from {website}")
        
        try:
            if "amazon" in website:
                product_name, price = scrape_amazon_product(driver, url)
            else:
                print(f"Unknown website: {website}")
                product_name, price = None, None

            if product_name and price:
                scraped_data.append([website, url, product_name, price, date])

        except Exception as e:
            print(f"Error scraping {url}: {e}")

    driver.quit()  # Close the browser when done
    print('-------------------------------')
    print(scraped_data)
    print('-------------------------------')
    return scraped_data

#! this function that can be called into another file it does the same thing as the main function
def call_scraper():
    driver = setup_driver()
    urls = get_data_from_csv('user_data_request.csv')
    scraped_data = scrape_all_products(driver, urls)
    write_to_csv(scraped_data, 'scraped_data.csv')

#! this is the main function that calls the other functions and sets up the driver
def main():
    driver = setup_driver()
    urls = get_data_from_csv('user_data_request.csv')
    scraped_data = scrape_all_products(driver, urls)
    write_to_csv(scraped_data, 'scraped_data.csv')

if __name__ == "__main__":
    main()
