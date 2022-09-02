'''
LETRA DEL EJERCICIO 2:

Parte 2 - Opcion 1:

Rrealizar un código en Python que realice:

A) un login en la web de RT (completando los campos de usuario y password) 
y realizando click en login. (por defecto usuario: root clave: password)
B) seleccionar la opción de crear un nuevo ticket (o caso).
C) ingresar al menos un valor en un campo del ticket
D) seleccionar la opción crear ticket.

Subir el código a un proyecto github de su preferencia.

Deberá especificar en el espacio para respuesta el link al mismo.
'''

import time
from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/opt/homebrew/Caskroom/chromedriver/104.0.5112.79/chromedriver")
# seteo la url
driver.get("http://localhost:8112/")

# busco el elemento por id y lo guardo en una variable elemento_user
elemento_user = driver.find_element(By.ID, "user")
elemento_user.clear()
elemento_user.send_keys("root")
# busco el elemento por xpath porque no tengo id y lo guardo en una variable elemento_pass
elemento_pass = driver.find_element(By.xpath, "//*[@id='login']/div[2]/div[2]/input")
elemento_pass.clear()
elemento_pass.send_keys("password")

driver.find_element(By.xpath, "//*[@id='login']/div[3]/div/input").click()
driver.get("http://localhost:8112")

time.sleep(20)

#B) seleccionar la opción de crear un nuevo ticket (o caso).
#C) ingresar al menos un valor en un campo del ticket
#D) seleccionar la opción crear ticket.


elemento_cr_ti = driver.find_element(By.xpath, "//*[@id='CreateTicketInQueue']/div[1]/input")
elemento_cr_ti.click()

elemento1 = driver.find_element(By.xpath, "//*[@id='TitleBox--_Ticket_Create_html--messagedetails----Q3JlYXRlIGEgbmV3IHRpY2tldCBpbiBHZW5lcmFs---0']/div/div/div[4]/div[2]/input")
elemento1.send_keys("esto es una prueba de carolina pereira")

elemento2 = driver.find_element(By.xpath, "//*[@id='SubmitTicket']/div[2]/input")
elemento2.click()

time.sleep(20)

driver.close()