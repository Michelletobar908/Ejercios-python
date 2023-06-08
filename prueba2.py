import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def main():
    # Ruta del WebDriver
    webdriver_path = r'C:\Users\pc\Desktop\selenium\chromedriver.exe'

    # Inicializar el WebDriver
    driver = webdriver.Chrome(executable_path=webdriver_path)
    driver.maximize_window()

    # Abrir la página del Banco de la República de Colombia
    driver.get('https://www.aulasuniminuto.edu.co/')
    # Esperar a que la página se cargue completamente
    time.sleep(5)

    boton_selector = '//*[@id="grid-cols-1"]/a'
    driver.find_element(By.XPATH, boton_selector).click()
    time.sleep(5)

    boton_3 = '//*[@id="region-main"]/div/div[2]/div/div/div/div/div/div[2]/div[3]/div/a'
    driver.find_element(By.XPATH, boton_3).click()
    time.sleep(5)

    campo_correo= driver.find_element(By.XPATH, '//*[@id="i0116"]')  # Cambiar 'campo_id' por el ID o selector adecuadro
    # Rellenar el campo con el texto deseado
    texto = 'ingresa aqui tu correo'
    campo_correo.send_keys(texto)

    boton_4 = '//*[@id="idSIButton9"]'
    driver.find_element(By.XPATH, boton_4).click()
    time.sleep(5)
    
    campo_contraseña = driver.find_element(By.XPATH, '//*[@id="i0118"]')  
    # Rellenar el campo con el texto deseado
    contraseña = 'ingresa aqui tu contraseña'
    campo_contraseña.send_keys(contraseña)
    time.sleep(10)
    
    boton_5 = '//*[@id="idSIButton9"]'
    element = driver.find_element(By.XPATH, boton_5).click()
    time.sleep(10)
    
    boton_6 = '//*[@id="uvd-course-1191"]/div[1]/div/div[2]/a'
    driver.find_element(By.XPATH, boton_6).click()
    time.sleep(10)

    descarga_excel = '//*[@id="module-403371"]/div/div/div[2]/div[1]/a/span'
    driver.find_element(By.XPATH, descarga_excel).click()
    time.sleep(10)

    # cerrar el webdrive
    driver.quit()
if __name__ == '__main__':
    main()
