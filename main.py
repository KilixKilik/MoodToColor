import random

# маппинг настроений → HEX + ANSI escape-коды (RGB для терминала)
MOODS = {
    "радость": ("#FFD700", "\033[48;2;255;215;0m"),
    "грусть": ("#4682B4", "\033[48;2;70;130;180m"),
    "злость": ("#FF4500", "\033[48;2;255;69;0m"),
    "спокойствие": ("#ADFF2F", "\033[48;2;173;255;47m"),
    "страх": ("#2F4F4F", "\033[48;2;47;79;79m"),
    "любовь": ("#FF69B4", "\033[48;2;255;105;180m"),
    "хаос": ("#8A2BE2", "\033[48;2;138;43;226m"),
    "удивление": ("#FFA500", "\033[48;2;255;165;0m"),
    "скука": ("#A9A9A9", "\033[48;2;169;169;169m"),
    "надежда": ("#32CD32", "\033[48;2;50;205;50m"),
}

RESET = "\033[0m"  # сброс цвета


def feel_it(mood=None):
    """возвращает цвет по настроению или случайному настроению"""
    if not mood:
        mood = random.choice(list(MOODS.keys()))
    hex_code, ansi_bg = MOODS.get(mood, MOODS["скука"])  # fallback на "скука"
    return mood, hex_code, ansi_bg


def render_color_block(ansi_bg, size=8):
    """рисует цветной блок в терминале"""
    block = "█" * size
    print(f"{ansi_bg}{block}{RESET}")


def main():
    print("🎨 MoodToColor — введи настроение или оставь пустым для случайного:")
    user_input = input("> ").strip().lower()

    mood, hex_code, ansi_bg = feel_it(user_input if user_input else None)

    print(f"\nТвоё настроение: {mood}")
    print(f"🎨 HEX: {hex_code}")
    render_color_block(ansi_bg)


if __name__ == "__main__":
    main()  # запуск

# Github: @KilixKilik
