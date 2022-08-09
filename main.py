import time

from selenium import webdriver
from selenium_stealth import stealth
from work import Work
from utils import Data
from report import Report


def main():
    input_number = int(input("Какое количество запросов забить? "))
    try:
        if input("Сбросить счетчик на ноль? y / n: ") == 'y':
            Report.set_count(6)
    except:
        print('Не удалось сбросить счетчик ')
    # create browser
    options = webdriver.ChromeOptions()
    # disable webdriver - brawser see all as person
    options.add_argument("--disable-blink-features=AutomationControlled")
    # Create browser
    browser = webdriver.Chrome(executable_path=Data.PATH)
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
    count = 0

    try:
        Work.autorization_in_site(Data.url[0], browser)
        while count != input_number:
            print(f"Забиваю {count + 1}-ый запрос")
            request = Data.return_data(request=True)
            args = Data.return_data(gos_org=True)
            Work.fill_first_form(Data.url[1], browser, request, args[0], args[1], args[2])
            time.sleep(1)
            Work.press_button(browser)
            Work.press_link(browser, Data.XPATH + "a[2]/span")  # Нажать принять ссылку
            Work.fill_two_form(browser)  # Заполнить форму
            print("Форма заполнена")
            Work.press_button(browser)  # Нажать кнопку принять
            Work.press_link(browser, Data.XPATH + "a[3]/span")
            print("Передано на исполнение СИС")
            Work.transver_to_sis(browser)  # Заполнить форму передать СИС
            Work.press_button(browser)  # Нажать кнопку передать СИС
            Work.press_link(browser, Data.XPATH + "a[2]/span")  # Нажать принять ссылку
            print("Запрос принят")
            Work.add_person_in_four_form(browser)  # Выбрать исполнителя
            print("Выбран исполнитель")
            Work.press_button(browser)  # Нажать кнопку передать
            Work.press_link(browser, Data.XPATH + "a[1]/span")  # Нажать Решить ссылку
            Work.fill_solution(browser)  # Заполнить форму описание решения
            Work.press_button(browser)  # Нажать кнопку Решить
            print("Запрос решен")
            Work.press_link(browser, Data.XPATH + "a[2]/span")  # Нажать Закрыть ссылку
            time.sleep(2)
            Report.add_list_report(request, args[0])
            count += 1

    except Exception as ex:
        print(ex)
    finally:
        browser.close()
        browser.quit()
        try:
            Data.to_change_txt_sd(count)
        except:
            print("Не удалось записать счетчик забитых вопросов.")
        try:
            Report.record_report_xls()
        except:
            print("Не удалось записать запросы в XLS файл!")


if __name__ == "__main__":
    main()
