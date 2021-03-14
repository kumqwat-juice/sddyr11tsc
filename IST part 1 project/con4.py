board = []
import random
for i in range(6):
    board.append([])
    for j in range(7):
        board[i].append("_")
playing = True

def draw():
    debuger = 0
    for x in board:
        
        print(debuger,x)
        debuger +=1
    print("-------------------------------------")
    print("    1,   2 ,  3 ,  4 ,  5 ,  6 ,  7  ")
    
while playing:
    hlist = []
    #function
    draw()
    choice = input("pick a column to place it in, from 1 to 7")  
    count = 0
    for i in range(0,6):
        
        if board[i][int(choice)-1] == '_':
           count+=1
        else: break
    board[count-1][int(choice)-1] = 'R'
 #winchecker function type 1   
    t = 0  
    while int(choice)-1-t > -1:
        if(board[count-1][int(choice)-1-t] != 'R'):         
            break
        hlist.append(int(choice)-1-t)
        t+=1
    j =0
    while int(choice)-1+j < 7:
        if(board[count-1][int(choice)-1+j] != 'R'):
            break
        hlist.append(int(choice)-1+j)
        j+=1
    hlist.pop(0)
    print(hlist)
#winchecker function type 2
    j =0
    downCheck = []
    upCheck = []
    for i in range (0,6):
        if(count-1-i >=0) and board[count-i-1][int(choice)-1] == 'R':
           upCheck.append( board[count-i-1][int(choice)-1])
        else: break
    for i in range (0,6):
        if (count-1+i < 6) and board[count-1+i][int(choice)-1] == 'R':
            downCheck.append( board[count-1+i][int(choice)-1])
        else: break
    upCheck.pop(0)
    for i in upCheck:
        downCheck.append(i)
#winchecker function type 3       
    diagcheck1 = []
    for i in range(0,6):
        if count-1-i >= 0 and int(choice)-1+i < 7 and board[count-1-i][int(choice)-1+i] == 'R':
            diagcheck1.append(board[count-1-i][int(choice)-1+i])
    for i in range(0,6):
        if count-1+i <6 and int(choice)-1-i >=0 and board[count-1+i][int(choice)-1-i] == 'R':
            diagcheck1.append(board[count-1+i][int(choice)-1-i])
    diagcheck1.pop(0)

    diagcheck2 = []
    for i in range(0,6):
        if count-1+i <6 and int(choice)-1+i < 7 and board[count-1+i][int(choice)-1+i] == 'R':
           diagcheck2.append(board[count-1+i][int(choice)-1+i])
    for i in range(0,6):
        if count-1-i >=0 and int(choice)-1-i >=0 and board[count-1-i][int(choice)-1-i] == 'R':
            diagcheck2.append(board[count-1-i][int(choice)-1-i])
    diagcheck2.pop(0)
     
    print(",,,,,,")
   
    bcount = 0
    botC = random.randint(0,6)
    
    for j in range(0,6):
        if board[j][botC] == '_':
           bcount+=1
        else:break
    board[bcount-1][botC] = 'Y'

    
           

    if downCheck == ['R','R','R','R'] or len(hlist) == 4 or diagcheck1 == ['R','R','R','R'] or diagcheck2 == ['R','R','R','R']:
        print("winner")
        draw()
        #function
        playing = False
    
        
