import random, time, openpyxl, os, datetime, shutil
from utils import Data


class Report:
    __list_report = []

    @staticmethod
    def set_count(count):
        with open(f"C:\\Pyton\\SD\\cromedriver\\report\\count.txt", 'w', encoding="utf-8") as file:
            file.write(str(count))

    @staticmethod
    def get_count():
        with open(f"C:\\Pyton\\SD\\cromedriver\\report\\count.txt", "r", encoding="utf-8") as file:
            return int(file.readline().strip())

    @classmethod
    def add_list_report(cls, request, gos_org):
        cls.__list_report.append(request + ' в ' + gos_org)

        # write in reports

    @classmethod
    def record_report_xls(cls, flag=True):
        date = datetime.date.today()
        path_xls = f'C:\\Pyton\\SD\\cromedriver\\report\\{date} {Data.person_name}.xlsx'
        path_pattern = 'C:\\Pyton\\SD\\cromedriver\\report\\report_pattern.xlsx'

        if os.path.exists(path_xls) == False:
            print(f'Создаю отчет {date} {Data.person_name}.xlsx')
            shutil.copyfile(path_pattern, path_xls)

        book = openpyxl.load_workbook(path_xls)
        sheet = book.worksheets[0]
        count = cls.get_count()

        i = 0
        while i < len(cls.__list_report):
            sheet[f'B{i + count}'] = cls.__list_report[i]
            sheet[f'F{i + count}'] = "Консультация оказана"
            i += 1

        count += len(cls.__list_report)
        cls.set_count(count)
        print('Запись в отчет')
        sheet[f'A2'] = f'{date.day} {Data.number_of_mouth[date.month].lower()} {date.year} г.'
        cls.save_report(book, path_xls)

    @staticmethod
    def get_shuffle(lst):
        random.shuffle(lst)
        return lst

    @classmethod
    def record_report_all(cls, list_data, flag=True):
        list_question = cls.get_shuffle(list_data[0])
        list_go = cls.get_shuffle(list_data[1])
        date = datetime.date.today()
        path_xls = f'C:\\Pyton\\SD\\cromedriver\\report\\{date} {Data.person_name}.xlsx'
        book = openpyxl.load_workbook(path_xls)
        sheet = book.worksheets[0]
        count = cls.get_count()

        while count <= 15:
            sheet[f'B{count}'] = list_question[count] + ' в ' + list_go[count]
            sheet[f'F{count}'] = "Выполнено"
            count += 1

        sheet[f'A2'] = f'{date.day} {Data.number_of_mouth[date.month].lower()} {date.year} г.'
        cls.set_count(6)
        print('Запись в отчет')
        cls.save_report(book, path_xls)

    @staticmethod
    def save_report(book, path_xls, flag=True):
        try:
            book.save(path_xls)
        except Exception as ex:
            print("Не удалось записать отчет :(")
            flag = False
        if flag:
            print('Отчет успешно записан!')
        time.sleep(4)


def main():
    if input("Сбросить счетчик на ноль? y / n: ") == 'y':
        Report.set_count(6)
    list_data = Data.readXLS('C:\\Pyton\\SD\\cromedriver\\report\\data.xlsx')
    Report.record_report_all(list_data)


if __name__ == '__main__':
    main()
