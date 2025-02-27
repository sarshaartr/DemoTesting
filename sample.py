import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://demoqa.com/text-box")

driver.maximize_window()
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