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
	correo = "example@mail.com"
	clave = "******"
	
	#Iniciamos Selenium con el navegador Google Chrome
	chrome_options = webdriver.ChromeOptions()
	prefs = {"profile.default_content_setting_values.notifications" : 2}
	chrome_options.add_experimental_option("prefs", prefs)
	driver = webdriver.Chrome(options = chrome_options)

	#Iniciamos sesión en la cuenta de Facebook
	driver.get("https://www.facebook.com/")
	driver.maximize_window()
	driver.find_element(By.ID, "email").click()
	driver.find_element(By.ID, "email").send_keys(correo)
	driver.find_element(By.ID, "pass").click()
	driver.find_element(By.ID, "pass").send_keys(clave)
	driver.find_element(By.ID, "u_0_b").click()

	#Creamos una nueva publicación
	time.sleep(5)
	WebDriverWait(driver, 10).until(
	    EC.presence_of_element_located((
	        By.XPATH, 
	        "//*[@id='mount_0_0']/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div"
	))).click()
	
	#Asignamos un comentario
	time.sleep(5)
	WebDriverWait(driver, 10).until(
	    EC.presence_of_element_located((
	        By.XPATH, 
	        "//*[@id='mount_0_0']/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div"
	))).send_keys("Publicación simple realizada mediante Selenium")

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
	chrome_options = webdriver.ChromeOptions()
	prefs = {"profile.default_content_setting_values.notifications" : 2}
	chrome_options.add_experimental_option("prefs", prefs)
	driver = webdriver.Chrome(options = chrome_options)

	#Iniciamos sesión en la cuenta de Facebook
	driver.get("https://www.facebook.com/")
	driver.maximize_window()
	driver.find_element(By.ID, "email").click()
	driver.find_element(By.ID, "email").send_keys(correo)
	driver.find_element(By.ID, "pass").click()
	driver.find_element(By.ID, "pass").send_keys(clave)
	driver.find_element(By.ID, "u_0_b").click()

	#Damos "Me gusta" a la primera publicación en la página principal
	time.sleep(5)
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

	time.sleep(5)
	publicaciones = driver.find_elements(By.XPATH, "//*[@aria-label='Me gusta']")
	publicaciones[0].click()

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
	
	
	#Definimos el correo electrónico destino
	correo_destino = "b.xavi@hotmail.es"

	#Iniciamos Selenium con el navegador Google Chrome
	driver = webdriver.Chrome()

	#Iniciamos sesión en Hotmail/Outlook
	driver.get("https://outlook.live.com/owa/")
	driver.maximize_window()
	driver.find_element(By.XPATH, "/html/body/header/div/aside/div/nav/ul/li[2]/a").click()

	time.sleep(5)
	driver.find_element(By.ID, "i0116").click()
	driver.find_element(By.ID, "i0116").send_keys(correo)
	driver.find_element(By.ID, "idSIButton9").click()

	time.sleep(5)
	driver.find_element(By.ID, "i0118").click()
	driver.find_element(By.ID, "i0118").send_keys(clave)
	driver.find_element(By.ID, "idSIButton9").click()

	#Creamos un mensaje nuevo
	time.sleep(5)
	WebDriverWait(driver, 10).until(
    		EC.presence_of_element_located((
    		     By.XPATH, 
        		"//*[@id='app']/div/div[2]/div[1]/div[1]/div/div/div[1]/div[1]/div[2]/button"
	))).click()

	#Establecemos el destinatario
	time.sleep(5)
	element = WebDriverWait(driver, 10).until(
    		EC.presence_of_element_located((
        		By.XPATH, 
        		"//*[@id='ReadingPaneContainerId']/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/div/div/div/div[1]/div/div/input"
	)))
	element.send_keys(correo)

	#Establecemos el asunto
	time.sleep(10)
	element = WebDriverWait(driver, 10).until(
    		EC.presence_of_element_located((
        		By.XPATH, 
        		"//*[starts-with(@id, 'TextField')]"     
	)))
	element.send_keys("Correo automatizado con Selenium")

	#Seleccionamos el area de contenido del correo
	time.sleep(5)
	WebDriverWait(driver, 10).until(
	    EC.presence_of_element_located((
	        By.XPATH, 
	        "//*[@id='ReadingPaneContainerId']/div/div/div/div[1]/div[2]/div[1]"
	))).click()

	#Escribimos nuestro mensaje
	time.sleep(5)
	WebDriverWait(driver, 10).until(
	    EC.presence_of_element_located((
	        By.XPATH, 
	        "//*[@id='ReadingPaneContainerId']/div/div/div/div[1]/div[2]/div[1]"
	))).send_keys(
	"""
	Hola estimado, este es un correo electrónico de ejemplo enviado con Selenium
	para el proyecto integrador final de la asignatura de Simulación. Puedes
	ignorarlo o eliminarlo si deseas.
	    
	Saludos, 
	Wilson.
	"""
	)

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
	
	
	#Definimos la ruta de nuestro documento
	documento = "C:\\Users\\Carlos\\Documents\DocumentoPrueba.docx"

	#Iniciamos Selenium con el navegador Google Chrome
	driver = webdriver.Chrome()

	#Ingresamos a nuestro conversor en línea
	driver.get("https://smallpdf.com/es/word-a-pdf")
	driver.maximize_window()

	#Subimos el documento a convertir
	driver.find_element(By.ID, "__picker-input").send_keys(documento)

	#Descargamos el documento PDF
	time.sleep(10)
	WebDriverWait(driver, 10).until(
    		EC.presence_of_element_located((
        		By.XPATH, 
        		"//button[@class='l3tlg0-0 eqlXyA']"
	))).click()

	time.sleep(5)
	driver.quit()
	
	
	#Iniciamos Selenium con el navegador Google Chrome
	driver = webdriver.Chrome()

	#Ingresamos a nuestro servicio TTS
	driver.get("https://www.ispeech.org/text.to.speech")
	driver.maximize_window()

	time.sleep(5)
	driver.execute_script("window.scrollTo(0, 50)")

	#Escribimos el texto a convertir
	time.sleep(5)
	WebDriverWait(driver, 10).until(
	    EC.presence_of_element_located((
	        By.XPATH, 
	        "//*[@id='demo']/div/div/div/div/div/div[2]/div[2]/div[1]/textarea"
	))).click()

	time.sleep(5)
	WebDriverWait(driver, 10).until(
	    EC.presence_of_element_located((
	        By.XPATH, 
	        "//*[@id='demo']/div/div/div/div/div/div[2]/div[2]/div[1]/textarea"
	))).clear()

	WebDriverWait(driver, 10).until(
	    EC.presence_of_element_located((
	        By.XPATH, 
	        "//*[@id='demo']/div/div/div/div/div/div[2]/div[2]/div[1]/textarea"
	))).send_keys(
	"""
	Hello, this is an example of Text to Speech
	using Selenium for it. Thanks.
	"""
	)

	#Damos click en 'Reproducir' y escuchamos el resultado
	driver.find_element(By.CLASS_NAME, "play-control-text").click()

	time.sleep(15)
	driver.quit()
	
	
	#Definimos la ruta de nuestra imagen
	imagen = "/home/wilson/Documentos/Simulacion/TrabajoFinal/Imagen-gato.jpg"

	#Iniciamos Selenium con el navegador Google Chrome
	driver = webdriver.Chrome()

	#Ingresamos al buscador por imágenes de Google
	driver.get("https://images.google.com/?gws_rd=ssl")
	driver.maximize_window()

	#Subimos la imagen con la cual queremos buscar
	time.sleep(5)
	driver.find_element(By.XPATH, "//*[@aria-label='Buscar por imágenes']").click()

	time.sleep(5)
	driver.find_element(By.XPATH, "//*[@class='iOGqzf H4qWMc aXIg1b']").click()

	time.sleep(5)
	driver.find_element(By.XPATH, "//*[@id='awyMjb']").send_keys(imagen)

	#Obtenemos el resultado de la busqueda
	time.sleep(5)
	element = driver.find_element(By.XPATH, "//*[@id='sbtc']/div[2]/div[2]/input")

	print('Busqueda de Google:', element.get_attribute("value"))

	time.sleep(5)
	driver.quit()
	
	
	#Definimos las credenciales
	correo = "estudiante@est.ups.edu.ec"
	clave = "*******"

	#Iniciamos Selenium con el navegador Google Chrome
	driver = webdriver.Chrome()

	#1. Ingresamos a la página de la Universidad Politécnica Salesiana
	driver.get("https://www.ups.edu.ec/")
	driver.maximize_window()

	#2. Ingresamos a nuestra cuenta personal
	time.sleep(5)
	driver.find_element(By.XPATH , "//*[@id='accesosCQI']/ul/li[3]/a").click()

	time.sleep(5)
	driver.find_element(By.XPATH , "//*[@id='username']").send_keys(correo)
	driver.find_element(By.XPATH , "//*[@id='password']").send_keys(clave)
	driver.find_element(By.XPATH , "//*[@id='login']/div[4]/center/input").click()

	#3. Accedemos al sistema de solicitudes
	time.sleep(5)
	driver.find_element(By.XPATH , "//*[@id='estSoli']").click()

	#4. Accedemos al detalle de la primera solicitud
	time.sleep(5)
	driver.execute_script("window.scrollTo(0, 100)")
	driver.find_element(
	    By.XPATH , 
	    "//*[@id='_upsportalestudiantesolicitudv1_WAR_upsportalestudiantesolicitudv1portlet_:formPrincipal:j_idt28_data']/tr[1]/td[6]/table/tbody/tr/td[3]/input"
	).click()

	#5. Descargamos una copia de la solicitud
	time.sleep(5)
	driver.execute_script("window.scrollTo(0, 100)")
	driver.find_element(
	    By.XPATH , 
	    "//*[@id='_upsportalestudiantesolicitudv1_WAR_upsportalestudiantesolicitudv1portlet_:formPrincipal:plantillaForm']/div[5]/a"
	).click()

	#6. Cerramos sesión
	time.sleep(5)
	driver.execute_script("window.scrollTo(0, 100)")
	driver.find_element(
	    By.XPATH , 
	    "//*[@id='accesosCQI']/ul/li[3]/a"
	).click()

	time.sleep(5)
	driver.quit()
	
	
	#Definimos las credenciales
	correo = "estudiantep@est.ups.edu.ec"
	clave = "******"

	#Iniciamos Selenium con el navegador Google Chrome
	driver = webdriver.Chrome()

	#1. Ingresamos al AVAC del periodo 47
	driver.get("http://avac.ups.edu.ec/presencial57")
	driver.maximize_window()

	#2. Iniciamos sesión
	time.sleep(5)
	driver.find_element(By.XPATH, "//*[@id='card-block-ups']/div/div/div[1]/div/div/a").click()

	time.sleep(5)
	driver.find_element(By.XPATH, "//*[@id='i0116']").send_keys(correo)
	driver.find_element(By.XPATH, "//*[@value='Siguiente']").click()

	time.sleep(5)
	driver.find_element(By.XPATH, "//*[@id='i0118']").send_keys(clave)
	driver.find_element(By.XPATH, "//*[@value='Iniciar sesión']").click()

	time.sleep(5)
	driver.find_element(By.XPATH, "//input[@value='No']").click()

	#3. Ingresamos a la asignatura de Simulación
	time.sleep(5)
	driver.get("https://avac.ups.edu.ec/presencial57/course/view.php?id=49")

	#4. Ingresamos a la unidad de RPA
	time.sleep(5)
	driver.find_element(By.XPATH, "//*[@id='chapters']/li[5]/a").click()

	#5. Descargamos las diapositivas
	time.sleep(5)
	driver.execute_script("window.scrollTo(0, 200)")
	driver.find_element(By.XPATH, "//*[@id='module-243573']/div/div/div[2]/div/a").click()

	#6. Cerramos sesión
	time.sleep(5)
	driver.find_element(By.XPATH, "//div[@class='usermenu nav-item dropdown user-menu login-menu']/a").click()

	time.sleep(5)
	driver.find_element(By.XPATH, "//div[@class='dropdown-menu dropdown-menu-right show']/a[6]").click()

	time.sleep(5)
	driver.quit()
