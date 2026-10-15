"""Питання 4-7: скільки пам'яті потребує секунда відео.

ЗМІНІТЬ WIDTH і HEIGHT на роздільну здатність свого дисплея.
"""
WIDTH = 1920       # ширина екрана в пікселях
HEIGHT = 1080      # висота екрана в пікселях
FPS = 22           # кадрів за секунду (за умовою)


def report(title, width, height, bytes_per_pixel):
    pixels = width * height                       # кількість пікселів у кадрі
    frame = pixels * bytes_per_pixel              # байтів в одному кадрі
    second = frame * FPS                          # байтів в одній секунді відео
    print(f"{title}: {width}x{height} = {pixels:,} пікселів; "
          f"кадр = {frame:,} Б; 1 с = {second:,} Б "
          f"= {second / 1000**2:.2f} МБ = {second / 1024**2:.2f} МіБ")
    return second


# RGB: 3 канали (R, G, B) по 1 байту (0..255) = 3 байти на піксель
rgb = report("Кольорове (RGB)", WIDTH, HEIGHT, 3)

# Градації сірого: 1 канал = 1 байт на піксель
gray = report("Чорно-біле (grey)", WIDTH, HEIGHT, 1)
print(f"Економія пам'яті: у {rgb / gray:.0f} рази\n")

# Відео на половину ширини і половину висоти екрана
half = report("Половина ширини і висоти, RGB", WIDTH // 2, HEIGHT // 2, 3)
print(f"Пам'яті потрібно в {rgb / half:.0f} рази менше (а не в 2)\n")


# Перетворення одного пікселя RGB -> grey (зважена сума каналів, ITU-R BT.601)
def to_gray(r, g, b):
    return round(0.299 * r + 0.587 * g + 0.114 * b)


print("Піксель (200, 100, 50) -> grey:", to_gray(200, 100, 50))
print("Простіший варіант - середнє:", round((200 + 100 + 50) / 3))
