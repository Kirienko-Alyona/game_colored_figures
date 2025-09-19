# levels.py

from settings import BLUE, YELLOW, PURPLE, GREEN, COLORS

# Конфігурації для кожного рівня
LEVEL_CONFIGS = {
    1: {
        'name': 'Перший крок',
        'description': 'Збери 10 кіл, щоб навчитися грати.',
        "square_color": BLUE,
        "change_square_color": False,
        "win_score": 3,
        "circle_speed": 5,
        "circle_color": GREEN,
        # "figure_type": CIRCLE,
    },
    2: {
        'name': 'Зміна кольорів',
        'description': 'Колір квадрата буде змінюватись. Будь уважний!',
        "square_color": "random",
        "change_square_color": True,
        "win_score": 3,
        "circle_speed": 6,
    },
    3: {
        'name': 'Прискорюйся!',
        'description': 'Кола падають значно швидше. Не втрачай концентрацію.',
        "square_color": "random",
        "change_square_color": True,
        "win_score": 3,
        "circle_speed": 7,
    },
    4: {
        'name': 'Етап 4',
        'description': 'Текст завдання',
        "square_color": "random",
        "change_square_color": True,
        "win_score": 3,
        "circle_speed": 8,
    },
    5: {
        'name': 'Етап 5',
        'description': 'Текст завдання',
        "square_color": "random",
        "change_square_color": True,
        "win_score": 3,
        "circle_speed": 9,
    },
    6: {
        'name': 'Етап 6',
        'description': 'Текст завдання',
        "square_color": "random",
        "change_square_color": True,
        "win_score": 3,
        "circle_speed": 10,
    },
    7: {
        'name': 'Етап 7',
        'description': 'Текст завдання',
        "square_color": "random",
        "change_square_color": True,
        "win_score": 3,
        "circle_speed": 11,
    },
    8: {
        'name': 'Етап 8',
        'description': 'Текст завдання',
        "square_color": "random",
        "change_square_color": True,
        "win_score": 3,
        "circle_speed": 12,
    },
    9: {
        'name': 'Етап 9',
        'description': 'Текст завдання',
        "square_color": "random",
        "change_square_color": True,
        "win_score": 3,
        "circle_speed": 13,
    },
    10: {
        'name': 'Етап 10',
        'description': 'Текст завдання',
        "square_color": "random",
        "change_square_color": True,
        "win_score": 3,
        "circle_speed": 14,
    },
}
