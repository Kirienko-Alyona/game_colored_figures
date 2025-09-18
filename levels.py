# levels.py

from settings import BLUE, YELLOW, PURPLE, GREEN, COLORS

# Конфігурації для кожного рівня
LEVEL_CONFIGS = {
    1: {
        "square_color": BLUE,
        "change_square_color": False,
        "win_score": 3,
        "circle_speed": 5,
    },
    2: {
        "square_color": "random",
        "change_square_color": True,
        "win_score": 3,
        "circle_speed": 7,
    },
    3: {
        "square_color": "random",
        "change_square_color": True,
        "win_score": 3,
        "circle_speed": 9,
    }
}
