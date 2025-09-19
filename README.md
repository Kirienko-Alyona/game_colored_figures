# game_colored_figures
Game with colored figures.

типова структура файлів
game/
│
├─ main.py            # точка входу
├─ settings.py        # константи та налаштування
├─ sprites.py         # класи спрайтів
├─ levels.py          # рівні, карти
├─ states/            # сцени/стани гри
│   ├─ menu.py
│   ├─ gameplay.py
│   └─ gameover.py
├─ assets/
│   ├─ images/
│   ├─ sounds/
│   └─ fonts/


7. Патерни проектування, що часто використовуються

Singleton – для менеджера ресурсів або налаштувань.

State – для керування станами гри.

Observer / Event system – для реакції на події (збільшення очок, втрата життя).

Component-based – для складних об’єктів, розділення поведінки на компоненти (фізика, AI, рендер).


-- ЗАПУСТИТИ pygbag - створиться нова компіляція
    pygbag C:\Users\Lenovo\Documents\Python-web\game_colored_figures

-- ЗУПИНИТИ pygbag
    ctrl+c
    