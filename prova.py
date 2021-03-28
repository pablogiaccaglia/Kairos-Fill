from selenium.webdriver.support.select import Select
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def fillerUserData():
    # collegamento con Chromium attraverso Selenium
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(executable_path="/Users/pablo/Desktop/chromedriver")
    time.sleep(1)
    driver.get(
        "https://identity.unifi.it/cas/login?service=https%3A%2F%2Fidentity.unifi.it%2Fcas%2Fidp%2Fprofile%2FSAML2%2FCallback%3FentityId%3Dhttps%253A%252F%252Fkairos.unifi.it%252Fsimplesaml%252Fmodule.php%252Fsaml%252Fsp%252Fmetadata.php%252Fep-prod%26SAMLRequest%3DPD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48c2FtbHA6QXV0aG5SZXF1ZXN0IHhtbG5zOnNhbWxwPSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6cHJvdG9jb2wiIHhtbG5zOnNhbWw9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjIuMDphc3NlcnRpb24iIEFzc2VydGlvbkNvbnN1bWVyU2VydmljZVVSTD0iaHR0cHM6Ly9rYWlyb3MudW5pZmkuaXQvc2ltcGxlc2FtbC9tb2R1bGUucGhwL3NhbWwvc3Avc2FtbDItYWNzLnBocC9lcC1wcm9kIiBEZXN0aW5hdGlvbj0iaHR0cHM6Ly9pZGVudGl0eS51bmlmaS5pdC9jYXMvaWRwL3Byb2ZpbGUvU0FNTDIvUE9TVC9TU08iIElEPSJfMDdjNTA4MjVjNmQxYTA4OGJiOTNkY2IzNTFjN2Y2MDNjOTYwNTZjMzhlIiBJc3N1ZUluc3RhbnQ9IjIwMjEtMDMtMTJUMjE6MDU6MDdaIiBQcm90b2NvbEJpbmRpbmc9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjIuMDpiaW5kaW5nczpIVFRQLVBPU1QiIFZlcnNpb249IjIuMCI%252BPHNhbWw6SXNzdWVyPmh0dHBzOi8va2Fpcm9zLnVuaWZpLml0L3NpbXBsZXNhbWwvbW9kdWxlLnBocC9zYW1sL3NwL21ldGFkYXRhLnBocC9lcC1wcm9kPC9zYW1sOklzc3Vlcj48ZHM6U2lnbmF0dXJlIHhtbG5zOmRzPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwLzA5L3htbGRzaWcjIj4KICA8ZHM6U2lnbmVkSW5mbz48ZHM6Q2Fub25pY2FsaXphdGlvbk1ldGhvZCBBbGdvcml0aG09Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvMTAveG1sLWV4Yy1jMTRuIyIvPgogICAgPGRzOlNpZ25hdHVyZU1ldGhvZCBBbGdvcml0aG09Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvMDQveG1sZHNpZy1tb3JlI3JzYS1zaGEyNTYiLz4KICA8ZHM6UmVmZXJlbmNlIFVSST0iI18wN2M1MDgyNWM2ZDFhMDg4YmI5M2RjYjM1MWM3ZjYwM2M5NjA1NmMzOGUiPjxkczpUcmFuc2Zvcm1zPjxkczpUcmFuc2Zvcm0gQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwLzA5L3htbGRzaWcjZW52ZWxvcGVkLXNpZ25hdHVyZSIvPjxkczpUcmFuc2Zvcm0gQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzEwL3htbC1leGMtYzE0biMiLz48L2RzOlRyYW5zZm9ybXM%252BPGRzOkRpZ2VzdE1ldGhvZCBBbGdvcml0aG09Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvMDQveG1sZW5jI3NoYTI1NiIvPjxkczpEaWdlc3RWYWx1ZT5xZGs0MUpGZ1JXdzBZMWx5SmFqQ25Ub2p5Z0ZSTVNQWGFBKzI3ejdKR3dnPTwvZHM6RGlnZXN0VmFsdWU%252BPC9kczpSZWZlcmVuY2U%252BPC9kczpTaWduZWRJbmZvPjxkczpTaWduYXR1cmVWYWx1ZT5jajRucUtjb2t2QXdCdldFalphVXRCUk1VSW9COUFKTUNjWlVCR3B0MU1FbGJOTlNxL3hudEFqeGltMFZ1Q3FvRHJnSmN6a0d6SjBCbmEzc1ovQ1ZFZ3B2eCtadEZGWE1lVVN4ZW45Q0ZHRGdGSWUwbFQ0MEkvbVUyV2g3Szh2M1gwZUNoclVwT2R1SmJNZW1ZbmNTVXp2NnNKWkNkOElaMXVYSlVnbXp2bEk9PC9kczpTaWduYXR1cmVWYWx1ZT4KPGRzOktleUluZm8%252BPGRzOlg1MDlEYXRhPjxkczpYNTA5Q2VydGlmaWNhdGU%252BTUlJRGZqQ0NBdWVnQXdJQkFnSUpBTnV3VzVDaG1DTkFNQTBHQ1NxR1NJYjNEUUVCQlFVQU1JR0hNUXN3Q1FZRFZRUUdFd0pKVkRFT01Bd0dBMVVFQ0JNRlNYUmhiSGt4RGpBTUJnTlZCQWNUQlZWa2FXNWxNUkl3RUFZRFZRUUtFd2xGWVhONVUzUmhabVl4SWpBZ0JnTlZCQU1UR1dWaGMzbGhZMkZrWlcxNU15NWxZWE41YzNSaFptWXVhWFF4SURBZUJna3Foa2lHOXcwQkNRRVdFV2x1Wm05QVpXRnplWE4wWVdabUxtbDBNQjRYRFRFMk1ESXlOVEE1TVRVME5sb1hEVEkyTURJeU5EQTVNVFUwTmxvd2dZY3hDekFKQmdOVkJBWVRBa2xVTVE0d0RBWURWUVFJRXdWSmRHRnNlVEVPTUF3R0ExVUVCeE1GVldScGJtVXhFakFRQmdOVkJBb1RDVVZoYzNsVGRHRm1aakVpTUNBR0ExVUVBeE1aWldGemVXRmpZV1JsYlhrekxtVmhjM2x6ZEdGbVppNXBkREVnTUI0R0NTcUdTSWIzRFFFSkFSWVJhVzVtYjBCbFlYTjVjM1JoWm1ZdWFYUXdnWjh3RFFZSktvWklodmNOQVFFQkJRQURnWTBBTUlHSkFvR0JBTXhOQ1Mvc2FSV2ZlZU5YS3M2MjdCUTA5WFJyd2RzS1A4SHNrd2tNd0xCbXJhcElGUko5cUpMcVpYYUdjZ0o3aWd4NHlqSURFdDRyT3p6dHdLcWNlYVlEV3E3b0NvekdjY1B1aXZLYUJEK0Z4VGcwT0UwOEdsNDh5TXU1NnpOaTRFQ3llUVpWd05OSHpBTWhRdEcxM3YxTm1tNFlVQ2Izd0R2OGZPWG1aWXpwQWdNQkFBR2pnZTh3Z2V3d0hRWURWUjBPQkJZRUZMYmZaY2dmR21raEgyUWUzUkRJeTdUR2t4aDFNSUc4QmdOVkhTTUVnYlF3Z2JHQUZMYmZaY2dmR21raEgyUWUzUkRJeTdUR2t4aDFvWUdOcElHS01JR0hNUXN3Q1FZRFZRUUdFd0pKVkRFT01Bd0dBMVVFQ0JNRlNYUmhiSGt4RGpBTUJnTlZCQWNUQlZWa2FXNWxNUkl3RUFZRFZRUUtFd2xGWVhONVUzUmhabVl4SWpBZ0JnTlZCQU1UR1dWaGMzbGhZMkZrWlcxNU15NWxZWE41YzNSaFptWXVhWFF4SURBZUJna3Foa2lHOXcwQkNRRVdFV2x1Wm05QVpXRnplWE4wWVdabUxtbDBnZ2tBMjdCYmtLR1lJMEF3REFZRFZSMFRCQVV3QXdFQi96QU5CZ2txaGtpRzl3MEJBUVVGQUFPQmdRQWk5WjdDeGhJMkg0RmNFdy9oaXVBR3VRT1BKY1B1YjF4ZHZlMmVEc2dSNGFaUXROQU92Q0h4a0tNUVMyUjJGVDZuVWpWcXZSTS9Lck1RdGU4dk02SGpQRXJ3d2x4WG8vVi9XeDBsc0h2dDFYUlQyaVlCY1FSQW5XOW53L3VaVitaK1RORVcycUxsM2pHUFhoWXVHYnlRcWJhcS9HWDJmWUFtcjNKa09zbVFHUT09PC9kczpYNTA5Q2VydGlmaWNhdGU%252BPC9kczpYNTA5RGF0YT48L2RzOktleUluZm8%252BPC9kczpTaWduYXR1cmU%252BPHNhbWxwOk5hbWVJRFBvbGljeSBBbGxvd0NyZWF0ZT0idHJ1ZSIgRm9ybWF0PSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6bmFtZWlkLWZvcm1hdDp0cmFuc2llbnQiLz48L3NhbWxwOkF1dGhuUmVxdWVzdD4%253D%26RelayState%3Dhttps%253A%252F%252Fkairos.unifi.it%252FportalePlanning%252Fauth%252Fauth_es.php%253Fresponse_type%253Dtoken%2526client_id%253Dclient%2526redirect_uri%253Dhttps%253A%252F%252Fkairos.unifi.it%252FportalePlanning%252FBIBL%252Flogin.php%2526scope%253Dopenid%252Bprofile%2526customer%253DBIBL")
    time.sleep(1)

    # xpath corrispondenti ai campi da riempire e ai box da selezionare (spunta gdpr e box "INVIA")
    userName = driver.find_element_by_xpath('//*[@id="username"]')
    print("qui2")
    password = driver.find_element_by_xpath('//*[@id="password"]')
    time.sleep(1)

    # clear + autofill dei campi (clear con key_down(Keys.CONTROL).send_keys('a') )
    ActionChains(driver) \
        .move_to_element(userName) \
        .click().key_down(Keys.CONTROL) \
        .send_keys('a') \
        .key_up(Keys.CONTROL) \
        .send_keys("7028112") \
        .perform()

    ActionChains(driver) \
        .move_to_element(password) \
        .click() \
        .key_down(Keys.CONTROL) \
        .send_keys('a') \
        .key_up(Keys.CONTROL) \
        .send_keys("Vannoni-1") \
        .perform()

    # spunta gdpr + click box "INVIA"
    # time.sleep(2)
    clickOnButton(driver, '//*[@id="fm1"]/div[3]/button')

    time.sleep(6)
    clickOnButton(driver, '//*[@id="form"]/div')

    #  time.sleep(2)
    selectFromDropdown(driver, "//select[@name = 'raggruppamento_servizi']", "Servizi bibliotecari")

    #  time.sleep(2)
    selectFromDropdown(driver, "//select[@name = 'servizio']", "Posto studio in biblioteca")

    selections = Select(driver.find_element_by_xpath('// *[ @ id = "area"]'))
    # get all options text
    for option in selections.options:
        print(option.text)


    #  time.sleep(2)
    selectFromDropdown(driver, "//select[@name = 'raggruppamento_aree']", "Biblioteca di Scienze Sociali")

    #  time.sleep(2)
    selectFromDropdown(driver, "//select[@name = 'area']", "Biblioteca di Scienze sociali - Sale Primo piano")

    #  time.sleep(2)

    driver.find_element_by_xpath('// *[ @ id = "data_inizio-form"]').is_displayed()

    time.sleep(2)
    clickOnButton(driver, '// *[ @ id = "data_inizio-form"]')
    clickOnButton(driver, '//*[@id="data_inizio-container"]/div[3]/div[1]/table/tbody/tr[6]/td[3]')


    time.sleep(2)

    clickOnButton(driver, '// *[ @ id = "verify"]')

    time.sleep(2)
    driver.quit()

    print("Prenotato")


def clickOnButton(driver, path):
    button = driver.find_element_by_xpath(path)
    button.click()


def selectFromDropdown(driver, path, text):
    selection = Select(driver.find_element_by_xpath(path))
    selection.select_by_visible_text(text)



if __name__ == '__main__':
    fillerUserData()
