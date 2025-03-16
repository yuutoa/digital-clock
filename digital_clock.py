import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtGui import QIcon


class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        #     Icon
        self.setWindowIcon(QIcon("static/icon_clock.png"))
        self.setWindowTitle("Digital Clock")
        self.setGeometry(900, 700, 1000, 200)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        # CSS Style Sheets
        self.time_label.setStyleSheet("font-size: 200px;" "color: #35A29F;")
        # Font Family
        font_id = QFontDatabase.addApplicationFont("static/DS-DIGI.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 200)
        self.time_label.setFont(my_font)

        # Application Background Color
        self.setStyleSheet("background-color: #26355D;")

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()


    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
