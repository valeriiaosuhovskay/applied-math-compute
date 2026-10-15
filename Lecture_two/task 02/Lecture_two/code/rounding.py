"""Питання 2-3: округлення в Python та математичне округлення (0.5 -> вгору)."""
from decimal import Decimal, ROUND_HALF_UP

# Вбудований round() у Python 3 округлює до найближчого ПАРНОГО при рівній відстані
# ("банківське округлення", round half to even).
print("round(2.5) =", round(2.5))     # 2  (парне)
print("round(3.5) =", round(3.5))     # 4  (парне)
print("round(0.5) =", round(0.5))     # 0
print("round(1.5) =", round(1.5))     # 2
print("round(2.49) =", round(2.49))   # 2


def round_half_up(x, digits=0):
    """Математичне округлення: .5 завжди в більший за модулем бік.

    Рядок str(x) беремо, щоб Decimal працював з десятковим записом числа,
    а не з його двійковим наближенням (як-от 2.675 -> 2.67499999...).
    """
    q = Decimal(1).scaleb(-digits)               # крок округлення: 1, 0.1, 0.01 ...
    return Decimal(str(x)).quantize(q, rounding=ROUND_HALF_UP)


print()
for value in (2.5, 3.5, 2.49, 2.51, -2.5):
    print(f"round_half_up({value}) = {round_half_up(value)}")
print("round_half_up(2.675, 2) =", round_half_up(2.675, 2))
print("round(2.675, 2) =", round(2.675, 2), "(через двійкове представлення)")

# Простий варіант для додатних чисел:
import math
print("math.floor(2.5 + 0.5) =", math.floor(2.5 + 0.5))
