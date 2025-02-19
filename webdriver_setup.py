#python

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def setup_driver():
    # Set up Chrome options
    options = webdriver.ChromeOptions()
    
    # Use your actual Chrome profile to avoid CAPTCHA
    options.add_argument(r"--user-data-dir=C:\Users\Jeb Boone\AppData\Local\Google\Chrome\User Data\Default")
    options.add_argument("--profile-directory=Default")  # Change if using a different profile

    # Optional: Make Selenium look more like a real user
    options.add_argument("--disable-blink-features=AutomationControlled")  # Reduces bot detection
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    # Optional: Increase window size to avoid detection
    options.add_argument("start-maximized")
    
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

    # Keep YouTube open for 30 seconds
    time.sleep(30)  # Adjust the time (in seconds) as needed

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    main()
