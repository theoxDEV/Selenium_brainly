import time
from selenium import webdriver

# Declaração das variáveis GLOBAIS
login_kroton = ''
senha_kroton = ''
driver = ''
select_unidade = ''
Aba_Uniderp = ''
acessados = []


def Acessando_KROTON():
    global login_kroton
    login_kroton = '05738456114'
    # login_kroton = input("Informe seu login: ")
    global senha_kroton
    senha_kroton = '91188922'
    # senha_kroton = input("Informe sua senha: ")
    url_kroton = ('http://login.kroton.com.br/')
    global driver
    driver = webdriver.Chrome("C:/drivers Selenium/chromedriver.exe")
    driver.maximize_window()
    driver.get(url_kroton)
    global Aba_Uniderp
    Aba_Uniderp = driver.window_handles[0]
    time.sleep(5)


def Logando_KROTON():
    Acessando_KROTON()
    global select_unidade
    select_unidade = driver.find_element_by_id('unidade')
    for option in select_unidade.find_elements_by_tag_name('option'):
        if option.text != "Escolha a unidade...":
            option.click()
            break
        else:
            continue
    driver.find_element_by_name('username').send_keys(login_kroton)
    driver.find_element_by_name('password').send_keys(senha_kroton)
    driver.find_element_by_id('btnLogin').click()
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="x553bf8e5db1a2b009cb332ffaa9619c0"]\
        /li[8]/a').click()
    time.sleep(10)


def Selecionando_Disciplina():
    Logando_KROTON()
    Aba_Disciplina = driver.window_handles[1]
    driver.switch_to.window(Aba_Disciplina)
    time.sleep(7)
    tag_a = ''
    lista_elementos = []
    lista_elementos = driver.find_elements_by_class_name('card-wrap')
    class_action = driver.find_elements_by_class_name('card-action')
    DNotaMaxima = 'https://www.avaeduc.com.br/course/view.php?id=6961'
    # desafionotamaxima = 'https://www.avaeduc.com.br/course/view.php?id=6961'
    # ABRINDO TODAS AS DISCIPLINAS
    for i in lista_elementos:
        for a in class_action:
            if tag_a not in acessados:
                tag_a = a.find_element_by_tag_name('a').get_attribute('href')
                if tag_a != DNotaMaxima:
                    driver.execute_script(f"window.open('{tag_a}', '_blank')")
                    acessados.append(tag_a)
                else:
                    continue


Selecionando_Disciplina()
