from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.reyab.com.br/")
driver.maximize_window()

clicar_link = WebDriverWait(driver, 10) #Aguarda até 10 segundos, se o link estiver disponivel para clicar

try:
    link = clicar_link.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Trabalhe Conosco")) #Procura o texto/link "Trabalhe conosco"
    )
    link.click() #Quando o elemento for encontrado retorna o clique na tela
    
    clicar_link.until(EC.url_contains("/trabalhe-conosco")) #Garante que a pagina tenha sido encontrada

except Exception as e:
    print(f"Erro: {e}")

time.sleep(8)
driver.quit()