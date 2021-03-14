import random
l6= ''
l5= ''
l4 = [' ',' ']
l3 = ''
l2 = ['','','','','']
l1=''
f = open("wordlist.txt", "r")
wordpick = f.readlines()
rNum = random.randint(1, 850)
word = (wordpick[rNum][0:len(wordpick[rNum])-1])
emptyword = []
lives = 0
for i in word:
    emptyword.append('_')
print(emptyword)
guessing = True
while guessing:
    guess = input("guess a letter for the word")
    count = 0
    Lcount = 0
    for i in word:
        if i == guess:
            emptyword[count] = i
        else:
            Lcount += 1
        count+=1
    if(Lcount == len(word)):
        lives +=1
    if(lives == 1):l1 = '-------'
    if(lives == 2):l2 = ['|','|','|','|','|']
    if(lives == 3):l3 = '-------'
    if(lives == 4):l4 = ['|','0']
    if(lives == 5):l5 = '/|\\'
    if(lives == 6):
        l6 = '/\\'

        print("The word was :",word+':. You are a loser, game over')
        guessing = False
    print(emptyword)
    if word == ''.join(emptyword):
        print("you are a winner")
        guessing = False
    print(l3 + '\n'+ l2[0],'   ',l4[0]+'\n'+l2[1],'   ',l4[1]+'\n'+l2[2],'  ',l5+'\n'+l2[3],'  ',l6+'\n'+l2[4]+'\n'+l1)
