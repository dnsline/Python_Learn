num = 100
while num > 0:
    print(num)
    if num == 50:
        print("break here because num == %s" % num)
        break
    num -= 1
