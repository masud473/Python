# encoder
def encoder():
    sx = "kdx"
    sy = "ygu"
    lis = []
    sil = []

    rev = list(map(str, input("Enter word/sentence: ").split()))
    for word in rev:
        i = len(word) - 1
        reword = str()
        while 0 <= i <= (len(word) - 1):
            reword = reword + word[i]
            i -= 1
        sil.append(reword)

    for word in sil:
        if len(word) > 2:
            code = sx + word[1:] + word[0] + sy
            lis.append(code)
        elif len(word) == 2:
            code = sx + word[1] + word[0] + sy
            lis.append(code)
        elif len(word) == 1:
            code = sx + word + sy
            lis.append(code)
    for i in lis:
        print(i, end=" ")


# decoder
def decoder():
    sil = []
    lis = list(map(str, input().split()))
    for word in lis:
        code = word[3:-3]
        if len(code) > 2:
            dc = code[len(code) - 1] + code[0 : len(code) - 1]
            sil.append(dc)
        elif len(code) == 2:
            dc = code[1] + code[0]
            sil.append(dc)
        elif len(code) == 1:
            dc = code
            sil.append(dc)
    rev = []
    for word in sil:
        i = len(word) - 1
        reword = str()
        while 0 <= i <= (len(word) - 1):
            reword = reword + word[i]
            i -= 1
        rev.append(reword)
    for i in rev:
        print(i, end=" ")


encoder()
