import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options for GitHub Actions
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
chrome_options.add_argument("--no-sandbox")  # Required for CI/CD environments
chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent shared memory issues
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
chrome_options.add_argument("--window-size=1920x1080")  # Set window size
chrome_options.add_argument("--remote-debugging-port=9222")  # Debugging port

# Initialize WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the webpage
driver.get("https://demoqa.com/text-box")

time.sleep(2)  # Wait for page to load

# Fill out the form
driver.find_element(By.ID, "userName").send_keys("Sarshaar")
driver.find_element(By.ID, "userEmail").send_keys("sarshaartr@gmail.com")
driver.find_element(By.ID, "currentAddress").send_keys("Johar")
driver.find_element(By.ID, "permanentAddress").send_keys("Mention above")

time.sleep(1)

# Click the submit button
submit_button = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].click();", submit_button)

time.sleep(5)

# Get output text
output_text = driver.find_element(By.ID, "output").text
print("\nSubmitted Data:\n", output_text)

# Close browser
driver.quit()
