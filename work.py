import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from utils import Data


class Work:
    @staticmethod
    def fill_first_form(url, browser, request, gos_org, person, email):
        # pass url
        browser.get(url=url)
        time.sleep(2)

        # search and input inform system
        inf_sistem = browser.find_element(By.ID, "label_2_application_solution")
        inf_sistem.clear()
        inf_sistem.send_keys((Data.inf_system))
        time.sleep(4)
        inf_sistem.send_keys(Keys.ENTER)
        time.sleep(2)

        # find frame
        frame = browser.find_element(By.XPATH,
                                     "/html/body/div[1]/div[2]/main/form/div/div[3]/div/div/div[1]/div[2]/div/div[1]/fieldset[1]/div[7]/div[2]/div/div/div/div/div/div/iframe")
        # change second frame
        browser.switch_to.frame(frame)
        req_description = browser.find_element(By.XPATH, "/ html / body")
        req_description.clear()
        req_description.send_keys(request)  # data request person
        # change main frame
        browser.switch_to.default_content()

        # Selector correspondent
        selector = browser.find_element(By.ID, "2_type_of_correspondent")
        time.sleep(1)
        Select(selector).select_by_value("State body")

        # region
        go = browser.find_element(By.XPATH, "//*[@id='2_region-selectized']")
        go.clear()
        go.send_keys('Северо-Казахстанская область')
        time.sleep(1)
        go.send_keys(Keys.ENTER)
        time.sleep(1)

        # Correspondent
        go = browser.find_element(By.ID, "2_other_correspondent").send_keys(gos_org)  # G O        p
        time.sleep(1)

        # Category
        go = browser.find_element(By.ID, "2_servicesubcategory_id-selectized")
        go.clear()
        go.send_keys('ОЦИТ')
        go.send_keys(Keys.ENTER)

        # person
        go = browser.find_element(By.ID, "2_client_name").send_keys(person)

        # mail
        go = browser.find_element(By.ID, "2_client_email").send_keys(email)

        time.sleep(2)

    @staticmethod
    def transver_to_sis(browser):
        time.sleep(2)
        go = browser.find_element(By.XPATH, "//*[@id='att_1-selectized']")
        go.clear()
        go.send_keys('СИС')
        time.sleep(1)
        go.send_keys(Keys.ENTER)

        # find frame
        frame = browser.find_element(By.XPATH,
                                     "/html/body/div[1]/div[2]/main/div[2]/div[2]/form/table/tbody/tr/td/div/div[1]/div[2]/span/div/div/div[2]/div[1]/div/div/iframe")
        # change second frame
        browser.switch_to.frame(frame)
        req_description = browser.find_element(By.XPATH, "/ html / body")
        req_description.clear()
        req_description.send_keys("В работу")
        # change main frame
        browser.switch_to.default_content()

    @staticmethod
    def autorization_in_site(url, browser):
        browser.get(url=url)
        # search AND input login
        input_m = browser.find_element(By.ID, "user")
        input_m.clear()
        input_m.send_keys(Data.login)
        # search and input password
        input_p = browser.find_element(By.ID, "pwd")
        input_p.clear()
        input_p.send_keys(Data.password)
        time.sleep(1)
        # click ENTER
        input_p.send_keys(Keys.ENTER)
        time.sleep(1)

    @staticmethod
    def press_link(browser, xpath):
        time.sleep(1)
        browser.refresh()
        time.sleep(1)
        accept = browser.find_element(By.XPATH, xpath)
        accept.click()

    @staticmethod
    def press_button(browser):
        time.sleep(1)
        accept = browser.find_element(By.XPATH, "//button[@type='submit']")
        accept.click()
        time.sleep(2)

    @staticmethod
    def fill_two_form(browser):
        time.sleep(2)
        go = browser.find_element(By.XPATH, "//*[@id='att_1-selectized']")
        go.clear()
        go.send_keys('Сопровождение клиентских мест пользователей (Консультация, обучение, установка ПО)')
        time.sleep(1)
        go.send_keys(Keys.ENTER)
        go = browser.find_element(By.XPATH, "//*[@id='att_2-selectized']")
        go.clear()
        go.send_keys('Эдуард Маляуцкий')
        time.sleep(1)
        go.send_keys(Keys.ENTER)
        time.sleep(3)

    @staticmethod
    def add_person_in_four_form(browser):
        time.sleep(2)
        go = browser.find_element(By.XPATH, "//*[@id='att_2-selectized']")
        go.clear()
        go.send_keys(Data.person_name)
        time.sleep(1)
        go.send_keys(Keys.ENTER)
        time.sleep(1)

    @staticmethod
    def fill_solution(browser):
        time.sleep(1)
        go = browser.find_element(By.XPATH, "//*[@id='att_0']")
        go.clear()
        go.send_keys("Консультация оказана")
        time.sleep(1)
