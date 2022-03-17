from PyQt5 import QtWidgets, QtCore, QtGui
from ui import Window


class Settings(Window):
    """Настройка графического инфтерфейса"""
    def __init__(self):
        super(Settings, self).__init__()
        self.style_sheet = "font: 14pt \"Times New Roman\";"  # Размер и шрифт текста
        self.header_list = ["Улица", "Дом", "Место", "TKD", "IP", "Примечание"]  # Названия хедера таблицы
        self.width_header = [250, 100, 160, 125, 125, 395]  # Размеры столбцов хедера

        self.set_settings_main_window()  # Настройки главного окна
        self.set_settings_combo_boxes()  # Настройки комбобокса
        self.set_settings_line_edits()  # Настройки поля ввода
        self.set_settings_buttons()  # Настрока кнопок
        self.set_settings_table_widget()  # Настройка таблицы

    def set_settings_main_window(self):
        """Найстройка главного окна"""
        self.resize(1200, 700)
        self.setWindowTitle("SearchInDB")
        self.setWindowIcon(QtGui.QIcon("Icons/main.ico"))

    def set_settings_combo_boxes(self):
        """Настройка поля Список"""
        self.combo_box.setMinimumSize(30, 30)
        self.combo_box.setStyleSheet(self.style_sheet)
        self.combo_box.setToolTip("Выберете раздел поиска")

        for i in ["Улица", "TKD", "IP"]:
            self.combo_box.addItem(i)

    def set_settings_line_edits(self):
        """Настройка поля Ввода"""
        self.line_edit.setMinimumSize(QtCore.QSize(0, 30))
        self.line_edit.setStyleSheet(self.style_sheet)
        self.line_edit.setToolTip("Введите значение")

    def set_settings_buttons(self):
        """Настройка кнопок"""
        self.search_button.setIcon(QtGui.QIcon("Icons/search.ico"))
        self.search_button.setToolTip("Поиск")

        self.add_button.setIcon(QtGui.QIcon("Icons/add.ico"))
        self.add_button.setToolTip("Добавить строку")

        self.del_button.setIcon(QtGui.QIcon("Icons/del.ico"))
        self.del_button.setToolTip("Удалить строку")

        self.save_button.setIcon(QtGui.QIcon("Icons/save.ico"))
        self.save_button.setToolTip("Сохранить")

        for i in [self.search_button, self.add_button, self.del_button, self.save_button]:
            i.setMinimumSize(33, 32)
            i.setStyleSheet(self.style_sheet)
            i.setToolTipDuration(3000)

    def set_settings_table_widget(self):
        """Настройка таблицы"""
        self.table_widget.setColumnCount(len(self.header_list))
        self.table_widget.setHorizontalHeaderLabels(self.header_list)
        self.table_widget.setStyleSheet(self.style_sheet)
        self.table_widget.verticalHeader().setVisible(False)
        self.table_widget.setSortingEnabled(True)
        self.table_widget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_widget.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)

        for i, j in zip(self.header_list, self.width_header):
            self.table_widget.setColumnWidth(self.header_list.index(i), j)
