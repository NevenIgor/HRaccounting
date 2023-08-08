from PyQt5 import QtCore, QtWidgets, QtGui
import time

from db_API import Database as DB


class PersonWidget(QtWidgets.QScrollArea):
    def __init__(self, main_data):
        super(PersonWidget, self).__init__()
        widget = QtWidgets.QWidget()
        main_layout = QtWidgets.QVBoxLayout(widget)
        main_layout.setAlignment(QtCore.Qt.AlignTop)

        if not main_data:
            data = dict()
            data['rank'] = ''
            data['surname'] = ''
            data['name'] = ''
            data['patr'] = ''
            data['person_ID'] = ''
            data['birthday'] = ''
            data['place_of_birth'] = ''
            data['nation'] = ''
            data['family_status'] = ''
            data['gender'] = ''
            data['division'] = ''
            data['position'] = ''
            data['mobile_number'] = ''
            data['phone_number'] = ''
            data['personal_business'] = ''
            data["date_of_join"] = ''
            data['contract_from'] = ''
            data['contract_type'] = ''
            data['contract_order'] = ''
            data['contract_ord_data'] = ''
            data['allowance_form'] = ''
            data['allowance_num'] = ''
            data['allowance_data'] = ''
        else:
            data = dict()
            data['rank'] = ''
            data['surname'] = main_data[1]
            data['name'] = main_data[2]
            data['patr'] = main_data[3]
            data['person_ID'] = main_data[0]
            data['birthday'] = main_data[4]
            data['place_of_birth'] = main_data[5]
            data['nation'] = main_data[6]
            data['family_status'] = main_data[7]
            data['gender'] = main_data[8]
            data['division'] = main_data[9]
            data['position'] = main_data[10]
            data['mobile_number'] = main_data[11]
            data['phone_number'] = main_data[12]
            data['personal_business'] = main_data[13]
            data["date_of_join"] = ''
            data['contract_from'] = ''
            data['contract_type'] = ''
            data['contract_order'] = ''
            data['contract_ord_data'] = ''
            data['allowance_form'] = ''
            data['allowance_num'] = ''
            data['allowance_data'] = ''

        first_group = QtWidgets.QGroupBox('Персональные данные')
        first_level = QtWidgets.QHBoxLayout()
        self.img_label = QtWidgets.QLabel('')
        self.img_label.setStyleSheet('border: 1px solid #333')
        if not data['person_ID']:
            pixmap = QtGui.QPixmap('4.jpg')
        else:
            pixmap = QtGui.QPixmap('PATH TO PHOTO')
        pixmap = pixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
        self.img_label.setPixmap(pixmap)
        self.img_label.setAlignment(QtCore.Qt.AlignCenter)

        p1 = QtWidgets.QVBoxLayout()
        p1.setAlignment(QtCore.Qt.AlignCenter)
        self.labels = dict()
        self.labels['person1'] = dict()
        self.labels['person1']['rank'] = QtWidgets.QLabel(f"<b>{data['rank']}</b>")
        self.labels['person1']['surname'] = QtWidgets.QLabel(f"<b>{data['surname']}</b>")
        self.labels['person1']['name'] = QtWidgets.QLabel(f"<b>{data['name']}</b>")
        self.labels['person1']['patr'] = QtWidgets.QLabel(f"<b>{data['patr']}</b>")

        for label in self.labels['person1'].keys():
            self.labels['person1'][label].setAlignment(QtCore.Qt.AlignCenter)
            p1.addWidget(self.labels['person1'][label])

        self.labels['person2'] = dict()
        self.labels['person2']['number'] = QtWidgets.QLabel(data['person_ID'])
        self.labels['person2']['gender'] = QtWidgets.QLabel(data['gender'])
        self.labels['person2']['birthday_date'] = QtWidgets.QLabel(str(data['birthday']))
        self.labels['person2']['place_of_birth'] = QtWidgets.QLabel(data['place_of_birth'])
        self.labels['person2']['nation'] = QtWidgets.QLabel(data['nation'])
        self.labels['person2']['family_status'] = QtWidgets.QLabel(data['family_status'])
        self.labels['person2']['division'] = QtWidgets.QLabel(data['division'])
        self.labels['person2']['position'] = QtWidgets.QLabel(data['position'])
        self.labels['person2']['mobile_number'] = QtWidgets.QLabel(data['mobile_number'])
        self.labels['person2']['phone_number'] = QtWidgets.QLabel(data['phone_number'])
        self.labels['person2']['personal_business'] = QtWidgets.QLabel(data['personal_business'])

        form = QtWidgets.QFormLayout()
        form.addRow('Личный номер:', self.labels['person2']['number'])
        form.addRow('Пол:', self.labels['person2']['gender'])
        form.addRow('Дата рождения:', self.labels['person2']['birthday_date'])
        form.addRow('Место рождения:', self.labels['person2']['place_of_birth'])
        form.addRow('Национальность:', self.labels['person2']['nation'])
        form.addRow('Семейное положение:', self.labels['person2']['family_status'])
        form.addRow('Подразделение:', self.labels['person2']['division'])
        form.addRow('Должность:', self.labels['person2']['position'])
        form.addRow('Сот. телефон:', self.labels['person2']['mobile_number'])
        form.addRow('Рабочий телефон:', self.labels['person2']['phone_number'])
        form.addRow('Номер личного дела:', self.labels['person2']['personal_business'])

        first_level.addWidget(self.img_label)
        first_level.addLayout(p1)
        first_level.addLayout(form)
        first_group.setLayout(first_level)

        main_layout.addWidget(first_group)

        if data['person_ID']:

            second_level = QtWidgets.QHBoxLayout()
            contract_gr = QtWidgets.QGroupBox('Контракт')
            form = QtWidgets.QFormLayout()
            contract_to = '24.09.27'
            form.addRow('Заключен от:', QtWidgets.QLabel(data['contract_from']))
            form.addRow('Срок заключения:', QtWidgets.QLabel(data['contract_type']))
            form.addRow('Заканчивается:', QtWidgets.QLabel(contract_to))
            form.addRow('Приказ:', QtWidgets.QLabel(data['contract_order']))
            form.addRow('Дата приказа:', QtWidgets.QLabel(data['contract_ord_data']))
            contract_gr.setLayout(form)

            allowance_gr = QtWidgets.QGroupBox('Допуск')
            form = QtWidgets.QFormLayout()
            form.addRow('Форма допуска', QtWidgets.QLabel(data['allowance_form']))
            form.addRow('Номер допуска', QtWidgets.QLabel(data['allowance_num']))
            form.addRow('Дата выдачи', QtWidgets.QLabel(data['allowance_data']))
            allowance_gr.setLayout(form)
            second_level.addWidget(contract_gr)
            second_level.addWidget(allowance_gr)

            passage_gr = QtWidgets.QGroupBox('Прохождение службы')
            passage_l = QtWidgets.QVBoxLayout()
            label = QtWidgets.QLabel(f'<b>В Вооруженных силах с {data["date_of_join"]}</b>')
            label.setAlignment(QtCore.Qt.AlignCenter)
            passage_l.addWidget(label)
            passage_table = QtWidgets.QTableWidget(1, 3)
            passage_table.setHorizontalHeaderLabels(('Дата', 'Условное\nнаименование', 'Должность'))
            passage_l.addWidget(passage_table)
            passage_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            passage_table.clicked.connect(self.open_passage)
            label = QtWidgets.QLabel(f'<b>Выслуга лет: {data["date_of_join"]}</b>')
            label.setAlignment(QtCore.Qt.AlignCenter)
            passage_l.addWidget(label)
            passage_gr.setLayout(passage_l)

            third_level = QtWidgets.QHBoxLayout()
            doc_gr = QtWidgets.QGroupBox('Документы')
            doc_l = QtWidgets.QVBoxLayout()
            doc_table = QtWidgets.QTableWidget(1, 5)
            doc_table.setHorizontalHeaderLabels(('Тип', 'Серия', 'Номер', 'Кем\nвыдан', 'Дата'))
            doc_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            doc_l.addWidget(doc_table)
            doc_gr.setLayout(doc_l)
            family_gr = QtWidgets.QGroupBox('Родственники')
            family_l = QtWidgets.QVBoxLayout()
            family_table = QtWidgets.QTableWidget(1, 5)
            family_table.setHorizontalHeaderLabels(('Степень\nродства', 'ФИО', 'Дата\nрождения', 'Документ', 'Телефон'))
            family_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            family_l.addWidget(family_table)
            family_gr.setLayout(family_l)
            third_level.addWidget(doc_gr)
            third_level.addWidget(family_gr)

            rank_gr = QtWidgets.QGroupBox('Прохождение службы')
            rank_l = QtWidgets.QVBoxLayout()
            rank_table = QtWidgets.QTableWidget(1, 5)
            rank_table.setHorizontalHeaderLabels(('Звание', 'Дата присвоения', 'Приказ', 'Номер приказа', 'Дата приказа'))
            rank_l.addWidget(rank_table)
            rank_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            rank_table.clicked.connect(self.open_passage)
            rank_gr.setLayout(rank_l)

            main_layout.addLayout(second_level)
            main_layout.addWidget(passage_gr)
            main_layout.addLayout(third_level)
            main_layout.addWidget(rank_gr)

        self.setWidget(widget)
        self.setWidgetResizable(True)

    def open_passage(self):
        pass


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.db = DB('db.db')

        data = dict()
        data['rank'] = 'Лейтенант'
        data['surname'] = 'ПЕТРОВ'
        data['name'] = 'Иван'
        data['patr'] = 'Иванович'
        data['person_ID'] = 'A-00002'
        data['birthday'] = time.time()
        data['place_of_birth'] = 'г. Москва'
        data['nation'] = 'русский'
        data['family_status'] = 'женат'
        data['gender'] = 'Мужской'
        data['division'] = 'в/ч 00001'
        data['position'] = 'Офицер отдела'
        data['mobile_number'] = '+7(999)199-77-55'
        data['phone_number'] = '13-37'
        data['personal_business'] = '1523'
        data["date_of_join"] = '2018'
        data['contract_from'] = '25.06.2019'
        data['contract_type'] = 'на 5 лет'
        data['contract_order'] = 'МО №625'
        data['contract_ord_data'] = '29.06.2019'
        data['allowance_form'] = 'Первая'
        data['allowance_num'] = 'Ю/55/6414'
        data['allowance_data'] = '24.09.18'

        self.db.insert(data)

        self.menubar = QtWidgets.QMenuBar()
        file_menu = self.menubar.addMenu('Файл')

        self.central_widget = QtWidgets.QWidget()
        self.splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        self.hbox = QtWidgets.QHBoxLayout()
        self.person_widget = PersonWidget(None)

        self.scroll_area = QtWidgets.QScrollArea()
        self.doc_widget = QtWidgets.QWidget()
        self.doc_layout = QtWidgets.QVBoxLayout(self.doc_widget)
        self.doc_layout.setAlignment(QtCore.Qt.AlignTop)
        self.doc_layout.setAlignment(QtCore.Qt.AlignHCenter)
        self.doc_widget.setLayout(self.doc_layout)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.doc_widget)

        self.scroll_area.hide()

        hbox = QtWidgets.QHBoxLayout()
        wid = QtWidgets.QLabel(f'Свидетельство о рождении')
        pixmap = QtGui.QPixmap(f'1.jpg')
        pixmap = pixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
        wid.setPixmap(pixmap)
        hbox.addWidget(wid)
        hbox.addWidget(QtWidgets.QLabel(f'Свидетельство о рождении'))
        self.doc_layout.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        wid = QtWidgets.QLabel(f'Паспорт')
        pixmap = QtGui.QPixmap(f'2.jpg')
        pixmap = pixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
        wid.setPixmap(pixmap)
        hbox.addWidget(wid)
        hbox.addWidget(QtWidgets.QLabel(f'Паспорт'))
        self.doc_layout.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        wid = QtWidgets.QLabel(f'Свидетельство о браке')
        pixmap = QtGui.QPixmap(f'3.jpg')
        pixmap = pixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
        wid.setPixmap(pixmap)
        hbox.addWidget(wid)
        hbox.addWidget(QtWidgets.QLabel(f'Свидетельство о браке'))
        self.doc_layout.addLayout(hbox)

        self.list = QtWidgets.QListWidget()
        list_items = dict()
        persons = self.db.execute('SELECT profile_ID, surname, name, patr FROM persons ORDER BY surname')
        for line in persons:
            text = f'{line[1]} {line[2][0]}.{line[3][0]}.'
            list_items[text] = line[0]
            self.list.addItem(QtWidgets.QListWidgetItem(text))
        self.list.setMaximumWidth(200)

        self.list.itemClicked.connect(lambda: self.chose_person(list_items[self.list.currentItem().text()]))

        self.splitter.addWidget(self.list)
        self.splitter.addWidget(self.person_widget)
        self.splitter.addWidget(self.scroll_area)
        self.hbox.addWidget(self.splitter)
        self.central_widget.setLayout(self.hbox)

        self.statusbar = QtWidgets.QStatusBar()

        self.setCentralWidget(self.central_widget)
        self.setMenuBar(self.menubar)
        self.setStatusBar(self.statusbar)

    def chose_person(self, id):
        data = self.db.get_data(id)
        self.splitter.replaceWidget(1, PersonWidget(data[0]))
        self.scroll_area.show()


class InsertWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.resize(900, 400)
    window.show()

    sys.exit(app.exec_())
