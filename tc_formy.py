
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from datetime import datetime

def log(message):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")

driver = webdriver.Chrome()
driver.maximize_window()

try:
    start_time = datetime.now()
    log("Iniciando teste TC-005")
    
    driver.get("https://formy-project.herokuapp.com/form")
    
    driver.find_element(By.ID, "first-name").send_keys("João")
    driver.find_element(By.ID, "last-name").send_keys("Silva")
    driver.find_element(By.ID, "job-title").send_keys("Analista de Testes")
    
    driver.find_element(By.ID, "radio-button-1").click()
    driver.find_element(By.ID, "checkbox-1").click()
    
    Select(driver.find_element(By.ID, "select-menu")).select_by_visible_text("Brazil")
    
    driver.find_element(By.ID, "datepicker").send_keys("01/01/2025")
    
    driver.find_element(By.XPATH, "//a[text()='Submit']").click()
    
    time.sleep(2)
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
    log(f"Alerta de sucesso: {alert_text}")

    status = "Passou"
except Exception as e:
    log(f"Erro durante o teste: {e}")
    status = "Falhou"
finally:
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    log(f"Teste finalizado em {duration} segundos.")
    driver.quit()
