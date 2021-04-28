def add_it_up(a):
    if type(a) != int:
        return 0
    s = 0
    for i in range(1, a + 1):
        s += i
    return s
# a = 96 , z = 122


print(add_it_up(12))
print(add_it_up('12'))



