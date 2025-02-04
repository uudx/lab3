def has_33(somelist):
    count = 0
    prenum = somelist[0]
    for num in somelist:
        if num == 3:
            if num == prenum:
                count +=1
        prenum = num
    if count >= 1:
        return True
    else:
        return False
print(has_33([1,3,3,3]))
