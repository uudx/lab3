def is_palindrome(string):
    if len(string)%2 == 0:
        return (f"{string} is polindrome" if string[0:int((len(string)/2))] == string[(int(len(string)/2)) : int(len(string))][::-1] else f"{string} is not palindrome")
    else:
        return (f"{string} is polindrome" if string[0:int(((len(string)-1)/2))] == string[int(((len(string)+1)/2)) : int(len(string))][::-1] else f"{string} is not palindrome")
print(is_palindrome(input()))
