# -*- coding: utf-8 -*-
# !/home/michaelfareshi/.virtualenvs/myvenv/bin/python3.8
from selenium.webdriver.support.select import Select
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def fillerUserData(biblioteca, aula, mese, giorno, nome, mail, matricola, telefono):
    full = False
    try:
        # collegamento con Chromium attraverso Selenium
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.sbafirenze.it/tools/")
        time.sleep(2)
        # scelta della Biblioteca
        sel = Select(driver.find_element_by_xpath("//select[@name = 'location']"))
        sel.select_by_visible_text(biblioteca)
        time.sleep(2)

        # scelta dell'aula/posto
        sel2 = Select(driver.find_element_by_xpath("//select[@name = 'service']"))
        sel2.select_by_visible_text(aula)
        time.sleep(2)

        # scelta della fascia oraria
        sel3 = Select(driver.find_element_by_xpath("//select[@name = 'worker']"))
        sel3.select_by_visible_text("Tutto il giorno")
        time.sleep(2)

        # scelta dela data dall'ui datepicker calendar
        mese = int(mese)
        # if mese==12:
        #    next_button_name= "ui-datepicker-next"
        #    toclick = driver.find_element_by_class_name(next_button_name)
        #    toclick.click()
        #    time.sleep(2)

        # scelta dela data dall'ui datepicker calendar
        table = driver.find_element_by_xpath(f"//table[@class='ui-datepicker-calendar']/tbody/tr[1]/td[1]")  #da correggere per selezionare la data corrente
        time.sleep(5)
        table.click()
        time.sleep(5)

        # click per selezionare un posto disponibile
        table2 = driver.find_element_by_xpath("//div[@class='time well well-lg']/a")

        table2.click()
        time.sleep(2)
        # xpath corrispondenti ai campi da riempire e ai box da selezionare (spunta gdpr e box "INVIA")
        clickMail = driver.find_element_by_xpath('//*[@id="post-335"]/div/div/div[3]/div/form/div[6]/div[2]/div/input')
        clickName = driver.find_element_by_xpath('//*[@id="post-335"]/div/div/div[3]/div/form/div[6]/div[3]/div/input')
        clickMatricola = driver.find_element_by_xpath(
            '//*[@id="post-335"]/div/div/div[3]/div/form/div[6]/div[4]/div/input')
        clickTelefono = driver.find_element_by_xpath(
            '//*[@id="post-335"]/div/div/div[3]/div/form/div[6]/div[5]/div/input')
        clickGdpr = driver.find_element_by_xpath(
            '//*[@id="ea-gdpr"]')  # xpath corrispondente alla locazione del tasto di accettazione del trattamento dei dati
        clickConferma = driver.find_element_by_xpath(
            '//*[@id="post-335"]/div/div/div[3]/div/form/div[6]/div[9]/div/button[1]')

        # clear + autofill dei campi (clear con key_down(Keys.CONTROL).send_keys('a') )
        ActionChains(driver).move_to_element(clickMail).click().key_down(Keys.CONTROL).send_keys('a').key_up(
            Keys.CONTROL).send_keys(mail).perform()
        ActionChains(driver).move_to_element(clickName).click().key_down(Keys.CONTROL).send_keys('a').key_up(
            Keys.CONTROL).send_keys(nome).perform()
        ActionChains(driver).move_to_element(clickMatricola).click().key_down(Keys.CONTROL).send_keys('a').key_up(
            Keys.CONTROL).send_keys(matricola).perform()
        ActionChains(driver).move_to_element(clickTelefono).click().key_down(Keys.CONTROL).send_keys('a').key_up(
            Keys.CONTROL).send_keys(telefono).perform()

        # spunta gdpr + click box "INVIA"
        clickGdpr.click()
        time.sleep(1)
        clickConferma.click()
        time.sleep(1)
        driver.quit()
        return full
    # eccezione sollevata quando la data scelta non è più selezionabile
    except:
        full = True
        return full

