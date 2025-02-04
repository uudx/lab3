def unique_elements(somelist):
    newlist = []
    for num in somelist:
        if num not in newlist:
            newlist.append(num)
    return newlist
