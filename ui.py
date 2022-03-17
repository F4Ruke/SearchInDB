from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):
    """Создание графического интерфейса"""
    def __init__(self):
        """Инициализация графического интерфейса"""
        super(Window, self).__init__()

        self.combo_box = QtWidgets.QComboBox()  # Создание комбобокса
        self.line_edit = QtWidgets.QLineEdit()  # Создание поля ввода

        h_layout_1 = QtWidgets.QHBoxLayout()  # Создание горизонтального лейаута
        for i in [self.combo_box, self.line_edit]:
            h_layout_1.addWidget(i)  # Добавление виджетов

        self.search_button = QtWidgets.QPushButton()  # Создание кнопки "Поиск"
        self.add_button = QtWidgets.QPushButton()  # Создание кнопки "Добавить"
        self.del_button = QtWidgets.QPushButton()  # Создание кнопки "Удалить"
        self.save_button = QtWidgets.QPushButton()  # Создание кнопки "Сохранить"

        h_layout_2 = QtWidgets.QHBoxLayout()  # Создание горизонтального лейаута
        for i in [self.search_button, self.save_button, self.add_button, self.del_button]:
            h_layout_2.addWidget(i)  # Добавление виджетов

        h_layout_3 = QtWidgets.QHBoxLayout()  # Создание горизонтального лейаута
        for i in [h_layout_1, h_layout_2]:
            h_layout_3.addLayout(i)  # Добавление лейаутов

        self.table_widget = QtWidgets.QTableWidget()  # Создание таблицы

        v_layout = QtWidgets.QVBoxLayout()  # Создание вертикального лейаута
        v_layout.addLayout(h_layout_3)  # Добавление лейатута
        v_layout.addWidget(self.table_widget)  # Добавление виджета

        self.setLayout(v_layout)  # Отображение вертикального лейаута
