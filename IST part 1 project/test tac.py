board = [['_','_','_'],['_','_','_'],['_','_','_']]
emptySquare={0:[1,2,3],1:[1,2,3],2:[1,2,3]}
import random
print("input row then column, use the key below to understand")
print("[11],[12],[13]")
print("[21],[22],[23]")
print("[31],[32],[33]")
playing = True
choosing = True
count = 0
while playing:
    while choosing:
        
        x = input("place your X")
        if int(x[1]) in emptySquare[int(x[0])-1]:
            board[int(x[0])-1][int(x[1])-1] = 'X'
            emptySquare={0:[],1:[],2:[]}
            break
        else:
            print("please try again you seemed to have picked a used square")          
    for i in range(3):
        print(board[i])
        
        for s in board[i]:
             count +=1
             if s == '_':
                emptySquare[i].append(count)          
        count =0
    ycheck = []
    for xcord in range(0,3):
       ycheck.append( board[xcord][int(x[1])-1] )
    diagcheck = []
    diagcheck2 = []
    if x[0] == x[1] or int(x[0]) == int(x[1])-2 or int(x[1])==int(x[0])-2:
        for i in range(0,3):
            diagcheck.append(board[0+i][0+i])
            diagcheck2.append(board[0+i][2-i])
   #win fucntion 
    if board[int(x[0])-1] == ['X','X','X'] or ycheck == ['X','X','X'] or diagcheck == ['X','X','X'] or diagcheck2 == ['X','X','X']:
        print("winner winner chicken dinner")
        break

    
    for i in emptySquare:
        if len(emptySquare[i]) > 0:
            board[int(i)][int(emptySquare[i][0])-1] = '0'
            ychecker = []
            for xcord in range(0,3):
               ychecker.append( board[xcord][int(emptySquare[i][0])-1] )
            diag = [board[0][2],board[1][1],board[2][0]]
            
            if (board[int(i)]) == ['0','0','0'] or ychecker == ['0','0','0'] or diag == ['0','0','0']:
                print("you are a loser, game over")
                playing = False
            emptySquare[i].remove(emptySquare[i][0])
            
            break
        
    print("The computer is Calculating...")
    for i in range(3):
        print(board[i])
    print("....")
    
 
    
    

    
            
    
        
        
    

    
    
