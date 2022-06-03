#converts pdf to image
#need pdf2image and poppler to convert
#pip install pdf2image
#install poppler

import sys
import os
from pdf2image import convert_from_path
#current directory
directory = os.getcwd()
pPath = directory+R"\poppler-22.04.0\Library\bin"

def convert():
	for arg in sys.argv[1:]:
		t = 0
		pages = convert_from_path(arg, 500,poppler_path=pPath)
		for page in pages:
			page.save('resume'+str(t)+'.png','PNG')
			print(t,'\n')
			t=t+1

		print(arg)


if __name__ == '__main__':
    try:
        ## your code, typically one function call
        convert()
    except Exception as e:
        print (e)