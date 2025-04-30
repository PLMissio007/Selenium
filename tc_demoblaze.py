
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
from datetime import datetime

def log(message):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")

driver = webdriver.Chrome()
driver.maximize_window()

try:
    start_time = datetime.now()
    log("Iniciando teste TC-004")
    
    driver.get("https://www.demoblaze.com/")
    driver.find_element(By.XPATH, "//a[text()='Phones']").click()
    driver.find_element(By.XPATH, "//a[text()='Samsung galaxy s6']").click()
    driver.find_element(By.XPATH, "//a[text()='Add to cart']").click()
    
    Alert(driver).accept()
    driver.find_element(By.XPATH, "//a[@id='cartur']").click()
    driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
    
    driver.find_element(By.ID, "name").send_keys("João Silva")
    driver.find_element(By.ID, "country").send_keys("Brasil")
    driver.find_element(By.ID, "city").send_keys("São Paulo")
    driver.find_element(By.ID, "card").send_keys("1234567812345678")
    driver.find_element(By.ID, "month").send_keys("12")
    driver.find_element(By.ID, "year").send_keys("2025")
    driver.find_element(By.XPATH, "//button[text()='Purchase']").click()
    
    modal_text = driver.find_element(By.XPATH, "//div[@class='sweet-alert']/h2").text
    log(f"Texto do modal: {modal_text}")

    status = "Passou"
except Exception as e:
    log(f"Erro durante o teste: {e}")
    status = "Falhou"
finally:
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    log(f"Teste finalizado em {duration} segundos.")
    driver.quit()
