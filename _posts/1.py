S = [0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0]

binary = []
length = len(S)

for i in range(0,length):

    if S[i].isupper():
        x = ord(S[i])-65
    elif S[i].islower():
        x = ord(S[i])-71
    elif S[i]=='+':
        x = 62
    elif S[i]=='/':
        x=63
    else:
        x = ord(S[i])+4
            
    temp = []
    while (x > 0):
        temp.append(0 if x % 2 == 0 else 1)
        x = int(x / 2)
    while (len(temp) < 6):
        temp.append(0)
    temp.reverse()
    binary = [*binary,*temp]
