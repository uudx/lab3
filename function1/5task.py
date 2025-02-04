def permute(s, l, r):
    if l == r:
        print("".join(s))
    else:
        for i in range(l, r + 1):
            s[l], s[i] = s[i], s[l]
            permute(s, l + 1, r)
            s[l], s[i] = s[i], s[l] 

def print_permutations(string):
    permute(list(string), 0, len(string) - 1)

user_input = input()
print_permutations(user_input)
