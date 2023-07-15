from PyQt5 import QtCore, QtWidgets, QtGui


class PersonWidget(QtWidgets.QScrollArea):
    def __init__(self):
        super(PersonWidget, self).__init__()
        widget = QtWidgets.QWidget()
        main_layout = QtWidgets.QVBoxLayout(widget)
        main_layout.setAlignment(QtCore.Qt.AlignTop)

        data = dict()
        data['rank'] = '<b>Лейтенант</b>'
        data['surname'] = '<b>ИВАНОВ</b>'
        data['name'] = '<b>Иван</b>'
        data['patr'] = '<b>Иванович</b>'
        data['number'] = 'A-00000'
        data['birthday_date'] = '23.08.2000 (22 лет)'
        data['place_of_birth'] = 'г. Москва'
        data['nation'] = 'русский'
        data['family_status'] = 'женат'
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

        first_group = QtWidgets.QGroupBox('Персональные данные')
        first_level = QtWidgets.QHBoxLayout()
        self.img_label = QtWidgets.QLabel('')
        self.img_label.setStyleSheet('border: 1px solid #333')
        pixmap = QtGui.QPixmap('4.jpg')
        pixmap = pixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
        self.img_label.setPixmap(pixmap)
        self.img_label.setAlignment(QtCore.Qt.AlignCenter)

        p1 = QtWidgets.QVBoxLayout()
        p1.setAlignment(QtCore.Qt.AlignCenter)
        self.labels = dict()
        self.labels['person1'] = dict()
        self.labels['person1']['rank'] = QtWidgets.QLabel(data['rank'])
        self.labels['person1']['surname'] = QtWidgets.QLabel(data['surname'])
        self.labels['person1']['name'] = QtWidgets.QLabel(data['name'])
        self.labels['person1']['patr'] = QtWidgets.QLabel(data['patr'])

        for label in self.labels['person1'].keys():
            self.labels['person1'][label].setAlignment(QtCore.Qt.AlignCenter)
            p1.addWidget(self.labels['person1'][label])

        self.labels['person2'] = dict()
        self.labels['person2']['number'] = QtWidgets.QLabel(data['number'])
        self.labels['person2']['birthday_date'] = QtWidgets.QLabel(data['birthday_date'])
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
        passage_table.setHorizontalHeaderLabels(('Дата', 'Условное наименование', 'Должность'))
        passage_l.addWidget(passage_table)
        passage_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        passage_table.clicked.connect(self.open_passage)
        label = QtWidgets.QLabel(f'<b>Выслуга лет: {data["date_of_join"]}</b>')
        label.setAlignment(QtCore.Qt.AlignCenter)
        passage_l.addWidget(label)
        passage_gr.setLayout(passage_l)

        main_layout.addWidget(first_group)
        main_layout.addLayout(second_level)
        main_layout.addWidget(passage_gr)

        self.setWidget(widget)
        self.setWidgetResizable(True)

    def open_passage(self):
        pass


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.menubar = QtWidgets.QMenuBar()
        file_menu = self.menubar.addMenu('Файл')

        self.central_widget = QtWidgets.QWidget()
        self.splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        self.hbox = QtWidgets.QHBoxLayout()
        self.person_widget = PersonWidget()

        scroll_area = QtWidgets.QScrollArea()
        self.doc_widget = QtWidgets.QWidget()
        self.doc_layout = QtWidgets.QVBoxLayout(self.doc_widget)
        self.doc_layout.setAlignment(QtCore.Qt.AlignTop)
        self.doc_layout.setAlignment(QtCore.Qt.AlignHCenter)
        self.doc_widget.setLayout(self.doc_layout)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.doc_widget)

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
        self.list.addItem(QtWidgets.QListWidgetItem('л-т Иванов И.И.'))
        self.list.setMaximumWidth(200)

        self.splitter.addWidget(self.list)
        self.splitter.addWidget(self.person_widget)
        self.splitter.addWidget(scroll_area)
        self.hbox.addWidget(self.splitter)
        self.central_widget.setLayout(self.hbox)

        self.statusbar = QtWidgets.QStatusBar()

        self.setCentralWidget(self.central_widget)
        self.setMenuBar(self.menubar)
        self.setStatusBar(self.statusbar)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.resize(900, 400)
    window.show()

    sys.exit(app.exec_())
