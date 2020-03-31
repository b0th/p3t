import numpy as np
import os,curses,time
import pet

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
        add_line=''.join([symbol for i in range(self.columns)])
        #add_line=''.join(add_line)
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
        self.pet,self.max_len=pet.camel.split('\n'),0
        
        for i in self.pet:
            if len(i)>self.max_len:
                self.max_len=len(i)
        

    def SpawnAtCenter(self,cleared_list):

        cleared_list=Matrix().ListToMatrix(cleared_list)
       
        top_line=len(cleared_list)-5-len(self.pet)
        ground_line=len(cleared_list)-5
        center_column=(Matrix().columns-self.max_len)//2

        x=0
        for line in range(top_line,ground_line):
            for a,b in zip(range(center_column,center_column+self.max_len),self.pet[x]):
                cleared_list[line][a]=b
            x+=1

        cleared_list=Matrix().MatrixToList(cleared_list)

        print(''.join(cleared_list))

    #faire function spawn,left,right

if __name__ == '__main__':
    #Matrix=Matrix()
    
    #Create matrix
    _matrix=Matrix().GetMatrix()
    #Convert bytes to strings
    cleared_matrix=Matrix().ClearMatrix(_matrix)
    #Initialization of the set
    display=Matrix().INIT(cleared_matrix,'─')
    #Make spawn p3t
    Pet().SpawnAtCenter(display)

    #print(''.join(display))
    



























'''stdscr = curses.initscr()
for i in range(10):
    print(''.join(display))
    stdscr.refresh()

    time.sleep(0.2)


curses.endwin()'''
