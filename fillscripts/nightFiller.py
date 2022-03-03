import os
import re

from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import logging
from fake_useragent import UserAgent
from database.users_database import UsersDatabase

class KairosBot:

    def __init__(self):

        self.driverPath = os.environ.get("CHROMEDRIVER_PATH")

        self.chrome_options = self.__configChromeOptions()
        self.driver = webdriver.Chrome(executable_path = os.environ.get("CHROMEDRIVER_PATH"),
                                       chrome_options = self.chrome_options)

        self.SINGLE_BOOK = "SINGLE_BOOK"
        self.DOUBLE_BOOK = "DOUBLE_BOOK"
        self.OPTION_1 = "Posto studio in biblioteca [MATTINA]"
        self.OPTION_2 = "Posto studio in biblioteca [POMERIGGIO]"
        self.MAX_RETRIES = 2
        self.MAX_WAITING_TIME = 40
        self.LOGIN_URL = "https://kairos.unifi.it/portalePlanning/BIBL/login.php"
        self.BOOKING_URL = "https://kairos.unifi.it/portalePlanning/BIBL/index.php?include=form"

        self.completed = False

    def __resetBot(self):
        if not str(self.driver).__contains__("null"):
            self.driver.quit()
        self.__init__()

    def start(self, bookingType):
        print("ciaoooo")
        users = UsersDatabase.get_users()

        if bookingType == self.SINGLE_BOOK:
            for user in users:
                logging.info(user['student_id'] + " " + user['user_pw'] + " " + user['hall'])
                self.__singleBook(self.OPTION_1, user)

        elif bookingType == self.DOUBLE_BOOK:
            for user in users:
                logging.info(user['student_id'] + " " + user['user_pw'] + " " + user['hall'])
                self.__singleBook(self.OPTION_1, user)
                self.driver.get(self.BOOKING_URL)
                self.__singleBook(self.OPTION_2, user)

    def __singleBook(self, option, user):

        self.completed = False

        self.__tryBooking(user, 'hall', option)
        booked_hall = user['hall']

        if self.completed is False:
            try:
                self.__tryBooking(user, 'secondary_hall', option)
                booked_hall = user['secondary_hall']

            except Exception as e:
                logging.info("Errore di prenotazione per " + user['student_id'] + " | causa : " + str(e))
                self.completed = False

        if self.completed is True:
            logging.info("Prenotato : " + option + " | " + booked_hall + " | " + user['student_id'])
        else:

            logging.info("Non prenotato il turno della " + (re.search("\[(.*?)\]", option).group(1)).lower())

    def __tryBooking(self, user, hall, option):

        self.__resetBot()
        self.__goToBookingPage(user['student_id'], user['user_pw'])

        for i in range(self.MAX_RETRIES):
            try:
                self.completed = self.__book(user['library'], user[hall], option)
                break
            except Exception as e:
                logging.info("Tentativo " + str(i + 1) + " fallito " + " - " + option + " - " + hall + " | " + user[
                    hall] + " | Errore di prenotazione :  " + str(e))
                self.driver.get(self.BOOKING_URL)

    def __configChromeOptions(self):

        # collegamento con Chromium attraverso Selenium
        ua = UserAgent()
        chrome_options = webdriver.ChromeOptions()
        chrome_options._binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("user-agent=" + ua.chrome)
        return chrome_options

    def __goToBookingPage(self, user_id, user_pw):
        self.driver.get(self.LOGIN_URL)

        # xpath corrispondenti ai campi da riempire e ai box da selezionare (spunta gdpr e box "INVIA")
        userNameXPath = '//*[@id="username"]'
        WebDriverWait(self.driver, self.MAX_WAITING_TIME).until(
                EC.visibility_of_element_located((By.XPATH, userNameXPath)))
        userNameWebElement = self.driver.find_element(by = By.XPATH, value = userNameXPath)

        passwordXPath = '//*[@id="password"]'
        WebDriverWait(self.driver, self.MAX_WAITING_TIME).until(
                EC.visibility_of_element_located((By.XPATH, passwordXPath)))
        passwordWebElement = self.driver.find_element(by = By.XPATH, value = passwordXPath)

        self.__fillData(userNameWebElement, user_id)
        self.__fillData(passwordWebElement, user_pw)

        gdprBoxXPath = '//*[@id="fm1"]/div[3]/button'
        WebDriverWait(self.driver, self.MAX_WAITING_TIME).until(
                EC.visibility_of_element_located((By.XPATH, gdprBoxXPath)))
        self.__clickOnButton(gdprBoxXPath)

        # little trick to handle possible loading errors
        self.driver.get(self.LOGIN_URL)

        inviaButtonXPath = '//*[@id="form"]/div'
        WebDriverWait(self.driver, self.MAX_WAITING_TIME).until(
                EC.visibility_of_element_located((By.XPATH, inviaButtonXPath)))
        self.__clickOnButton(inviaButtonXPath)

        servizioGeneralXPath = "//select[@name = 'raggruppamento_servizi']"
        WebDriverWait(self.driver, self.MAX_WAITING_TIME).until(
                EC.visibility_of_element_located((By.XPATH, servizioGeneralXPath)))
        self.__selectFromDropdown(servizioGeneralXPath, "Servizi bibliotecari")

    def __book(self, library, hall, option = "Posto studio in biblioteca [MATTINA]"):

        servizioXPath = "//select[@name = 'servizio']"
        WebDriverWait(self.driver, self.MAX_WAITING_TIME).until(
                EC.visibility_of_element_located((By.XPATH, servizioXPath)))
        self.__selectFromDropdown(servizioXPath, option)

        # get all options text
        """ selections = Select(driver.find_element_by_xpath('// *[ @ id = "area"]'))
        for option in selections.options:
            # logging.info(option.text)
            pass """

        bibliotecheSelectionXPath = "//select[@name = 'raggruppamento_aree']"
        WebDriverWait(self.driver, self.MAX_WAITING_TIME).until(
                EC.visibility_of_element_located((By.XPATH, bibliotecheSelectionXPath)))
        self.__selectFromDropdown(bibliotecheSelectionXPath, library)
        self.__selectFromDropdown("//select[@name = 'area']", hall)

        calendarSelectionXPath = '// *[ @ id = "data_inizio-form"]'
        WebDriverWait(self.driver, self.MAX_WAITING_TIME).until(
                EC.visibility_of_element_located((By.XPATH, calendarSelectionXPath)))
        self.__clickOnButton(calendarSelectionXPath)

        datepicker = self.driver.find_element(By.CLASS_NAME, value = "datepicker-days")
        table = datepicker.find_element(By.CLASS_NAME, value = "table-condensed")
        tableRows = table.find_elements(By.CSS_SELECTOR, value = "tr")
        dateToSelect = None

        for row in tableRows:
            tableColumns = row.find_elements(By.CSS_SELECTOR, value = "td")
            for column in tableColumns:
                if str(column.get_attribute("class")) == "day":
                    dateToSelect = column

        if dateToSelect is None:
            for row in tableRows:
                tableColumns = row.find_elements(By.CSS_SELECTOR, value = "td")
                for column in tableColumns:
                    if str(column.get_attribute("class")) == "active day":
                        dateToSelect = column

        WebDriverWait(self.driver, self.MAX_WAITING_TIME).until(EC.visibility_of(dateToSelect))
        dateToSelect.click()

        verifyButtonXPath = '// *[ @ id = "verify"]'
        WebDriverWait(self.driver, self.MAX_WAITING_TIME).until(
                EC.visibility_of_element_located((By.XPATH, verifyButtonXPath)))
        self.__clickOnButton(verifyButtonXPath)

        WebDriverWait(self.driver, self.MAX_WAITING_TIME).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "slot_available ")))
        confirmButtonElement = self.driver.find_element(by = By.CLASS_NAME, value = "slot_available ")
        confirmButtonElement.click()

        confermaButtonXPath = '//*[@id="conferma"]'
        WebDriverWait(self.driver, self.MAX_WAITING_TIME).until(
                EC.visibility_of_element_located((By.XPATH, confermaButtonXPath)))
        self.__clickOnButton(confermaButtonXPath)

        return True

    def __clickOnButton(self, path):
        button = self.driver.find_element(by = By.XPATH, value = path)
        button.click()

    def __selectFromDropdown(self, path, text):
        selection = Select(self.driver.find_element(by = By.XPATH, value = path))
        selection.select_by_visible_text(text)

    def __fillData(self, webElement, data):
        # clear + autofill dei campi (clear con key_down(Keys.CONTROL).send_keys('a') )
        ActionChains(self.driver) \
            .move_to_element(webElement) \
            .click().key_down(Keys.CONTROL) \
            .send_keys('a') \
            .key_up(Keys.CONTROL) \
            .send_keys(data) \
            .perform()