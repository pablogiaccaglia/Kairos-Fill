# -*- coding: utf-8 -*-
from selenium.webdriver.support.select import Select
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def fillerUserData(aula, nome, mail, matricola, telefono, row, column):
    try:

        # collegamento con Chromium attraverso Selenium
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=chrome_options)
        time.sleep(5)
        driver.get("https://www.sbafirenze.it/tools/")
        time.sleep(5)

        # scelta della Biblioteca
        sel = Select(driver.find_element_by_xpath("//select[@name = 'location']"))
        time.sleep(5)
        sel.select_by_visible_text("Lettere")
        time.sleep(5)

        # scelta dell'aula/posto
        sel2 = Select(driver.find_element_by_xpath("//select[@name = 'service']"))
        time.sleep(5)
        sel2.select_by_visible_text(aula)
        time.sleep(5)

        # scelta della fascia oraria
        sel3 = Select(driver.find_element_by_xpath("//select[@name = 'worker']"))
        time.sleep(5)
        sel3.select_by_visible_text("Tutto il giorno")
        time.sleep(5)

        # scelta dela data dall'ui datepicker calendar, serve quando il giorno da prenotare è del mese successivo

        # next_button_name = "ui-datepicker-next"
        # time.sleep(2)
        # toclick = driver.find_element_by_class_name(next_button_name)
        # time.sleep(2)
        # toclick.click()
        # time.sleep(2)

        # scelta dela data dall'ui datepicker calendar
        table = driver.find_element_by_xpath(f"//table[@class='ui-datepicker-calendar']/tbody/tr[{row}]/td[{column}]")
        time.sleep(5)
        table.click()
        time.sleep(5)

        # click per selezionare un posto disponibile
        table2 = driver.find_element_by_xpath("//div[@class='time well well-lg']/a")
        time.sleep(5)
        table2.click()
        time.sleep(5)

        # xpath corrispondenti ai campi da riempire e ai box da selezionare (spunta gdpr e box "INVIA")
        clickMail = driver.find_element_by_xpath('//*[@id="post-335"]/div/div/div[2]/div/form/div[6]/div[2]/div/input')
        clickName = driver.find_element_by_xpath('//*[@id="post-335"]/div/div/div[2]/div/form/div[6]/div[3]/div/input')
        clickMatricola = driver.find_element_by_xpath(
            '//*[@id="post-335"]/div/div/div[2]/div/form/div[6]/div[4]/div/input')
        clickTelefono = driver.find_element_by_xpath(
            '//*[@id="post-335"]/div/div/div[2]/div/form/div[6]/div[5]/div/input')
        clickGdpr = driver.find_element_by_xpath(
            '//*[@id="ea-gdpr"]')
        clickConferma = driver.find_element_by_xpath(
            '//*[@id="post-335"]/div/div/div[2]/div/form/div[6]/div[9]/div/button[1]')
        time.sleep(5)

        # clear + autofill dei campi (clear con key_down(Keys.CONTROL).send_keys('a') )
        ActionChains(driver).move_to_element(clickMail).click().key_down(Keys.CONTROL).send_keys('a').key_up(
            Keys.CONTROL).send_keys(mail).perform()
        ActionChains(driver).move_to_element(clickName).click().key_down(Keys.CONTROL).send_keys('a').key_up(
            Keys.CONTROL).send_keys(nome).perform()
        ActionChains(driver).move_to_element(clickMatricola).click().key_down(Keys.CONTROL).send_keys('a').key_up(
            Keys.CONTROL).send_keys(matricola).perform()
        ActionChains(driver).move_to_element(clickTelefono).click().key_down(Keys.CONTROL).send_keys('a').key_up(
            Keys.CONTROL).send_keys(telefono).perform()
        time.sleep(4)

        # spunta gdpr + click box "INVIA"
        clickGdpr.click()
        time.sleep(5)
        clickConferma.click()
        time.sleep(5)
        driver.quit()

        print("Prenotato : " + nome)
    except:
        print("Errore di prenotazione :  " + nome)
        # fillerUserData(aula,nome, mail, matricola, telefono, row, column)
