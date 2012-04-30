import math
import random
import sys
sys.path.append("./osc")
from animations import FadeAnimation

z = random.randrange(0,24)

if __name__ == "__main__":
    import time
    out = FadeAnimation()
    out.FADERATE = 8.0
    out.start()
	
    while True:
        for i in range(24):
			pix = [(0.0,0.0,0.0)]*24
			
			
			while z < random.randrange(16,24):
				pix[i] = (random.randrange(0.0, 1023.0),random.randrange(0.0, 1023.0),random.randrange(0.0, 1023.0))
				out.write(pix)
				   
				if(i < 24):
				   i-=1
				   
				z+=1
			
			z = 0
			i = 0.0
			
			time.sleep(0.8)

			#time.sleep(0.2)
			#pix[i] = (random.randrange(0.0, 1023.0),random.randrange(0.0, 1023.0),random.randrange(0.0, 1023.0))
