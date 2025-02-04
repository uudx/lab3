def spy_game(somelist):
    fzero = True
    szero = False
    seven = False
    i = 0
    for num in somelist:
        if num == 0 and fzero == True:
            fzero , szero = szero, fzero
        if num == 0 and szero == True:
            szero, seven = seven, szero
        if num == 7 and seven == True:
            return True
        if i == len(somelist)-1:
            return False
            break
        i += 1

print(spy_game([1,2,4,0,0,7,5]))
