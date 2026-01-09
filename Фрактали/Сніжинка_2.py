import turtle as t


def snowflake(level, length):
    if level == 0:
        t.forward(length/3)
        t.backward(length/3)
        return

    for _ in range(6):
        t.forward(length)           # рух до кінця гілки
        snowflake(level - 1, length/3) # рекурсія далі назовні
        t.backward(length)          # повернення    
        t.right(60)



if __name__ == "__main__":
    t.speed(0)
    snowflake(4, 200)
    t.done()