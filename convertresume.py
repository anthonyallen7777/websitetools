#converts pdf to image
#need pdf2image and poppler to convert
#pip install pdf2image
#install poppler

import sys
from pdf2image import convert_from_path

def convert():
	for arg in sys.argv[1:]:
		t = 0
		pages = convert_from_path(arg, 500)
		for page in pages:
		#	page.save(t+'.png','PNG')
			print(t,'\n')
			t=t+1

		print(arg)


if __name__ == '__main__':
    try:
        ## your code, typically one function call
        convert()
    except Exception as e:
        print (e)