import random
import string

def generate_random_input(n, min_length, max_length, alphabet):
    S = []
    for i in range(n):
        l = random.randint(min_length, max_length)
        s = ''
        for j in range(l):
            c = random.choice(alphabet)
            s += c
        S.append(s)
    return S

# ************** MAIN ****************

for i in range(30):
    #numOfStr = random.randint(1, 10)
    strings = generate_random_input(i+1, 7, 7, "abcdefghijklmnopqrstuvwxyz")
    print("String list no {}:\n{}\nNumber of strings in this list: {}\n".format(i+1, strings, i+1))