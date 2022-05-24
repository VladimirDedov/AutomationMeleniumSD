from selenium import webdriver
from selenium_stealth import stealth
from work import Work
from utils import Data
import time
def main():
    input_number = int(input("Какое количество запросов забить? "))
    # create browser
    options = webdriver.ChromeOptions()
    # disable webdriver - brawser see all as person
    options.add_argument("--disable-blink-features=AutomationControlled")
    # Create browser
    browser = webdriver.Chrome(executable_path=Data.path)
    browser.maximize_window()
    # brawser see all as person
    stealth(browser,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
    count=0

    try:
        Work.autorization(Data.url[0], browser)
        while count!=input_number:
            request=Data.returnData(request=True)
            args=Data.returnData(gos_org=True)
            Work.completion(Data.url[1], browser, request , args[0], args[1],args[2])
            Work.presslink(browser, "Принять")#Нажать принять ссылку
            Work.threepage(browser)# Заполнить форму
            Work.pressbutton(browser)#Нажать кнопку принять
            Work.presslink(browser, "Передать на исполнение СИС, СТО")
            Work.transverSIS(browser)# Заполнить форму передать СИС
            Work.pressbutton(browser)  # Нажать кнопку передать СИС
            Work.presslink(browser, "Принять")  # Нажать принять ссылку
            Work.addperson(browser)# Выбрать исполнителя
            Work.pressbutton(browser)  # Нажать кнопку передать
            Work.presslink(browser, "Решить")  # Нажать Решить ссылку
            Work.provided(browser)# Заполнить форму описание решения
            Work.pressbutton(browser)  # Нажать кнопку Решить
            Work.presslink(browser, "Закрыть")  # Нажать Закрыть ссылку
            Work.pressbutton(browser)  # Нажать кнопку Закрыть
            count+=1

    except Exception as ex:
        print(ex)
    finally:
        browser.close()
        browser.quit()
        Data.to_change_txt_sd(count)

if __name__ == "__main__":
    main()
