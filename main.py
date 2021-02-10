from tkinter import *


def main():

    chips = [[0 for j in range(8)]  for i in range(8)] + [False]

    window = Tk()
    window.title("Reversi")

    canvas = Canvas(window, width=810, height=810)
    button = Button(window, text="Restart", command=lambda: Restart(canvas, chips, window))
    canvas.pack()
    button.pack()

    canvas.bind('<Button-1>', lambda event : MousePress(event, canvas, chips, window))

    Restart(canvas, chips, window)

    window.mainloop()


def Restart(canvas, chips, window):
    chips[8] = False

    for i in range(8):
        for j in range(8):
            chips[i][j] = 0
    chips[3][3] = chips[4][4] = 1
    chips[3][4] = chips[4][3] = 2
    chips[2][3] = chips[3][2] = chips[4][5] = chips[5][4] = 3

    children = window.winfo_children()
    for i in children:
        if str(type(i)) == "<class 'tkinter.Label'>":
            i.destroy()

    draw(canvas, chips)


def MousePress(event, canvas, chips, window):

    if event.x < 0 or event.x >= 800 or event.y < 0 or event.y >= 800:
        return

    x, y = event.x // 100, event.y // 100

    if chips[x][y] == 3:
        chips[x][y] = 2 - chips[8]
        chips[8] = not chips[8]

        for i in range(8):
            for j in range(8):
                if chips[i][j] == 3:
                    chips[i][j] = 0

        flip(chips, x, y)
        if not find_move(chips):
            chips[8] != chips[8]
            if not find_move(chips):
                game_over(canvas, chips, window)

    draw(canvas, chips)


def find_move(chips):
    res = False
    for i in range(8):
        for j in range(8):
            if chips[i][j] == 2 - chips[8]:
                x, y = i + 1, j
                one = False
                while  x < 8 and chips[x][y] == 1 + chips[8]:
                    one = True
                    x += 1
                if one and x < 8 and chips[x][y] == 0:
                    res = True
                    chips[x][y] = 3

                x, y = i - 1, j
                one = False
                while  x >= 0 and chips[x][y] == 1 + chips[8]:
                    one = True
                    x -= 1
                if one and x >= 0 and chips[x][y] == 0:
                    res = True
                    chips[x][y] = 3

                x, y = i, j + 1
                one = False
                while  y < 8 and chips[x][y] == 1 + chips[8]:
                    one = True
                    y += 1
                if one and y < 8 and chips[x][y] == 0:
                    res = True
                    chips[x][y] = 3

                x, y = i, j - 1
                one = False
                while  y >= 0 and chips[x][y] == 1 + chips[8]:
                    one = True
                    y -= 1
                if one and y >= 0 and chips[x][y] == 0:
                    res = True
                    chips[x][y] = 3

                x, y = i + 1, j + 1
                one = False
                while  y < 8 and x < 8 and chips[x][y] == 1 + chips[8]:
                    one = True
                    y += 1
                    x += 1
                if one and y < 8 and x < 8 and chips[x][y] == 0:
                    res = True
                    chips[x][y] = 3

                x, y = i + 1, j - 1
                one = False
                while  y >= 0 and x < 8 and chips[x][y] == 1 + chips[8]:
                    one = True
                    y -= 1
                    x += 1
                if one and y >= 0 and x < 8 and chips[x][y] == 0:
                    res = True
                    chips[x][y] = 3

                x, y = i - 1, j + 1
                one = False
                while  x >= 0 and y < 8 and chips[x][y] == 1 + chips[8]:
                    one = True
                    x -= 1
                    y += 1
                if one and y < 8 and x >= 0 and chips[x][y] == 0:
                    res = True
                    chips[x][y] = 3

                x, y = i - 1, j - 1
                one = False
                while  y >= 0 and x >= 0 and chips[x][y] == 1 + chips[8]:
                    one = True
                    y -= 1
                    x -= 1
                if one and y >= 0 and x >= 0 and chips[x][y] == 0:
                    res = True
                    chips[x][y] = 3
    return res


def flip(chips, x, y):

    t, change = [], []

    x1, y1 = x - 1, y
    while x1 >= 0 and chips[x1][y1] == 2 - chips[8]:
        t.append([x1, y1])
        x1 -= 1
    if x1 >= 0 and chips[x1][y1] == 1 + chips[8]:
        change += t
    t = []

    x1, y1 = x + 1, y
    while x1 < 8 and chips[x1][y1] == 2 - chips[8]:
        t.append([x1, y1])
        x1 += 1
    if x1 < 8 and chips[x1][y1] == 1 + chips[8]:
        change += t
    t = []

    x1, y1 = x, y - 1
    while y1 >= 0 and chips[x1][y1] == 2 - chips[8]:
        t.append([x1, y1])
        y1 -= 1
    if y1 >= 0 and chips[x1][y1] == 1 + chips[8]:
        change += t
    t = []

    x1, y1 = x, y + 1
    while y1 < 8 and chips[x1][y1] == 2 - chips[8]:
        t.append([x1, y1])
        y1 += 1
    if y1 < 8 and chips[x1][y1] == 1 + chips[8]:
        change += t
    t = []

    x1, y1 = x + 1, y + 1
    while y1 < 8 and x1 < 8 and chips[x1][y1] == 2 - chips[8]:
        t.append([x1, y1])
        y1 += 1
        x1 += 1
    if y1 < 8 and x1 < 8 and chips[x1][y1] == 1 + chips[8]:
        change += t
    t = []

    x1, y1 = x - 1, y + 1
    while y1 < 8 and x1 >= 0 and chips[x1][y1] == 2 - chips[8]:
        t.append([x1, y1])
        y1 += 1
        x1 -= 1
    if y1 < 8 and x1 >= 0 and chips[x1][y1] == 1 + chips[8]:
        change += t
    t = []

    x1, y1 = x + 1, y - 1
    while y1 >= 0 and x1 < 8 and chips[x1][y1] == 2 - chips[8]:
        t.append([x1, y1])
        y1 -= 1
        x1 += 1
    if y1 >= 0 and x1 < 8 and chips[x1][y1] == 1 + chips[8]:
        change += t
    t = []

    x1, y1 = x - 1, y - 1
    while y1 >= 0 and x1 >= 0 and chips[x1][y1] == 2 - chips[8]:
        t.append([x1, y1])
        y1 -= 1
        x1 -= 1
    if y1 >= 0 and x1 >= 0 and chips[x1][y1] == 1 + chips[8]:
        change += t
    t = []

    for i in change:
        chips[i[0]][i[1]] = 1 + chips[8]


def draw(canvas, chips):
    canvas.delete("all")
    for i in range(8):
        for j in range(8):

            if chips[i][j] == 0:
                canvas.create_rectangle(i * 100 + 4, j * 100 + 4, (i + 1) * 100, (j + 1) * 100, fill='bisque2', width=3)
            if chips[i][j] == 1:
                canvas.create_rectangle(i * 100 + 4, j * 100 + 4, (i + 1) * 100, (j + 1) * 100, fill='bisque2', width=3)
                canvas.create_oval(i * 100 + 4 + 20, j * 100 + 4 + 20, (i + 1) * 100 - 20, (j + 1) * 100 - 20, fill='white', width=0)
            if chips[i][j] == 2:
                canvas.create_rectangle(i * 100 + 4, j * 100 + 4, (i + 1) * 100, (j + 1) * 100, fill='bisque2', width=3)
                canvas.create_oval(i * 100 + 4 + 20, j * 100 + 4 + 20, (i + 1) * 100 - 20, (j + 1) * 100 - 20, fill='black', width=0)
            if chips[i][j] == 3:
                canvas.create_rectangle(i * 100 + 4, j * 100 + 4, (i + 1) * 100, (j + 1) * 100, fill='bisque2', outline='gold', width=3)


def game_over(canvas, chips, window):
    b, w = 0, 0
    for i in range(8):
        for j in range(8):
            if chips[i][j] == 1:
                w += 1
            if chips[i][j] == 2:
                b += 1
    txt = "Ничья"
    if w > b:
        txt = "Победил игрок за белых"
    if b > w:
        txt = "Победил игрок за чёрных"
    label = Label(window, text=txt, fg="orange", font="Arial 30")
    label.pack()

if __name__ == "__main__":
    main()
