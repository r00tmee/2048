from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGridLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from game_logic import GameLogic
from constants import *

class Game2048(QWidget):
    def __init__(self):
        super().__init__()
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.game_logic = GameLogic(GRID_SIZE)
        self.tiles = [[QLabel() for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.layout.setSpacing(16)
        self.layout.setContentsMargins(20, 20, 20, 20)
        
        # Header
        self.header = QVBoxLayout()
        self.header.setSpacing(5)
        
        # Title and description
        title_container = QVBoxLayout()
        title_container.setSpacing(0)
        
        self.title = QLabel("2048")
        self.title.setFont(QFont("Arial", 52, QFont.Weight.Bold))
        self.title.setStyleSheet(TITLE_STYLE)
        self.title.setFixedHeight(65)
        
        self.description = QLabel("Joignez les nombres et obtenez 2048 !")
        self.description.setFont(QFont("Arial", 13))
        self.description.setStyleSheet(DESCRIPTION_STYLE)
        self.description.setFixedHeight(25)
        
        title_container.addWidget(self.title)
        title_container.addWidget(self.description)
        
        # Top bar avec titre et scores
        top_bar = QHBoxLayout()
        top_bar.setSpacing(10)
        
        # Scores container
        scores_container = QHBoxLayout()
        scores_container.setSpacing(5)
        
        # Current score
        self.score_container = QWidget()
        score_layout = QVBoxLayout(self.score_container)
        score_layout.setSpacing(0)
        score_layout.setContentsMargins(0, 0, 0, 0)
        score_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.score_label = QLabel("SCORE")
        self.score_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.score_label.setFont(QFont("Arial", 11))
        self.score_label.setAccessibleName("label")
        self.score_label.setFixedHeight(18)
        
        self.score_value = QLabel("0")
        self.score_value.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.score_value.setFont(QFont("Arial", 18))
        self.score_value.setAccessibleName("value")
        self.score_value.setFixedHeight(22)
        
        score_layout.addWidget(self.score_label)
        score_layout.addWidget(self.score_value)
        
        # Best score
        self.best_score_container = QWidget()
        best_score_layout = QVBoxLayout(self.best_score_container)
        best_score_layout.setSpacing(0)
        best_score_layout.setContentsMargins(0, 0, 0, 0)
        best_score_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.best_score_label = QLabel("MEILLEUR")
        self.best_score_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.best_score_label.setFont(QFont("Arial", 11))
        self.best_score_label.setAccessibleName("label")
        self.best_score_label.setFixedHeight(18)
        
        self.best_score_value = QLabel(str(self.game_logic.best_score))
        self.best_score_value.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.best_score_value.setFont(QFont("Arial", 18))
        self.best_score_value.setAccessibleName("value")
        self.best_score_value.setFixedHeight(22)
        
        best_score_layout.addWidget(self.best_score_label)
        best_score_layout.addWidget(self.best_score_value)
        
        self.score_container.setStyleSheet(SCORE_STYLE)
        self.best_score_container.setStyleSheet(SCORE_STYLE)
        
        scores_container.addWidget(self.score_container)
        scores_container.addWidget(self.best_score_container)
        
        top_bar.addLayout(title_container, stretch=1)
        top_bar.addLayout(scores_container)
        
        self.header.addLayout(top_bar)
        self.layout.addLayout(self.header)

        # Game grid
        self.game_container = QWidget()
        self.game_container.setStyleSheet(GRID_STYLE)
        self.gridLayout = QGridLayout(self.game_container)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                label = self.tiles[i][j]
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                label.setFixedSize(TILE_SIZE, TILE_SIZE)
                label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
                self.update_tile_style(label, 0)
                self.gridLayout.addWidget(label, i, j)

        self.layout.addWidget(self.game_container)
        self.setLayout(self.layout)
        self.update_ui()

    def update_tile_style(self, label, value):
        bg_color, text_color = TILE_COLORS.get(value, ("#CDC1B4", "#776E65"))
        font_size = "24px"
        if value > 512:
            font_size = "20px"
        if value > 1024:
            font_size = "18px"
            
        label.setStyleSheet(f"""
            QLabel {{
                background: {bg_color};
                color: {text_color};
                border-radius: 3px;
                font-size: {font_size};
            }}
        """)

    def keyPressEvent(self, event):
        moved = False
        if event.key() == Qt.Key.Key_Left:
            moved = self.game_logic.move_left()
        elif event.key() == Qt.Key.Key_Right:
            moved = self.game_logic.move_right()
        elif event.key() == Qt.Key.Key_Up:
            moved = self.game_logic.move_up()
        elif event.key() == Qt.Key.Key_Down:
            moved = self.game_logic.move_down()
        if moved:
            self.game_logic.add_random_tile()
            self.update_ui()

    def update_ui(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                value = self.game_logic.grid[i][j]
                self.tiles[i][j].setText(str(value) if value != 0 else "")
                self.update_tile_style(self.tiles[i][j], value)
        self.score_value.setText(str(self.game_logic.score))
        self.best_score_value.setText(str(self.game_logic.best_score)) 