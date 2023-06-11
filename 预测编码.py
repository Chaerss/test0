

def DPCM(yinBuf, yBuf, dpBuf,frameWidth,  frameHeight):
	for i in range(frameHeight * frameWidth):	
		if (i % frameWidth == 0):
		
			dpBuf[i] = yinBuf[i]
			yBuf[i] = dpBuf[i]		
		else:		
			tmp = yinBuf[i] - yBuf[i - 1]


			
		


