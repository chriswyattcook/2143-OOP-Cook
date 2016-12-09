"""

Name: Chris Cook
Email: c.w.cook@live.com
Assignment: Program-03 - ImageEdit
Due: Wednesday Dec. 7, 2016 @ 1:00pm

"""

import sys
from PIL import Image
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from random import randint

class ImageEdit(object):
    def __init__(self,input_file):
        self.Img = Image.open(input_file)
    
    def glass_effect(self,value,image,imageout=None):
        blankImage = Image.new( 'RGB', (255,255), "black")
        pixels = pixelsOG = self.Img.load()
        width,height = self.Img.size  
        #print(height,width)		
        		
        xPos = yPos = 0
		

        for x in range(0,width-1):
            for y in range(0,height -1):
                xChoice = randint(-int(value),int(value))
                yChoice = randint(-int(value),int(value))
                if(x+xChoice > 0 and x+xChoice < width):
                    if(0 < y+yChoice < height):
                        #print(x,y+yChoice)
                        #print(pixelsOG[(x+(xChoice)),(y+(yChoice))])
                        pixels[x,y]=pixelsOG[(x+(xChoice)),(y+(yChoice))]
                        
           
        self.Img.save(imageout)
        return(imageout)
	#flips an image vertically of horizontally
    def flip(self,value,image,imageout=None):
        #self.Img.show()
        if (value == '0'):
            blankImage = Image.new( 'RGB', (255,255), "black")
            pixels = self.Img.load()
	
            width,height = self.Img.size
			
            current = 0
            opposite = width-1 - current	
			
            for x in range(width//2):
                #print(current,opposite)
                for i in range(height):
                    temp=pixels[current,i]
                    pixels[current,i] = pixels[opposite,i]
                    pixels[opposite,i] = temp
                current += 1
                opposite = width - current
        
            self.Img.save(imageout)
            
            return(imageout)
			
        if (value == '1'):
            blankImage = Image.new( 'RGB', (255,255), "black")
            pixels = self.Img.load()
	
            width,height = self.Img.size
			
            current = 0
            opposite = height-1 - current	
			
            for x in range(height//2):
                #print(current,opposite)
                for i in range(width):
                    temp=pixels[i,current]
                    pixels[i,current] = pixels[i,opposite]
                    pixels[i,opposite] = temp
                current += 1
                opposite = height - current
        
            self.Img.save(imageout)
            return(imageout)
		
	#blurs an image by a number that is passed in
    def blur(self,value,image,imageout=None):
        pixels = self.Img.load()
        width,height = self.Img.size     
        blurRadius = int(value)
        r=b=g=0
		
        z=2*blurRadius*2*blurRadius
        #print(width,height)
        for x in range(0+blurRadius,width-blurRadius-1):
            for y in range(0+blurRadius,height-blurRadius-1):
                for xPos in range(-blurRadius,blurRadius):
                    for yPos in range(-blurRadius,blurRadius):
                        
                        thePixel=self.Img.getpixel((x+xPos,y+yPos))
                        r+= thePixel[0]
                        g+= thePixel[1]
                        b+= thePixel[2]
			
                    self.Img.putpixel((x,y),((r//z),(g//z),(b//z)))
                r=g=b=0   
        self.Img.save(imageout)
        return(imageout)
        
	#uses a value passed in to give the appearance of a cartoon/ poster look
    def posterize(self,value,image,imageout=None):
        pixels = self.Img.load()
        width,height = self.Img.size
		
        value = int(value)
       
        for x in range(width):
            for y in range(height):
                r,g,b =self.Img.getpixel((x,y))
                
                r = self.__snap_color__(r,value)
                g = self.__snap_color__(g,value)
                b = self.__snap_color__(b,value)
				
                newColor=(r,g,b)
				
                self.Img.putpixel((x,y),newColor)
				
        self.Img.save(imageout)
        return(imageout)
        
	#solarizes an image 
    def solarize(self,value,image,imageout=None):
        pixels = self.Img.load()
        width,height = self.Img.size
		
        value = int(value)
		
        for x in range(width):
            for y in range(height):
                
                r,g,b=self.Img.getpixel((x,y))
                if r <= value:
                    r = value - r
                else: 
                    r = value + r
					
                if g <= value:
                    g = value - g
                else: 
                    g = value + g
					
                if b <= value:
                    b = value - b
                else: 
                    b = value + b
				
                newColor=(r,g,b)

                self.Img.putpixel((x,y),newColor)				
		
        self.Img.save(imageout)
        return(imageout)
        
	#Takes an image, grayscales it, and then makes it look like a picture 
	#Warhol would have made
    def warhol(self,value,image,imageout=None):
        pixels = self.Img.load()
        width,height = self.Img.size
       
	   #255/5 seemed the easiest
        rectangles = [0,51,102,153,204]
	
        warhol_colors=[(255,255,0),(0,0,255),(255,0,255),(255,165,0) ,(255,192,203)]
		
        for x in range(width):
            for y in range(height):
                
                r,g,b=self.Img.getpixel((x,y))
				
                gray = (r+g+b)//3
				
                newColor=(gray,gray,gray)

                self.Img.putpixel((x,y),newColor)
                    
        self.posterize(64,image,imageout)
				
        for x in range(width):
            for y in range(height):
                newColor2=self.Img.getpixel((x,y))
                nR = 0
                while nR < 5:
                    
                    if newColor2[0] <= rectangles[nR]:
                        newColor2 = warhol_colors[nR]
                        self.Img.putpixel((x,y),newColor2)
                    nR += 1
                        
        
        
        self.Img.save(imageout)
        return(imageout)

		
    def __snap_color__(self,color,snap_val):
        color = int(color)
        m = color % snap_val
        if m < (snap_val // 2):
            color -= m
        else:
            color += (snap_val - m)
                    
        return int(color)
