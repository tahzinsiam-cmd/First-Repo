st = input("Enter your message:")
words = st.split(" ")

nwords =[]

coding = True
if coding:
    for word in words:
        if(len(word)>=3):
            r1 = 'dsh '
            r2 = 'def'
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
            print(" ".join(nwords))
        else:
            nwords.append(word[::-1])


else:
     for word in words:
        if(len(word)>=3):
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])

print(" ".join(nwords))
