import subprocess
import sys
import os
from webdriver_manager.chrome import ChromeDriverManager

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

def install_chrome_driver():
    """Install ChromeDriver using webdriver-manager."""
    print("Installing ChromeDriver...")
    ChromeDriverManager().install()

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

if __name__ == "__main__":
    install_packages()
    install_chrome_driver()
    chrome_user_data_dir = get_chrome_user_data_dir()
    print(f"Chrome user data directory: {chrome_user_data_dir}")
