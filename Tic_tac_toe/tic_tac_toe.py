#!/usr/bin/env python
# coding: utf-8

# In[9]:


my_dict={1:[3,3],2:[3,8],3:[3,13],4:[9,3],5:[9,8],6:[9,13],7:[14,3],8:[14,8],9:[14,13]}
em_dic={}
def make_line(pos,ch):
    for i in range(18):
        my_pos=my_dict.get(pos)
       
       
        for j in range(16):
            if j>0 and  (i==0 or i==17 or i==5 or i==11):
                print("_ ",end="")

            elif i>0 and (j==0 or j==15 or j==5 or j==10):
                print(" |",end="")
                        
            elif i==my_pos[0] and j==my_pos[1] :
                print(" "+ch,end="")
            
            elif len(em_dic) > 0 :
                c=0
                for va in em_dic.values():
                    if i==va[0] and j==va[1]:
                        print(va[2]+" ",end="")
                        c=1
                if c!=1 :
                    print("  ",end="")
                        
            else :
                print("  ",end="")
             

        print(end="\n")
    
        
    lis=my_pos.copy()
    lis.append(ch)
    em_dic[pos]=lis 



print("\tWELCOME")

k=1

for i in range(18):
    pos=3
    for j in range(16):
        if j>0 and  (i==0 or i==17 or i==5 or i==11):
            print("_ ",end="")
        elif i>0 and (j==0 or j==15 or j==5 or j==10):
            print(" |",end="")
        elif (i==3 or i== 9 or i== 14 )and j==pos :
            print(k,end=" ")
            k+=1
            pos+=5
            
            
        else :
            print("  ",end="")
          
    print(end="\n")
    
    
print("\n")
play_1=input("Enter player 1 Name : ")
play_2=input("Enter player 2 Name : ")

choice_1=1
choice_2=0
print(f"{play_1} choice is 'X'")
print(f"{play_2} choice is 'O'")

flag=0
play=True
count=[]
data=[None,None,None,None,None,None,None,None,None,None]
move=1
while(flag!=1):
    
    if(play):
        pos_1=int(input(f"{play_1} enter your position from '1 to 9' : "))
        if pos_1 not in count :
            count.append(pos_1)
            data[pos_1]="X"
            make_line(pos_1,"X")
            play=False
        else :
            print("Enter VALID POSITION")
    
    else :
        pos_1=int(input(f"{play_2} enter your position from '1 to 9' : "))
        if pos_1 not in count :
            count.append(pos_1)
            data[pos_1]="O"
            make_line(pos_1,"O")
            play=True
        else :
            print("Enter VALID POSITION")
    
    for i , j in zip(range(1,9,3),range(1,4)) :
    
        if (data[i]=="X" and data[i+1]=="X" and data[i+2]=="X") or (data[j]=="X" and data[j+3]=="X" and data[j+6]=="X") or (data[1]=="X" and data[5]=="X" and data[9]=="X")  or (data[3]=="X" and data[5]=="X" and data[7]=="X") :
            print(f"\n\t{play_1} WINS")
            flag=1
        elif (data[i]=="O" and data[i+1]=="O" and data[i+2]=="O") or (data[j]=="O" and data[j+3]=="O" and data[j+6]=="O") or (data[1]=="O" and data[5]=="O" and data[9]=="O")  or (data[3]=="O" and data[5]=="O" and data[7]=="O") :
            print(f"\n\t{play_2} WINS")
            flag=1
        elif move==9 :
            print("\n\tDRAW \n\tTRY NEXT TIME")
            flag=1
            
        
    move+=1


# #### 

# In[ ]:





# In[ ]:




