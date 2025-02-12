import random

from colorama import init
init()

w = 25
n = w ** 2
bytesLen = len(str(n)) + 1

snail = ["0"+" "*(bytesLen-1)] * n
count = 0
direction = "r"
rshift = 1
x = -1
y = 0

stepColor = max(256*2 // n, 1)
stepBlue = 0
stepRed = 0
stepGreen = 0
while True:
    count += 1
    if direction == "r":
        x += 1
    elif direction == "l":
        x -= 1
    elif direction == "u":
        y -= 1
    elif direction == "d":
        y += 1

    index = x + y * w
    if index + 1 > n:
        break
    r, g, b = (33, 77, 33)
    if n // 3 < count < n*2 // 3:
        stepBlue += stepColor
        # stepGreen -= stepColor
    elif count > n * 2 // 3:
        stepRed += stepColor
        # stepBlue -= stepColor
    else:
        stepGreen += stepColor

    if count > n * 4 // 5:
        stepBlue -= stepColor
        stepGreen -= stepColor * 2

    r += stepRed
    g += stepGreen
    b += stepBlue
    if count == n:
        r = 255
        g = 60
        b = 80
    addColor = f"\x1b[38;2;{min(r, 255)};{min(g, 255)};{min(b, 255)}m"

    snail[index] = f"{addColor}{str(count)}{" "*(bytesLen - len(str(count)))}"
    if count == n:
        break
    elif x + y == w - 1 and x >= w / 2:
        direction = "d"
    elif x == y and x >= w / 2:
        direction = "l"
    elif x + y == w - 1 and x < w / 2:
        direction = "u"
    elif x + 1 == y and x < w / 2 - 1:
        direction = "r"


for i in range(0, n, w):
    row = snail[i:i+w]
    for cell in row:
        print(cell, end="")
    print()
