import openpyxl, datetime, random


class Data:
    @staticmethod
    def __readTXT(name_file):
        file = open(name_file, "r", encoding="utf-8")
        line1 = file.readline().strip()
        line2 = file.readline().strip()
        file.close()
        if line1 == "Интранет портал государственных органов":
            print('IPGошники забивают вручную!')
            exit()
        return line1, line2

    # read xls file
    @staticmethod
    def readXLS(data_name):
        list_request, list_go, list_person, list_email = [], [], [], []
        book = openpyxl.open(data_name, read_only=True)
        sheet = book.worksheets[0]  # first list in book
        for row in range(1, sheet.max_row + 1):
            list_request.append(sheet[row][0].value)
            list_go.append(sheet[row][1].value)
            list_person.append(sheet[row][2].value)
            list_email.append(sheet[row][3].value)
        book.close()
        return list_request, list_go, list_person, list_email

    # return one record from array
    @classmethod
    def return_data(cls, request=False, gos_org=False):
        list_go_person_mail = []

        if request:
            ran = random.randint(1, len(cls.__list_data[1]))
            return cls.__list_data[0][ran]
        elif gos_org:
            ran = random.randint(1, len(cls.__list_data[1]))
            for i in range(1, 4):
                list_go_person_mail.append(cls.__list_data[i][ran])
            return list_go_person_mail

    # overwrite the number of requests
    @staticmethod
    def __write_fileTXT(text_lines):
        with open("sd.txt", "w", encoding="utf-8") as file:
            for text in text_lines:
                file.write(text + "\n")

    # Add to end file month and number of requests
    @staticmethod
    def __write_to_end_fileTXT(month, count):
        with open("sd.txt", "a", encoding="utf-8") as file:
            file.write(month + "\n")
            file.write(count + "\n")

    # Filling in the file SD
    @classmethod
    def to_change_txt_sd(cls, count):
        text_lines = []
        date = datetime.date.today()
        with open("sd.txt", "r", encoding="utf-8") as file:
            for t in file.readlines():
                text_lines.append(t.rstrip())

        if cls.number_of_mouth[date.month] == text_lines[-2]:
            count = int(text_lines[-1]) + count
            text_lines[-1] = str(count)
            cls.__write_fileTXT(text_lines)
        else:
            cls.__write_to_end_fileTXT(cls.number_of_mouth[date.month], str(count))
        file.close()

    # Data set
    try:
        __list_data = readXLS('data.xlsx')
    except:
        print("Не удалось прочитать файл data.xlsx")
    try:
        inf_sistem, person_name = __readTXT("informsystem.txt")
    except:
        print("Не удалось прочитать файл informsystem.txt")
    try:
        login, password = __readTXT("login.txt")
    except:
        print("Не удалось прочитать файл login.txt")

    XPATH = '/html/body/div[1]/div[2]/main/div[2]/div[2]/div[2]/div/div/'
    PATH = "C:\Pyton\SD\cromedriver\chromedriver.exe"
    url = [
        "https://sd.nitec.kz/pages/UI.php",
        "https://sd.nitec.kz/pages/UI.php?operation=new&class=UserRequest&c%5Borg_id%5D=1&c%5Bmenu%5D=NewUserRequest"
    ]
    number_of_mouth = {
        1: "Январь",
        2: "Февраль",
        3: "Март",
        4: "Апрель",
        5: "Май",
        6: "Июнь",
        7: "Июль",
        8: "Август",
        9: "Сентябрь",
        10: "Октябрь",
        11: "Ноябрь",
        12: "Декабрь"
    }
