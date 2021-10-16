from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC


class KairosBot:

    def __init__(self):

        self.chrome_options = self.__configChromeOptions()
        self.driver = webdriver.Chrome(executable_path="/Users/pablo/Desktop/chromedriver", chrome_options=self.chrome_options)

    def resetBot(self):
        if not str(self.driver).__contains__("null"):
            self.driver.quit()
        self.__init__()

    def __configChromeOptions(self):
        # collegamento con Chromium attraverso Selenium
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        return chrome_options

    def fillerUserData(self, user_id, user_pw, library, hall):
        try:

            self.driver.get("https://kairos.unifi.it/portalePlanning/BIBL/login.php")

            # xpath corrispondenti ai campi da riempire e ai box da selezionare (spunta gdpr e box "INVIA")
            userNameXPath = '//*[@id="username"]'
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, userNameXPath)))
            userNameWebElement = self.driver.find_element(by=By.XPATH, value=userNameXPath)

            passwordXPath = '//*[@id="password"]'
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, passwordXPath)))
            passwordWebElement = self.driver.find_element(by=By.XPATH, value=passwordXPath)

            self.__fillData(userNameWebElement, user_id)
            self.__fillData(passwordWebElement, user_pw)

            gdprBoxXPath = '//*[@id="fm1"]/div[3]/button'
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, gdprBoxXPath)))
            self.__clickOnButton(gdprBoxXPath)

            self.driver.get("https://kairos.unifi.it/portalePlanning/BIBL/login.php")

            inviaButtonXPath = '//*[@id="form"]/div'
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, inviaButtonXPath)))
            self.__clickOnButton(inviaButtonXPath)

            servizioGeneralXPath = "//select[@name = 'raggruppamento_servizi']"
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, servizioGeneralXPath)))
            self.__selectFromDropdown(servizioGeneralXPath, "Servizi bibliotecari")

            servizioXPath = "//select[@name = 'servizio']"
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, servizioXPath)))
            self.__selectFromDropdown(servizioXPath, "Posto studio in biblioteca")

            # get all options text
            """ selections = Select(driver.find_element_by_xpath('// *[ @ id = "area"]'))
            for option in selections.options:
                # print(option.text)
                pass """

            if hall == "Biblioteca di Scienze sociali - Sale Primo piano":
                hall = "Biblioteca di Scienze sociali - Sale Secondo piano"

            bibliotecheSelectionXPath = "//select[@name = 'raggruppamento_aree']"
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, bibliotecheSelectionXPath)))
            self.__selectFromDropdown(bibliotecheSelectionXPath, library)
            self.__selectFromDropdown("//select[@name = 'area']", hall)

            calendarSelectionXPath = '// *[ @ id = "data_inizio-form"]'
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, calendarSelectionXPath)))
            self.__clickOnButton(calendarSelectionXPath)

            datepicker = self.driver.find_element(By.CLASS_NAME, value="datepicker-days")
            table = datepicker.find_element(By.CLASS_NAME, value="table-condensed")
            tableRows = table.find_elements(By.CSS_SELECTOR, value="tr")
            dateToSelect = None

            for row in tableRows:
                tableColumns = row.find_elements(By.CSS_SELECTOR, value="td")
                for column in tableColumns:
                    if str(column.get_attribute("class")) == "active day":
                        dateToSelect = column

            WebDriverWait(self.driver, 5).until(EC.visibility_of(dateToSelect))
            dateToSelect.click()

            verifyButtonXPath = '// *[ @ id = "verify"]'
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, verifyButtonXPath)))
            self.__clickOnButton(verifyButtonXPath)

            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "slot_available ")))
            confirmButtonElement = self.driver.find_element(by=By.CLASS_NAME, value="slot_available ")
            confirmButtonElement.click()

            confermaButtonXPath = '//*[@id="conferma"]'
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, confermaButtonXPath)))
            self.__clickOnButton(confermaButtonXPath)

            print("Prenotato : " + user_id)

        except Exception as e:
            print("Errore di prenotazione :  " + str(e))
            # fillerUserData(aula,nome, mail, matricola, telefono, row, column)

    def __clickOnButton(self, path):
        button = self.driver.find_element(by=By.XPATH, value=path)
        button.click()

    def __selectFromDropdown(self, path, text):
        selection = Select(self.driver.find_element(by=By.XPATH, value=path))
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
