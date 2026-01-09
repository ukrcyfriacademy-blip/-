import turtle as t

def triangle(length):
    for _ in range(3):
        t.forward(length)
        t.left(120)

def sierpinski_triangle(length, level):
    if level == 0:
        triangle(length)
    else:
        sierpinski_triangle(length / 2, level - 1)
        t.forward(length / 2)
        sierpinski_triangle(length / 2, level - 1)
        t.backward(length / 2)
        t.left(60)
        t.forward(length / 2)
        t.right(60)
        sierpinski_triangle(length / 2, level - 1)
        t.left(60)
        t.backward(length / 2)
        t.right(60)


if __name__ == "__main__":
    triangle(200)
    sierpinski_triangle(50,100)
    t.done()