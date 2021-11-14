
def rotate(message):
    rot = ''
    i = len(message) - 1
    while(i >= 0):
        rot = rot + message[i]
        i -= 1
    return rot

def encrypt(text):
    flag = ''
    key = 'secret'
    encrypt_text = []

    for i in list(rotate(text)):
        flag += chr(ord(i) << 1) # multiplies by 2

    K = len(flag)
    newKey = (key * ((K // len(key)) + 1))[:K] # secretsecretsecretsecretsecretse


    for i in list(zip(newKey, flag)):
        a = chr(ord(i[0]) + ord(i[1]))
        encrypt_text.append(a)

    encrypt_text = ''.join(encrypt_text)

def decrypt(text):
    key = 'secret'
    K = len(text)
    newKey = (key * ((K // len(key)) + 1))[:K]
    print(newKey)
    

    a = []
    for i in range(len(text)):
        t1 = ord(text[i]) - ord(newKey[i])
        t1 = t1 // 2
        a.append(t1)

    return a

text = 'áÕÃÖ×ÖáÇÑÜÓâÕÍÅäÑÚß×ÃÞÏÜÛÓÃÔËÖÛÇ'

res = decrypt(text)[::-1]
print(res)


res = [chr(i) for i in res]
res = ''.join(res)

print(res)
