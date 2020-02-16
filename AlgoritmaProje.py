import time

with open("statements.txt", "r") as myfile:
    statements = myfile.readlines()

with open("the_truman_show_script.txt", "r") as myfile:
    script = str(myfile.readlines())


def cumleSayisi(data):
    count = 1
    for i in range(0, 336):
        if data[i] == '\n':
            count = count + 1
    return count
#kaç tane kelime var truman scriptinde boşluğa geldiğinde 1 ekliyor

cumleler = ['']
for i in range(0, len(statements)):
    cumleler.append('')
#dinamik array oluşturur ve statementtaki cümlelerden bir array oluşturuyoruz kaç cümle varsa saydırmamıza yarıyor.
#bunu yapmazsak statementtaki cümlelerin arraylerini belirtmemiz lazım

def replaceAltire(statements):
    flag = 0
    for i in range(0, len(statements)):
        for j in range(0, len(statements[i])):
            if statements[i][j] == '_':
                flag = flag + 1
            elif flag == 0:
                cumleler[i] = cumleler[i] + statements[i][j]
            elif statements[i][j] == '\n': #boşluğa yani endline a geldiğinde flagi sıfırlıyor istenilen statement bittiği için bi sonraki statementa öyle geçer
                flag = 0
    return cumleler

#alt tireyi tespit edip eğer alt tire varsa atlaması için yani alt tireyi görünce duruyor

cumleler = replaceAltire(statements)

#alt tireye kadar olan kısmı alır sonrasını okumaz.


def textSearch(substr, txt):
    M = len(substr)
    N = len(txt)

    uzunluk = [0] * M
    j = 0
    uzunlukArray(substr, M, uzunluk)
    i = 0
    while i < N:
        if substr[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            j = uzunluk[j - 1]
            index = i - j  # ending index
            return index
        elif i < N and substr[j] != txt[i]:
            if j != 0:
                j = uzunluk[j - 1]
            else:
                i += 1


def uzunlukArray(substr, M, uzunluk):
    len = 0
    uzunluk[0]
    i = 1

    while i < M:
        if substr[i] == substr[len]:
            len += 1
            uzunluk[i] = len
            i += 1
        else:
            if len != 0:
                len = uzunluk[len - 1]
            else:
                uzunluk[i] = 0
                i += 1

#KMP algoritması ve search kısmı

def findtheGap(ending, script):
    for i in range(0, 20):
        if script[ending + i] == ' ':
            return ending + i
        elif script[ending + i] == '!':
            return ending+i
        elif script[ending + i] == '?':
            return ending + i
        elif script[ending + i] == '-':
            return ending + i
        elif script[ending + i] == '(':
            return ending + i
        elif script[ending + i] == ')':
            return ending + i
        elif script[ending + i] == '"':
            return ending + i

#scripte bakıyor ending + i dediği kelimeden sonra gelen kısım boşluk ünlem soru işareti falan varsa kelimeyi orda durduruyor.


def lookForFirst(starting,script):
    for i in range(0,20):
        if script[starting-i]==' ':
            return starting-i
        elif script[starting-i]=='_':
            return starting-i


algoritmaBaslangic = time.time()
for i in range(0, len(cumleler) - 1): #statementtaki endline kadar ki kısımlar array sıfırdan başladığı için
    ending = textSearch(cumleler[i], script) #statementın içinden i. cümleyi alır truman show textinden aratır buna ending diyoruz
    if ending != None:
        starting = ending - len(cumleler[i]) #truman show textin içersinden istenilen statementın yerini bulup uzunlugunu çıkartıp cümlenin nerde başladığını bulur.
        print('Original Statement with missing parts=',statements[i],end='') #statementı kendisi end kısmını yazmazsak üç alt tireden sonrasını almaz.
        kayipKelimeindexi = findtheGap(ending, script) #statement boşluğun doldurulması gereken yerin indeksini burda tutuyoruz
        print(script[ending:kayipKelimeindexi],"\n")
        print('Completed Statement=',script[starting:starting + len(script[ending:kayipKelimeindexi]) - 3 + len(statements[i])], "\n") #eksik olan kelimeyi yerine yerleştirip
        #yazdırdığımız yer -3 anlamı kelimeyi azaltıyo fazla almasın diye
    else:
        print("Statement not Found!")
algoritmaBitis = time.time()
print("Text search time : ", algoritmaBitis - algoritmaBaslangic)

