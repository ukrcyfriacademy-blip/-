import turtle as t
def draw_cantor(level, length):
    if level == 0:
        t.forward(length)
        return
    else:
        length/=2
        # Верхня лінія
        draw_cantor(level - 1, length)

        # Перехід на праву частину
        t.penup()
        t.forward(length)
        t.pendown()

        # Нижня лінія
        draw_cantor(level - 1, length)
        
if __name__ == "__main__":

    # Тестовий запуск (лише коли запускаємо цей файл напряму)
    draw_cantor(1, 120)
    t.done()