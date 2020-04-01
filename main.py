import numpy as np
import os,curses,time
import pet
import random

class Matrix:

    def __init__(self):
        self.columns,self.lines=os.get_terminal_size()
    
    def GetMatrix(self):
        matrix=np.chararray((self.lines, self.columns))
        matrix[:]='.'
        return matrix

    def ClearMatrix(self,array):
        ret=[]
        for i in array:
            b=''
            for ii in i:
                b+=ii.decode("utf-8")
            ret.append(b)
        return ret

    def INIT(self,cleared_list,symbol):
        ground_line=len(cleared_list)-5
        add_line=symbol*self.columns
        clear_line=add_line.replace(symbol,' ')
        cleared_list[ground_line]=add_line
        for i in range(ground_line):
            cleared_list[i]=clear_line
        return cleared_list

    # v Recommended to use after function INIT v
    
    def ListToMatrix(self,MATRIX):
        for i in range(len(MATRIX)):
            MATRIX[i]=list(MATRIX[i])
        return MATRIX

    def MatrixToList(self,LIST):
        for i in range(len(LIST)):
            LIST[i]=''.join(LIST[i])
        return LIST

class Pet:

    def __init__(self):
        self.pet,self.max_len=pet.snail.split('\n'),0
        
        for i in self.pet:
            if len(i)>self.max_len:
                self.max_len=len(i)
        
    def Spawn(self,cleared_list,pet,pos=0): #Random spawn pos -> w Matrix().columns & random.choice
        cleared_list=Matrix().ListToMatrix(cleared_list)
       
        top_line=len(cleared_list)-5-len(pet)
        ground_line=len(cleared_list)-5
        center_column=(Matrix().columns-self.max_len)//2+pos

       
        for line,x in zip(range(top_line,ground_line),range(len(pet))):
            for a,b in zip(range(center_column,center_column+self.max_len),pet[x]):
                cleared_list[line][a]=b
          

        cleared_list=Matrix().MatrixToList(cleared_list)
        print(''.join(cleared_list))
    
    def RotatePet(self):
        rev_symbols={'\\':'/','/':'\\','(':')',')':'(','{':'}','}':'{','<':'>','>':'<',"'":'`','`':"'"}
        space_count=[self.max_len-len(x) for x in self.pet]

        for i in range(len(self.pet)):
            self.pet[i]=tuple(self.pet[i][::-1])

        rotated_pet=[]
        for x,space in zip(self.pet,space_count):
            sub,a=[],0
            sub.append(space*' ')
            for c in x:
                for y in rev_symbols:
                    if c==y:
                        c=rev_symbols[y]
                        break
                sub.append(c)
            rotated_pet.append(sub)

        for i in range(len(rotated_pet)):
            rotated_pet[i]=''.join(rotated_pet[i])
        return rotated_pet

    def MovementPet(self,display):
        #Make spawn p3t
        Pet().Spawn(display,PET)
        #Moving p3t
        pos=0
        while True:
            display=Matrix().INIT(cleared_matrix,'-')
            random_move=random.choice([1,-1])
            pos+=random_move
            if random_move==1:
                p3t=rotated_pet
            else:
                p3t=PET
            Pet().Spawn(display,p3t,pos)
            time.sleep(0.2)

if __name__ == '__main__':
    #Normal p3t
    PET=Pet().pet
    #Rotated p3t
    rotated_pet=Pet().RotatePet()
    #Create matrix
    _matrix=Matrix().GetMatrix()
    #Convert bytes to strings
    cleared_matrix=Matrix().ClearMatrix(_matrix)
    #Initialization of the set
    display=Matrix().INIT(cleared_matrix,'-')
    #Displaying
    Pet().MovementPet(display)
  