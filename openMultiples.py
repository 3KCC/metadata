import os
from PIL import Image
import ExifTags
from pprint import pprint

path = "C:\Users\MinhTrang-EZFX\Desktop\Minh Trang\Pictures\\"

dirList=os.listdir(path)
for fname in dirList:
	img = Image.open(path+fname)
	print fname
	try:
		exif = {
			ExifTags.TAGS[k]: v
			for k, v in img._getexif().items()
			if k in ExifTags.TAGS
		}
		pprint(exif['DateTime'])
		print '\n'
	except:
		print "No attributes\n"
	