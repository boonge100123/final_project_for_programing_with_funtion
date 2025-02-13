#python

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def setup_driver():
    # Set up Chrome options
    options = webdriver.ChromeOptions()
    
    # Run in headless mode (optional)
    # options.add_argument('--headless')
    
    # Disable GPU hardware acceleration (optional)
    # options.add_argument('--disable-gpu')
    
    # Set a custom window size (optional)
    # options.add_argument('window-size=1200x600')
    
    # Disable extensions (optional)
    options.add_argument('--disable-extensions')
    
    # Ignore certificate errors (optional)
    options.add_argument('--ignore-certificate-errors')
    
    # Set up ChromeDriver using WebDriver Manager and Service
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    return driver

def main():
    # Initialize the WebDriver
    driver = setup_driver()

    # Open YouTube
    driver.get("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    # Print the title of the page
    print(driver.title)

    # Keep YouTube open for 10 seconds
    time.sleep(30)  # Adjust the time (in seconds) as needed

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    main()
