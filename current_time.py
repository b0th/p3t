import datetime,os

class Time:

    def __init__(self):
        self.num_dir='./numbers/'

    def TimeToAsciiArt(self):
        time=str(datetime.datetime.now())[11:-7]

        ret=[]
        chars=[x.replace('.txt','') for x in os.listdir(self.num_dir)]
        for x in time:
            if x in chars:
                x=open('{}{}.txt'.format(self.num_dir,x),'r')
                x=x.read().split('\n')
                ret.append(x)
        
        total_len=sum([len(max(x,key=len)) for x in ret])
        
        return ret,total_len
