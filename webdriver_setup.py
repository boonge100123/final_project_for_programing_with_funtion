import subprocess
import sys
import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#! this function installs the packages that are needed for the program to run if they are not already installed
#! like the pip install funtion in the terminal
def install_packages():
    packages = [
        "selenium",
        "webdriver-manager",
        "pandas",
        "matplotlib"
    ]
    
    for package in packages:
        try:
            __import__(package)  # Try to import the package
        except ImportError:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

#! this function sets up the driver for the chrome browser
#! the chrome browser is used to let python interact with the web browser it will onaly work with chrome
def setup_driver():
    """Sets up and returns a Chrome WebDriver instance with user profile support."""
    # Set up Chrome options
    options = webdriver.ChromeOptions()
    
    # Use your actual Chrome profile to avoid CAPTCHA
    chrome_user_data_path = get_chrome_user_data_dir()
    options.add_argument(f"--user-data-dir={chrome_user_data_path}")
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

#! this function gets the chrome user data directory so that he user can use their own chrome profile
def get_chrome_user_data_dir():
    """Returns the default Chrome user data directory based on the OS."""
    if sys.platform == "win32":
        return os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data")
    elif sys.platform == "darwin":
        return os.path.expanduser("~/Library/Application Support/Google/Chrome")
    elif sys.platform.startswith("linux"):
        return os.path.expanduser("~/.config/google-chrome")
    else:
        raise RuntimeError("Unsupported operating system")

#! this is the main function that test runs the program to make sure that the webdriver is working
def main():
    """Main function to set up the environment and test WebDriver."""
    install_packages()  # Install necessary packages
    driver = setup_driver()  # Set up the WebDriver
    
    # Open YouTube
    driver.get("https://www.youtube.com/watch?v=xvFZjo5PgG0")
    play_button = driver.find_element(By.CSS_SELECTOR, "button.ytp-large-play-button.ytp-button")
    play_button.click()
    
    # Print the title of the page
    print(driver.title)
    
    # Keep YouTube open for 30 seconds
    time.sleep(30)
    
    # Close the browser
    driver.quit()

if __name__ == "__main__":
    main()
