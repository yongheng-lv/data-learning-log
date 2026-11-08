def str_reverse(s):
    s = s[::-1]
    return s
def substr(s, x, y):
    s = s[x:y]
    return s
if __name__ == "__main__":
    print(str_reverse("我是吕永恒"))
    print(substr("我是吕永恒", 1, 4))