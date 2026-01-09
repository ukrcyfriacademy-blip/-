import turtle as t
angle = 60



def koch(level, length):
    if level == 0:
        t.forward(length)
        
    else:
        length /= 3
        koch(level-1, length)
        t.left(angle)
        koch(level-1, length)
        t.right(2 * angle)
        koch(level-1, length)
        t.left(angle)
        koch(level-1, length)
    # t.right(2 * angle)


if __name__ == "__main__":
    t.speed(0)
    koch(2, 60)
    t.done()