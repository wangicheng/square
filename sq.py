import math
import numpy as np
#sq=np.array([2,4,6,7,8,9,11,15,16,17,18,19,24,25,27,29,33,35,37,42,50])
sq=np.array([1,2,2,3,3,3])
sq2=np.power(sq,2)
space=np.zeros((6,6))
if int(math.sqrt(sum(sq2)))==math.sqrt(sum(sq2)):
    while np.sum(space)==0:#直到排成功
        for use in range(1,len(sq)):#排正方形:
            use=sq2[use]
            ok=0
            x=0
            y=0
            while ok==1:
                if sum(sum(space[x:x+use+1,y:y+use+1]))==0:
                    space[x:x+use+1,y:y+use+1]=use
            