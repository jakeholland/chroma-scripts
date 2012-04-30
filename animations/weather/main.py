import sys
import pywapi
import string
import random
import math
sys.path.append("./osc")
from animations import FadeAnimation

weather = pywapi.get_weather_from_noaa('KCMI')
#Seattle- KBFI Phoenix- KPHX Urbana- KCMI
temp = weather['temp_f']
conditions = weather['weather']
#conditions = "Heavy Thunderstorm"



if conditions.find("Mostly") > -1:
	cloud = 0.5
elif conditions.find("Partly") > -1:
	cloud = 0.8
elif conditions.find("Few") > -1:
	cloud = 1.0
else:
	cloud = 0.4
if conditions.find("Heavy") > -1:
	severe = 0.02
elif conditions.find("Light") > -1:
	severe = 0.2
else:
	severe = 0.05
i = 0
count = 0
print temp + "F"
print conditions

if __name__ == "__main__":
    import time
    out = FadeAnimation()
    pix = [(0.0,0.0,0.0)] * 24
    out.FADERATE = 10.0
    out.start()
		
    while True:		
#Rain
			if conditions.find("Rain") > -1:
				if random.randint(0,5) < 3:
					pix[random.randint(0,23)] = (0.0,0.0,1023.0)
				out.write(pix)
				for i in xrange(24):
					if pix[i][2] > 0.0:
						pix[i] = (0.0,0.0,pix[i][2] - 50.0)
					else:
						pix[i] = (0.0,0.0,0.0)
				time.sleep(severe)
#Thunder
			elif conditions.find("Thunder") > -1:
				count+=1
				if random.randint(0,5) < 3:
					pix[random.randint(0,23)] = (0.0,0.0,1023.0)
				
				if conditions.find("storm") > -1 and count > 5:
					l1= random.randint(0,23)
					pix[l1]= (1023.0,1023.0,0.0)
					if l1 < 21 and l1 > 3:
						pix[l1 +3]= (1023.0,1023.0,0.0)
						pix[l1 -3]= (1023.0,1023.0,0.0)
						count = 0
				out.write(pix)
							
				for i in xrange(24):
					if pix[i][2] > 0.0 and pix[i][1] == 0.0:
						pix[i] = (0.0,0.0,pix[i][2] - 50.0)
					else:
						pix[i] = (0.0,0.0,0.0)
				time.sleep(severe)

#Snow
			elif conditions.find("Snow") > -1:
				if random.randint(0,5) < 3:
					pix[random.randint(0,23)] = (1023.0,1023.0,1023.0)
				out.write(pix)
				for i in xrange(24):
					if pix[i][0] > 0.0 and pix[i][1] > 0.0 and pix[i][2] > 0.0:
						pix[i] = (pix[i][0] - 30.0,pix[i][1] - 30.0,pix[i][2] - 30.0)
					else:
						pix[i] = (0.0,0.0,0.0)
				time.sleep(severe)

#Clouds
			elif conditions.find("Cloud") > -1:
				for i in xrange(24):
					pix[i] = (0.0,765.0,1023.0)
					i+=1
					count+=1
					out.write(pix)
					if count > 5:
						pix[random.randint(0,23)] = (900.0,900.0,900.0)
						count = 0
					out.write(pix)

				time.sleep(cloud+.5)
#Fair
			elif conditions.find("Fair") > -1:
				for i in xrange(24):
					if random.randint(0,23)> 15:
						pix[i] = (0.0,715.0,1000.0)
					else:
					   pix[i] = (0.0,765.0,1023.0)
					i+=1
				time.sleep(cloud+1)
				out.write(pix)
#Fog
			elif conditions.find("Fog") > -1:
				for i in xrange(24):
					if random.randint(0,23)> 15:
						pix[i] = (952.0,932.0,932.0)
					else:
						pix[i] = (1000.0,950.0,950.0)
					i+=1
				time.sleep(cloud+1)
				out.write(pix)
#Overcast
			elif conditions.find("Overcast") > -1:
				for i in xrange(24):
					if random.randint(0,23)> 15:
						pix[i] = (952.0,932.0,932.0)
					else:
						pix[i] = (1000.0,950.0,950.0)
					i+=1
				time.sleep(cloud+1)
				out.write(pix)
