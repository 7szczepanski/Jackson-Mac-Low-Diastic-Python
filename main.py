import random
import string
def createDict():
    line = ""
    with open('dictionay.txt', 'a') as f:
        for h in range(0, 1000):
            line = ''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase, k=15))
            f.write(line + "\n")

def pushWords(lines):
    with open('dictionay.txt') as f:
        content = f.readlines()
        for lin in content:
            lines.append(lin)

def diastic(seed,dic):
    currentWord = 0
    currentSeed = 0
    phrase = ""
    for i in range(0,len(seed)):
        c = seed[i]
        for j in range (currentWord, len(dic)):
            if dic[j][i]==c:
                if c == ' ':
                    str = ' '
                    phrase += str + "\n"
                    break
                str = dic[j]
                phrase += str + "\n"
                currentWord = j+1
                break
    return phrase


def main():
    seek = input("Give me sentence to recreate ( max 15 chars )")
    lines = []
    pushWords(lines)
    fraza = diastic(seek, lines)
    print(fraza)


if __name__ == '__main__':
    main()
