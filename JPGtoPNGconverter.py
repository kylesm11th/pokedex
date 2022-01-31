import sys
import os
from PIL import Image

    #grab the 1st and 2nd argument
path = sys.argv[1]
directory = sys.argv[2]

    #check if new folder exists, if not, create it.
if not os.path.exists(directory):
    os.makedirs(directory)
    
    #loop through pokedox
for filename in os.listdir(path):
  clean_name = os.path.splitext(filename)[0]
  img = Image.open(f'{path}{filename}')
    #added the / in case user doesn't enter it. You may want to check for this and add or remover it. 
    #convert to png  
  img.save(f'{directory}/{clean_name}.png', 'png')
  print('all done!')
