import openpyxl, datetime, random

class Data:
    def __readTXT(name_file):
        file = open(name_file, "r", encoding="utf-8")
        line1 = file.readline().strip()
        line2 = file.readline().strip()
        file.close()
        if line1 == "Интранет портал государственных органов":
            print('IPGошники забивают вручную!')
            exit()
        return line1, line2

    #read xls file
    def __readXLS(data_name):
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
    def returnData(request=False, gos_org=False):
        list_go_person_mail = []

        if request:
            ran = random.randint(1, len(Data.__list_data[1]))
            return Data.__list_data[0][ran]
        elif gos_org:
            ran = random.randint(1, len(Data.__list_data[1]))
            for i in range(1, 4):
                list_go_person_mail.append(Data.__list_data[i][ran])
            return list_go_person_mail
    #overwrite the number of requests
    def __write_fileTXT(text_lines):
        file = open("sd.txt", "w", encoding="utf-8")
        for text in text_lines:
            file.write(text + "\n")
        file.close()
    # Add to end file month and number of requests
    def __write_to_end_fileTXT(month, count):
        file = open("sd.txt", "a", encoding="utf-8")
        file.write(month + "\n")
        file.write(count + "\n")
        file.close()
    #Filling in the file SD
    def to_change_txt_sd(count):
        text_lines = []
        date = datetime.date.today()
        file = open("sd.txt", "r", encoding="utf-8")
        for t in file.readlines():
            text_lines.append(t.rstrip())

        if Data.number_of_mouth[date.month] == text_lines[-2]:
            count = int(text_lines[-1]) + count
            text_lines[-1] = str(count)
            Data.__write_fileTXT(text_lines)
        else:
            Data.__write_to_end_fileTXT(Data.number_of_mouth[date.month], str(count))
        file.close()
    #Data set
    __list_data= __readXLS('data.xlsx')
    inf_sistem, person_name = __readTXT("informsystem.txt")
    login, password = __readTXT("login.txt")
    path = "C:\Pyton\SD\cromedriver\chromedriver.exe"
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




