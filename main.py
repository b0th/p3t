import numpy as np
import os,time,sys,random

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

        pet_name=sys.argv[1]
        x=open('pets/{}.txt'.format(pet_name),'r')
        self.pet=x.read().split('\n')
        self.max_len=0

        for i in self.pet:
            if len(i)>self.max_len:
                self.max_len=len(i)

    def Spawn(self,cleared_list,pet,pos=0): #Random spawn pos -> w Matrix().columns & random.choice
        cleared_list=Matrix().ListToMatrix(cleared_list)
        top_line=len(cleared_list)-5-len(pet)
        ground_line=len(cleared_list)-5

        for line,x in zip(range(top_line,ground_line),range(len(pet))):
            for a,b in zip(range(pos,pos+self.max_len),pet[x]):
                cleared_list[line][a]=b
          
        cleared_list=Matrix().MatrixToList(cleared_list)
        return ''.join(cleared_list)
    
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

    def RandomPetPosition(self):
        l_or_r=random.choice([1,-1])
        columns=Matrix().columns
        random_pos=random.randrange(3,columns-self.max_len,1)
        goal_pos=l_or_r*random.randrange(3,20,1)+random_pos
        return [l_or_r,random_pos,goal_pos]

    def MovementPets(self,display):
        pets_number,pets=int(sys.argv[2]),[]

        for i in range(pets_number):
            pets.append(Pet().RandomPetPosition())

        while True:
            for pet in range(len(pets)):
                p3t=PET
                if pets[pet][0]==1:
                    p3t=rotated_pet
        
                try:
                    pets[pet][1]+=pets[pet][0]
                    grab_matrix=Pet().Spawn(display,p3t,pets[pet][1])
                    
                    if pets[pet][1]==pets[pet][2]:
                        l_or_r=random.choice([-1,1])
                        goal_pos=l_or_r*random.randrange(4,20,1)+pets[pet][1]
                        pets[pet]=[l_or_r,pets[pet][1],goal_pos]
                except:
                    pets[pet][0]*=-1
                    pets[pet][2]=pets[pet][0]*random.randrange(6,20,1)+pets[pet][1]
                    pets[pet][1]+=pets[pet][0]
                    

            display=Matrix().INIT(cleared_matrix,'─')
            print(''.join(grab_matrix))
            #print(pets)
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
    display=Matrix().INIT(cleared_matrix,'─')
    #Displaying
    Pet().MovementPets(display)