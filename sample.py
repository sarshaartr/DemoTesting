import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options for GitHub Actions
chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--no-sandbox")  
chrome_options.add_argument("--disable-dev-shm-usage")  
chrome_options.add_argument("--disable-gpu")  
chrome_options.add_argument("--window-size=1920x1080")  
chrome_options.add_argument("--remote-debugging-port=9222")  


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


driver.get("https://demoqa.com/text-box")

time.sleep(2)  


driver.find_element(By.ID, "userName").send_keys("Sarshaar")
driver.find_element(By.ID, "userEmail").send_keys("sarshaartr@gmail.com")
driver.find_element(By.ID, "currentAddress").send_keys("Johar")
driver.find_element(By.ID, "permanentAddress").send_keys("Mention above")

time.sleep(1)


submit_button = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].click();", submit_button)

time.sleep(5)


output_text = driver.find_element(By.ID, "output").text
print("\nSubmitted Data:\n", output_text)


driver.quit()
