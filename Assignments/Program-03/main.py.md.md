Name: Chris Cook
Email: c.w.cook@live.com
Assignment: Program-03 - ImageEdit
Due: Friday Dec. 9, 2016 @ 5:00pm
Purpose: Prompts the user for an image filename, the action desired to be performed on the image, and the output name. 
The program will blur, glass-ify, flip, posterize, solarize, or Warhol-ilize the image, and then save the image


    from PIL import Image
    import os
    import sys
    from PIL import Image, ImageDraw, ImageFont, ImageFilter
    import random
    import imageEdit
    from imageEdit import *
    
    if __name__=="__main__":
    
        commands = {}
    	
        commands['-i']=input("Enter the name of the file you want to modify with the extension.  ")
    	
        commands['-x']=input("Which operation would you like to perform? (flip,glass,blur,posterize,solarize, or warhol)  ")
    	
        if commands['-x'] == 'flip':
            commands['-v']=input("Enter a 0 for horizontal flip or a 1 for a veritcal flip.  ")
    	
        if commands['-x'] == 'glass':
            commands['-v']=input("Enter an integer.  ")        
    	
        if commands['-x'] == 'blur':
            commands['-v']=input("Enter an integer that will blur the image.  ")      
    
        if commands['-x'] == 'posterize':
            commands['-v']=input("Enter an integer that will posterize the image. (64 is the best)  ") 
    
        if commands['-x'] == 'solarize':
            commands['-v']=input("Enter an integer that will solarize the image.  ")  	
    
        if commands['-x'] == 'warhol':
            commands['-v']=64 		
        
        commands['-o']=input("What would you like the name of the output file to be?  ")
    	
        if '-i' in commands.keys():
            input_file = commands['-i']
    		
        if '-o' in commands.keys():
            output_file = commands['-o']
        else:
            output_file = commands['-i']
    		
    
    		
    	#Creates a new ImageEdit object
        ie = ImageEdit(input_file)	
    	
        if commands['-x'] == 'flip':
            out = ie.flip(commands['-v'],input_file,output_file) 
    	
        if commands['-x'] == 'glass':
            out = ie.glass_effect(commands['-v'],input_file,output_file)
    	
        if commands['-x'] == 'blur':
            out = ie.blur(commands['-v'],input_file,output_file) 
    		
        if commands['-x'] == 'posterize':
            out = ie.posterize(commands['-v'],input_file,output_file) 
    
        if commands['-x'] == 'solarize':
            out = ie.solarize(commands['-v'],input_file,output_file) 
    
        if commands['-x'] == 'warhol':
            out = ie.warhol(commands['-v'],input_file,output_file) 
    		
        print(out+" is the edited image.")