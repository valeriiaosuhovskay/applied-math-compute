"""Завдання 2: зображення - це матриця чисел.

Змінюйте тільки row, col і value (та figsize для експерименту 4).
"""
import numpy as np
import matplotlib.pyplot as plt

# Матриця 4 рядки x 6 стовпців. Кожне число - яскравість одного пікселя:
# 0 = чорний, 255 = білий. Тип uint8 = 1 байт на елемент (значення 0..255).
G = np.array([
    [ 0, 40,  80, 120, 160, 200],
    [20, 60, 100, 140, 180, 220],
    [30, 70, 110, 150, 190, 230],
    [50, 90, 130, 170, 210, 250]
], dtype=np.uint8)

# Параметри експерименту: G[row, col] - спочатку рядок (згори вниз), потім стовпець (зліва направо).
row = 1
col = 4
value = 0

# Перевірки, щоб не вийти за межі матриці та діапазон uint8
if not (0 <= row < G.shape[0] and 0 <= col < G.shape[1]):
    raise ValueError("Індекс виходить за межі матриці")
if not 0 <= value <= 255:
    raise ValueError("Яскравість має бути від 0 до 255")

# Копія, щоб оригінал G залишався незмінним для порівняння
changed = G.copy()
changed[row, col] = value

print("Початкова матриця:\n", G)
print("Змінена матриця:\n", changed)
print("Форма:", G.shape)                 # (4, 6) - рядки, стовпці
print("Тип елементів:", G.dtype)         # uint8
print("Кількість пікселів:", G.size)     # 24
print("Обсяг даних пікселів:", G.nbytes, "байтів")  # 24 (по 1 байту на піксель)

# Два зображення поруч: оригінал і змінене
fig, axes = plt.subplots(1, 2, figsize=(9, 4))   # figsize - лише розмір вікна, не даних

for ax, data, title in zip(axes, [G, changed], ["Початкове зображення", "Після зміни"]):
    ax.imshow(
        data,
        cmap="gray",             # відтінки сірого
        vmin=0, vmax=255,        # фіксована шкала яскравості: 0 чорний, 255 білий
        interpolation="nearest", # без згладжування: кожен піксель - окремий квадрат
        origin="upper"           # рядок 0 зверху
    )
    ax.set_xticks(range(data.shape[1]))
    ax.set_yticks(range(data.shape[0]))
    ax.set_xlabel("Стовпець")
    ax.set_ylabel("Рядок")
    ax.set_title(title)

plt.tight_layout()
plt.show()
