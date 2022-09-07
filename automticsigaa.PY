from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\Users\ericl\OneDrive\Área de Trabalho\python\chromedriver.exe")
driver.get('https://si3.ufc.br/sigaa/verTelaLogin.do%3bjsessionid=ADFBEA8217180207398081ADEBB404F2.node22')
driver.maximize_window()

elem = driver.find_element("name","user.login").send_keys("usuario")
elem = driver.find_element("name","user.senha").send_keys("senha")

driver.find_element('xpath', '/html/body/div[2]/main/table/tbody/tr/td/div/form/table/tfoot/tr/td/input').click()
driver.get('https://si3.ufc.br/sigaa/verPortalDiscente.do')

driver.find_element('xpath', '/html/body/div[4]/main/div/div[4]/div[2]/table/tbody/tr[5]/td[1]/form').click()
