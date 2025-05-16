from PyQt6.QtWidgets import QApplication, QMainWindow
from game_widget import Game2048
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_STYLE
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("2048")
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setStyleSheet(WINDOW_STYLE)
        self.game_widget = Game2048()
        self.setCentralWidget(self.game_widget)
        self.game_widget.setFocus()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
