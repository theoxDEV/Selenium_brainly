import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/drivers Selenium/chromedriver.exe')

# Buscando_Pergunta_Brainly
driver.get('https://brainly.com.br/')
time.sleep(3)
conteudo_Questao = driver.find_element_by_name('q')
conteudo_Questao.send_keys('Porque o sol é grande?' + Keys.ENTER)
time.sleep(3)

# Busca o link
pergunta_1 = driver.find_element_by_xpath("/html/\
body/div[3]/div[2]/div/div/div[1]/div/div[2]/div[1]/div[1]/a")
saved_link = pergunta_1.get_attribute('href')
pergunta_1.click()
time.sleep(2)

# Sair do POPuP de Login
x = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]')
x.click()

# Acessa a resposta
resposta_1 = driver.find_element_by_xpath('//*[@id="answers"]\
/div[3]/div/div[3]/div[1]/div/div/span')
string_Resposta_1 = resposta_1.text
print(string_Resposta_1)
