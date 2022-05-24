
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from utils import Data

class Work:
    def completion(url, browser, request, gos_org, person, email):
        # pass url
        browser.get(url=url)
        time.sleep(2)
        # search and input inform sistem
        inf_sistem = browser.find_element(By.ID, "label_2_application_solution")
        inf_sistem.clear()
        inf_sistem.send_keys((Data.inf_sistem))
        time.sleep(3)
        inf_sistem.send_keys(Keys.ENTER)
        # find frame
        frame = browser.find_element(By.XPATH, "//div[@id='cke_1_contents']/iframe")
        # change second frame
        browser.switch_to.frame(frame)
        req_description = browser.find_element(By.XPATH, "/ html / body")
        req_description.clear()
        req_description.send_keys(request)#data request person
        # change main frame
        browser.switch_to.default_content()
        # Selector
        selector = browser.find_element(By.ID, "2_type_of_correspondent")
        time.sleep(1)
        Select(selector).select_by_value("State body")
        # Correspondent
        go = browser.find_element(By.ID, "2_other_correspondent").send_keys(gos_org)# G O
        # region
        go = browser.find_element(By.ID, "2_region")
        Select(go).select_by_value("35")
        # Category
        reg = browser.find_element(By.ID, "2_servicesubcategory_id")
        Select(reg).select_by_value("2")
        # person
        go = browser.find_element(By.ID, "2_client_name").send_keys(person)
        # mail
        go = browser.find_element(By.ID, "2_client_email").send_keys(email)
        # send sozdat
        time.sleep(3)
        Work.pressbutton(browser)
        time.sleep(2)

    def transverSIS(browser):
        time.sleep(2)
        # find frame
        frame = browser.find_element(By.XPATH, "//div[@id='cke_1_contents']/iframe")
        # change second frame
        browser.switch_to.frame(frame)
        req_description = browser.find_element(By.XPATH, "/ html / body")
        req_description.clear()
        req_description.send_keys("В работу")
        # change main frame
        browser.switch_to.default_content()
        selector = browser.find_element(By.ID, "att_1")
        Select(selector).select_by_value("165")
        time.sleep(2)

    def autorization(url, browser):
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

    def presslink(browser, text):
        accept = browser.find_element(By.LINK_TEXT, text)
        accept.click()

    def pressbutton(browser):
        time.sleep(1)
        accept = browser.find_element(By.XPATH, "//button[@type='submit']")
        accept.click()
        time.sleep(2)

    def threepage(browser):
        selector = browser.find_element(By.ID, "att_1")
        Select(selector).select_by_visible_text("Сопровождение клиентских мест пользователей (Консультация, обучение, установка ПО)")
        selector = browser.find_element(By.ID, "att_2")
        Select(selector).select_by_value("1282")
        time.sleep(2)

    def addperson(browser):
        selector = browser.find_element(By.ID, "att_2")
        Select(selector).select_by_visible_text(Data.person_name)
        time.sleep(2)

    def provided(browser):
        input_m = browser.find_element(By.ID, "att_0")
        input_m.clear()
        input_m.send_keys("Консультация оказана")
        time.sleep(2)

