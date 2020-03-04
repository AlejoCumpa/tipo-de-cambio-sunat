from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd
import json

chromedriver_path = 'C:/Program Files/Chromedriver/chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
switcher = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Setiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}

sleep(2)
webdriver.get('https://e-consulta.sunat.gob.pe/cl-at-ittipcam/tcS01Alias')
sleep(3)

for anhoFecha in range(1995 , 2020):
    arrayTC = []

    for i in range(1 , 13):
        
        while True:
            try:
                mesTexto = switcher[i]
                mes = webdriver.find_element_by_name('mes')
                mes.send_keys(mesTexto)
                anho = webdriver.find_element_by_name('anho')
                anho.send_keys(str(anhoFecha))
                sleep(1)
                boton = webdriver.find_element_by_name('B1')
                boton.click()
                sleep(2)

                fecha = 0
                compra = 0
                venta = 0

                tabla = webdriver.find_element_by_css_selector("body > form > div:nth-child(4) > center > table > tbody")
                tableRows = tabla.find_elements_by_tag_name("tr")
                iterRows = iter(tableRows)
                next(iterRows)
                for fila in iterRows:    
                    celdas = fila.find_elements_by_tag_name("td")
                    for j in range(len(celdas)):
                        if j%3 == 0 :
                            fecha = str(anhoFecha) + '-' + str(i).zfill(2) + '-' + str(celdas[j].text).zfill(2)
                        elif j % 3 == 1:
                            compra = celdas[j].text
                        elif j% 3 == 2:
                            venta = celdas[j].text
                            arrayTC.append({ "fecha": fecha,"compra":compra,"venta": venta })                
                            fecha = 0
                            compra = 0
                            venta = 0
                break
            except:
                botonAnterior = webdriver.find_elements_by_class_name("button")[0].click()
    with open("tc-sunat-" + str(anhoFecha)+ ".json", 'w') as f:
        json.dump(arrayTC, f)

