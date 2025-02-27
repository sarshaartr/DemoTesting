from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
chrome_options.add_argument("--no-sandbox")  # Required for running in CI/CD environments
chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent shared memory issues
chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
chrome_options.add_argument("--remote-debugging-port=9222")  # Debugging port
chrome_options.add_argument("--user-data-dir=/tmp/chrome-data")  # Use a unique directory

# Initialize WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open a webpage
driver.get("https://www.google.com")
print(driver.title)

# Close the browser
driver.quit()
