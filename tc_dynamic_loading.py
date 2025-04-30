
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

def log(message):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")


driver = webdriver.Chrome()
driver.maximize_window()


try:
    start_time = datetime.now()
    log("Iniciando teste TC-003")
    
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    driver.find_element(By.XPATH, "//button[text()='Start']").click()
    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h4[text()='Hello World!']"))
    )
    log("Texto 'Hello World!' visível.")

    status = "Passou"
except Exception as e:
    log(f"Erro durante o teste: {e}")
    status = "Falhou"
finally:
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    log(f"Teste finalizado em {duration} segundos.")
    driver.quit()
