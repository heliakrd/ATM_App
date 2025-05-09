import sys

from PyQt6.QtWidgets import (
    QApplication, QWidget, QGridLayout, QPushButton, QLineEdit, QLabel,
    QStackedWidget, QVBoxLayout, QHBoxLayout, QMessageBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFont, QIntValidator


class LoginPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        layout = QGridLayout(self)

        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        layout.addWidget(QLabel('Username:'), 0, 0)
        layout.addWidget(self.username_input, 0, 1)
        layout.addWidget(QLabel('Password:'), 1, 0)
        layout.addWidget(self.password_input, 1, 1)

        login_btn = QPushButton('Log in')
        login_btn.clicked.connect(self.login)

        close_btn = QPushButton('Close')
        close_btn.clicked.connect(QApplication.instance().quit)

        layout.addWidget(login_btn, 2, 0, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addWidget(close_btn, 2, 1, alignment=Qt.AlignmentFlag.AlignRight)

    def login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Invalid Entry", "Please fill in both username and password.")
            return

        self.stacked_widget.setCurrentIndex(1)


class LanguagePage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        main_layout = QVBoxLayout(self)

        label = QLabel("Choose your language")
        font = QFont("Verdana", 16)
        font.setBold(True)
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(label)

        button_layout = QHBoxLayout()

        english_btn = QPushButton("English")
        persian_btn = QPushButton("فارسی")

        english_btn.setFixedSize(120, 40)
        persian_btn.setFixedSize(120, 40)

        english_btn.clicked.connect(self.go_to_main_menu)
        persian_btn.clicked.connect(self.go_to_main_menu)

        button_layout.addWidget(english_btn, alignment=Qt.AlignmentFlag.AlignLeft)
        button_layout.addWidget(persian_btn, alignment=Qt.AlignmentFlag.AlignRight)

        main_layout.addLayout(button_layout)

    def go_to_main_menu(self):
        self.stacked_widget.setCurrentIndex(2)

class MainAtm(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        layout = QVBoxLayout()
        self.setLayout(layout)

        top_buttons_layout = QHBoxLayout()

        btn1 = QPushButton('Get Cash')
        btn1.setFixedSize(120, 40)
        btn1.clicked.connect(self.go_to_get_cash_page)
        top_buttons_layout.addWidget(btn1, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        btn2 = QPushButton('Change Password')
        btn2.setFixedSize(120, 40)
        btn2.clicked.connect(self.go_to_change_password_page)
        top_buttons_layout.addWidget(btn2, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)

        bottom_buttons_layout = QHBoxLayout()

        btn3 = QPushButton('Money Transfer')
        btn3.setFixedSize(120, 40)
        btn3.clicked.connect(self.go_to_money_transfer_page)
        bottom_buttons_layout.addWidget(btn3, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft)

        btn4 = QPushButton('Account Balance')
        btn4.setFixedSize(120, 40)
        btn4.clicked.connect(self.go_to_account_balance_page)
        bottom_buttons_layout.addWidget(btn4, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight)

        layout.addLayout(top_buttons_layout)
        layout.addLayout(bottom_buttons_layout)

    def go_to_get_cash_page(self):
        self.stacked_widget.setCurrentIndex(3)

    def go_to_change_password_page(self):
        self.stacked_widget.setCurrentIndex(5)

    def go_to_money_transfer_page(self):
        self.stacked_widget.setCurrentIndex(6)

    def go_to_account_balance_page(self):
        self.stacked_widget.setCurrentIndex(7)

class GetCash(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        layout = QVBoxLayout()
        self.setLayout(layout)

        top_buttons_layout = QHBoxLayout()
        bottom_buttons_layout = QHBoxLayout()

        amounts = ['500,000', '1,500,000', '2,000,000', '2,500,000']
        for i, amount in enumerate(amounts):
            btn = QPushButton(amount)
            btn.setFixedSize(120, 40)
            btn.clicked.connect(self.go_to_done_page)
            if i < 2:
                top_buttons_layout.addWidget(btn)
            else:
                bottom_buttons_layout.addWidget(btn)

        layout.addLayout(top_buttons_layout)
        layout.addLayout(bottom_buttons_layout)

    def go_to_done_page(self):
        self.stacked_widget.setCurrentIndex(4)


class DonePage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel('Mission Accomplished successfully!')
        label.setFont(QFont("Tahoma", 14, QFont.Weight.Bold))
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(label)

        button1_layout = QHBoxLayout()

        bye_btn = QPushButton("Good Bye")
        new_btn = QPushButton("New Mission")

        bye_btn.setFixedSize(120, 40)
        new_btn.setFixedSize(120, 40)

        bye_btn.clicked.connect(QApplication.instance().quit)
        new_btn.clicked.connect(self.go_to_main_menu)

        button1_layout.addWidget(bye_btn, alignment=Qt.AlignmentFlag.AlignLeft)
        button1_layout.addWidget(new_btn, alignment=Qt.AlignmentFlag.AlignRight)

        layout.addLayout(button1_layout)

    def go_to_main_menu(self):
        self.stacked_widget.setCurrentIndex(2)

class ChangePassword(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()

        self.stacked_widget = stacked_widget

        layout = QGridLayout()
        self.setLayout(layout)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        layout.addWidget(QLabel('Enter your new password:'), 0, 0)
        layout.addWidget(self.password_input, 0, 1)


        c_btn = QPushButton('Confirm')
        c_btn.setFixedSize(120, 40)
        c_btn.clicked.connect(self.go_to_main_menue)

        layout.addWidget(c_btn, 1, 0, alignment=Qt.AlignmentFlag.AlignCenter)

    def go_to_main_menue(self):
        self.stacked_widget.setCurrentIndex(2)

class MoneyTransfer(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.card_input = QLineEdit()
        self.card_input.setPlaceholderText("Destination card number")
        self.card_input.setMaxLength(16)


        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Amount to transfer")
        self.amount_input.setValidator(QIntValidator())

        layout.addWidget(QLabel("Enter destination card number:"))
        layout.addWidget(self.card_input)

        layout.addWidget(QLabel("Enter amount to transfer:"))
        layout.addWidget(self.amount_input)

        button_layout = QHBoxLayout()

        back_button = QPushButton('Back to menu')
        back_button.setFixedSize(120, 40)
        back_button.clicked.connect(self.go_to_main_menu)

        confirm_btn = QPushButton("Confirm")
        confirm_btn.setFixedSize(120, 40)
        confirm_btn.clicked.connect(self.transfer_money)

        button_layout.addWidget(back_button)
        button_layout.addWidget(confirm_btn)

        layout.addLayout(button_layout)


    def transfer_money(self):
        card = self.card_input.text().strip()
        amount = self.amount_input.text().strip()

        if not card or not amount:
            QMessageBox.warning(self, "Invalid Entry", "Please fill in both fields.")
            return

        if len(card) != 16 or not card.isdigit():
            QMessageBox.warning(self, "Invalid Card", "Card number must be 16 digits.")
            return

        if int(amount) <= 0:
            QMessageBox.warning(self, "Invalid Amount", "Amount must be greater than zero.")
            return

        QMessageBox.information(self, "Success", f"{amount} Rials transferred to card {card}.")

    def go_to_main_menu(self):
        self.stacked_widget.setCurrentIndex(2)

class AccountBalance(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel("Account Balance")
        label.setFont(QFont("Tahoma", 16, QFont.Weight.Bold))
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        balance_label = QLabel("Your current balance is:")
        balance_value = QLabel("10,000,000 Rials")

        balance_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        balance_value.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(balance_label)
        layout.addWidget(balance_value)

        confirm_button = QPushButton('Confirm')
        confirm_button.setFixedSize(120, 40)
        confirm_button.clicked.connect(QApplication.instance().quit)
        layout.addWidget(confirm_button, alignment=Qt.AlignmentFlag.AlignCenter)

    def set_language(self, translations: dict):
        self.label_title.setText(translations["account_balance_title"])
        self.label_balance.setText(translations["account_balance_text"])
        self.button_back.setText(translations["back_button"])


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ATM")
        self.setWindowIcon(QIcon("atm.png"))
        self.resize(500, 400)

        self.stacked_widget = QStackedWidget()

        self.login_page = LoginPage(self.stacked_widget)
        self.language_page = LanguagePage(self.stacked_widget)
        self.main_atm_page = MainAtm(self.stacked_widget)
        self.get_cash_page = GetCash(self.stacked_widget)
        self.done_page = DonePage(self.stacked_widget)
        self.change_password_page = ChangePassword(self.stacked_widget)
        self.money_transfer_page = MoneyTransfer(self.stacked_widget)
        self.account_balance_page = AccountBalance(self.stacked_widget)

        self.stacked_widget.addWidget(self.login_page)
        self.stacked_widget.addWidget(self.language_page)
        self.stacked_widget.addWidget(self.main_atm_page)
        self.stacked_widget.addWidget(self.get_cash_page)
        self.stacked_widget.addWidget(self.done_page)
        self.stacked_widget.addWidget(self.change_password_page)
        self.stacked_widget.addWidget(self.money_transfer_page)
        self.stacked_widget.addWidget(self.account_balance_page)

        self.back_btn = QPushButton()
        self.back_btn.setIcon(QIcon('back.png'))
        self.back_btn.setFixedSize(40, 30)
        self.back_btn.clicked.connect(self.go_previous)

        self.forward_btn = QPushButton()
        self.forward_btn.setIcon(QIcon('forward.png'))
        self.forward_btn.setFixedSize(40, 30)
        self.forward_btn.clicked.connect(self.go_next)

        nav_layout = QHBoxLayout()
        nav_layout.addWidget(self.back_btn)
        nav_layout.addWidget(self.forward_btn)
        nav_layout.addStretch()

        main_layout = QVBoxLayout(self)
        main_layout.addLayout(nav_layout)
        main_layout.addWidget(self.stacked_widget)

    def go_previous(self):
        index = self.stacked_widget.currentIndex()
        if index > 0:
            self.stacked_widget.setCurrentIndex(index - 1)

    def go_next(self):
        index = self.stacked_widget.currentIndex()
        if index < self.stacked_widget.count() - 1:
            self.stacked_widget.setCurrentIndex(index + 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())