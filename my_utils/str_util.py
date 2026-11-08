def str_reverse(s):
    s = s[::-1]
    print(s)
def substr(s, x, y):
    my_list = s.split(s[x],s[y])
    print(my_list)
str_reverse("hello")
substr("我叫吕永恒", 1, 3)