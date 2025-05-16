TILE_COLORS = {
    0: ("#CCC0B3", "#776E65"),
    2: ("#EEE4DA", "#776E65"),
    4: ("#EDE0C8", "#776E65"),
    8: ("#F2B179", "#F9F6F2"),
    16: ("#F59563", "#F9F6F2"),
    32: ("#F67C5F", "#F9F6F2"),
    64: ("#F65E3B", "#F9F6F2"),
    128: ("#EDCF72", "#F9F6F2"),
    256: ("#EDCC61", "#F9F6F2"),
    512: ("#EDC850", "#F9F6F2"),
    1024: ("#EDC53F", "#F9F6F2"),
    2048: ("#EDC22E", "#F9F6F2"),
}

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 650
GRID_SIZE = 4
TILE_SIZE = 90

TITLE_STYLE = """
    QLabel {
        color: #776E65;
        font-weight: bold;
        padding: 0px;
        margin: 0px;
    }
"""

DESCRIPTION_STYLE = """
    QLabel {
        color: #776E65;
        margin-top: -5px;
    }
"""

SCORE_STYLE = """
    QWidget {
        background: #BBADA0;
        border-radius: 6px;
        min-width: 95px;
        max-width: 95px;
        min-height: 60px;
        max-height: 60px;
        padding: 0px;
    }
    QLabel {
        background: transparent;
        padding: 0px;
        margin: 0px;
    }
    QLabel[accessibleName="label"] {
        color: #EEE4DA;
        font-size: 11px;
        letter-spacing: 1px;
        margin-top: -12px;
        margin-bottom: -4px;
    }
    QLabel[accessibleName="value"] {
        color: white;
        font-weight: bold;
        margin-top: -22px;
        margin-bottom: 8px;
    }
"""

GRID_STYLE = """
    QWidget {
        background: #BBADA0;
        border-radius: 6px;
    }
"""

WINDOW_STYLE = "background: #FAF8EF;" 