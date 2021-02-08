import os
import time
import wget
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

if __name__ = "__main__":
	#Iniciamos Selenium con el navegador Google Chrome
	driver = webdriver.Chrome()

	#Abrimos el editor de Paint Online
	driver.get("http://paintonline.editaraudio.com/")
	driver.maximize_window()
	driver.switch_to.frame(0)

	#Importamos la imagen base de Xavier Hervas (Imagen previamente descarga)
	driver.find_element(By.ID, "main_menu_0_0").click()
	driver.find_element(By.ID, "main_menu_1_2").click()
	driver.find_element(By.ID, "main_menu_2_0").click()
	driver.find_element(By.ID, "file_open").send_keys("/home/wilson/Documentos/Simulacion/ExamenFinal/XavierHervas.jpg")

	#Dibujamos algo sobre el lienzo del dibujo (Un visto bueno en este caso)
	driver.find_element(By.ID, "pencil").click()
	driver.find_element(By.CSS_SELECTOR, "#size > button.increase_number").click()
	driver.find_element(By.CSS_SELECTOR, "#size > button.increase_number").click()
	driver.find_element(By.CSS_SELECTOR, "#size > button.increase_number").click()
	driver.find_element(By.CSS_SELECTOR, "#size > button.increase_number").click()
	element = driver.find_element(By.ID, "canvas_minipaint")

	x = 250
	y = 50

	actions = ActionChains(driver)
	actions.move_to_element_with_offset(element, x, y).perform()
	actions.click_and_hold().perform()

	while y < 75:
    	actions.move_to_element_with_offset(element, x, y)
    	x += 3
    	y += 3

	while y > 30:
    		actions.move_to_element_with_offset(element, x, y)
    		x += 3
     	y -= 3

	actions.release().perform()

	#Descargamos el flyer creado a la carpeta de descargas
	driver.find_element(By.ID, "canvas_minipaint").click()
	driver.find_element(By.ID, "main_menu_0_0").click()
	driver.find_element(By.ID, "main_menu_1_5").click()
	driver.find_element(By.ID, "pop_data_name").click()
	driver.find_element(By.ID, "pop_data_name").send_keys("Flyer")
	driver.find_element(By.ID, "popup_ok").click()

	time.sleep(5)
	driver.quit()
	
	#Iniciamos Selenium con el navegador Google Chrome
	chrome_options = webdriver.ChromeOptions()
	prefs = {"profile.default_content_setting_values.notifications" : 2}
	chrome_options.add_experimental_option("prefs", prefs)
	driver = webdriver.Chrome(options = chrome_options)

	#Iniciamos sesión en la cuenta de Facebook
	driver.get("https://www.facebook.com/")
	driver.maximize_window()
	driver.find_element(By.ID, "email").click()
	driver.find_element(By.ID, "email").send_keys("example@mail.com") #Reemplazar por datos personales
	driver.find_element(By.ID, "pass").click()
	driver.find_element(By.ID, "pass").send_keys("***********") #Reemplazar por datos personales
	driver.find_element(By.ID, "u_0_b").click()

	#Creamos una nueva publicación
	time.sleep(5)
	WebDriverWait(driver, 10).until(
    		EC.presence_of_element_located((
        		By.XPATH, 
        		"//*[@id='mount_0_0']/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div"
	))).click()

	#Subimos el flyer creado de Xavier Hervas
	time.sleep(5)
	WebDriverWait(driver, 10).until(
    		EC.presence_of_element_located((
        		By.XPATH, 
        		"//*[@id='mount_0_0']/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[1]/div[2]/div/div[1]/input"
	))).send_keys("/home/wilson/Descargas/XavierHervasFlyer.png")

	#Asignamos un comentario
	time.sleep(5)
	WebDriverWait(driver, 10).until(
    		EC.presence_of_element_located((
        		By.XPATH, 
        		"//*[@id='mount_0_0']/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div"
	))).send_keys("Flyer subido mediante Selenium (Simulación)")

	#Publicamos el contenido
	time.sleep(5)
	WebDriverWait(driver, 10).until(
    		EC.presence_of_element_located((
        		By.XPATH, 
        		"//*[@id='mount_0_0']/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[2]/div"
	))).click()

	#Cerramos sesión
	time.sleep(5)
	WebDriverWait(driver, 10).until(
    		EC.presence_of_element_located((
        		By.XPATH, 
        		"//*[@id='mount_0_0']/div/div[1]/div/div[2]/div[4]/div[1]/span/div/div[1]"
	))).click()

	time.sleep(5)
	WebDriverWait(driver, 10).until(
    		EC.presence_of_element_located((
        		By.XPATH, 
        		"//*[@id='mount_0_0']/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div[4]/div"
	))).click()

	time.sleep(5)
	driver.quit()
	
	#Iniciamos Selenium con el navegador Google Chrome
	driver = webdriver.Chrome()

	#Abrimos la vista de descarga de archivo compartido
	driver.get(url = "https://drive.google.com/file/d/1eQPzLAt1DWxqiILPj9V8uzGHR0ecWdY3/view")
	driver.maximize_window()

	time.sleep(5)
	actions = ActionChains(driver)
	element = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div[3]/div[2]/div[2]/div[3]")
	actions.move_to_element(element).click().perform()

	time.sleep(5)
	driver.quit()

	datos = pd.read_csv("/home/wilson/Descargas/DatosExamen.csv")
	
	#Iniciamos Selenium con el navegador Google Chrome
	driver = webdriver.Chrome()

	#Iniciamos sesión en Hotmail/Outlook
	driver.get("https://outlook.live.com/owa/")
	driver.maximize_window()
	driver.find_element(By.XPATH, "/html/body/header/div/aside/div/nav/ul/li[2]/a").click()

	time.sleep(5)
	driver.find_element(By.ID, "i0116").click()
	driver.find_element(By.ID, "i0116").send_keys("example@mail.com") #Reemplazar por datos personales
	driver.find_element(By.ID, "idSIButton9").click()

	time.sleep(5)
	driver.find_element(By.ID, "i0118").click()
	driver.find_element(By.ID, "i0118").send_keys("**********") #Reemplazar por datos personales
	driver.find_element(By.ID, "idSIButton9").click()

	#Enviamos el flyer a todos los correos del archivo
	for correo in datos["Correo"]:
    		#Creamos un mensaje nuevo
    		time.sleep(5)
    		WebDriverWait(driver, 10).until(
        		EC.presence_of_element_located((
            		By.XPATH, 
            		"//*[@id='app']/div/div[2]/div[1]/div[1]/div/div/div[1]/div[1]/div[2]/button"
    		))).click()

    		#Establecemos el asunto
    		time.sleep(10)
    		element = WebDriverWait(driver, 10).until(
        		EC.presence_of_element_located((
            		By.XPATH, 
    		        	"//*[starts-with(@id, 'TextField')]"     
    		)))
    		element.send_keys("Flyer del candidato Xavier Hervas con Selenium (Simulacion)")

    		#Establecemos el destinatario
    		time.sleep(5)
    		element = WebDriverWait(driver, 10).until(
        		EC.presence_of_element_located((
            		By.XPATH, 
            		"//*[@id='ReadingPaneContainerId']/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/div/div/div/div[1]/div/div/input"
    		)))
    		element.send_keys(correo)

	    	#Seleccionamos el area de contenido del correo
    		time.sleep(5)
    		WebDriverWait(driver, 10).until(
        		EC.presence_of_element_located((
            		By.XPATH, 
            		"//*[@id='ReadingPaneContainerId']/div/div/div/div[1]/div[2]/div[1]"
    		))).click()

    		#Adjuntamos el flyer de Xavier Hervas
    		time.sleep(5)
    		WebDriverWait(driver, 10).until(
        		EC.presence_of_element_located((
            		By.CSS_SELECTOR, 
            		"#ReadingPaneContainerId > div > div > div > div._29NreFcQ3QoBPNO3rKXKB0 > div._1vGTUqFfb2m4yyZJJPHFDg._1PGX4GmfSf_CaaQSnoiB4l > input:nth-child(4)"
    		))).send_keys("/home/wilson/Descargas/XavierHervasFlyer.png")

    		#Damos click en el boton enviar
    		time.sleep(5)
    		WebDriverWait(driver, 10).until(
        		EC.presence_of_element_located((
            		By.XPATH, 
            		"//*[@id='ReadingPaneContainerId']/div/div/div/div[1]/div[3]/div[2]/div[1]/div/span/button[1]"
    		))).click()
    	
    	#Cerramos sesión
	time.sleep(5)
	WebDriverWait(driver, 10).until(
    		EC.presence_of_element_located((
        		By.XPATH, 
        		"//*[@id='O365_MainLink_Me']"
	))).click()

	time.sleep(5)
	WebDriverWait(driver, 10).until(
    		EC.presence_of_element_located((
        		By.XPATH, 
        		"//*[@id='mectrl_body_signOut']"
	))).click()

	time.sleep(5)
	driver.quit()
	
	#Iniciamos Selenium con el navegador Google Chrome
	chrome_options = webdriver.ChromeOptions()
	prefs = {"profile.default_content_setting_values.notifications" : 2}
	chrome_options.add_experimental_option("prefs", prefs)
	driver = webdriver.Chrome(options = chrome_options)

	#Iniciamos sesión en la cuenta de Facebook
	driver.get("https://www.facebook.com/")
	driver.maximize_window()
	driver.find_element(By.ID, "email").click()
	driver.find_element(By.ID, "email").send_keys("example@mail.com")
	driver.find_element(By.ID, "pass").click()
	driver.find_element(By.ID, "pass").send_keys("******")
	driver.find_element(By.ID, "u_0_b").click()

	#Ingresamos a la publicación del Flyer
	time.sleep(5)
	driver.get("https://www.facebook.com/photo/?fbid=1847535578735935&set=a.105895986233245")

	#Iniciamos la recoleccion de datos (Comentarios en este caso)
	comentarios = []

	time.sleep(5)
	lista_comentarios = driver.find_elements(
    		By.XPATH, 
    		"//div[@style='text-align: start;']"
	)

	lista_usuarios = driver.find_elements(
    		By.XPATH, 
    		"//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8']"
	)

	for usuario, comentario in zip(lista_usuarios, lista_comentarios):
	    comentarios.append({"usuario": usuario.text, "comentario": comentario.text})
    
	#Cerramos sesión
	driver.get("https://www.facebook.com/")

	time.sleep(5)
	WebDriverWait(driver, 10).until(
    		EC.presence_of_element_located((
        		By.XPATH, 
        		"//*[@id='mount_0_0']/div/div[1]/div/div[2]/div[4]/div[1]/span/div/div[1]"
	))).click()

	time.sleep(5)
	WebDriverWait(driver, 10).until(
    		EC.presence_of_element_located((
        		By.XPATH, 
        		"//*[@id='mount_0_0']/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div[4]/div"
	))).click()

	time.sleep(5)
	driver.quit()

	informe = open("/home/wilson/Documentos/Simulacion/ExamenFinal/ComentariosFlyer.csv", "w")
	escritor = csv.DictWriter(informe, fieldnames = ["usuario","comentario"])
	escritor.writeheader()
	escritor.writerows(comentarios)
