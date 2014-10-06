from PIL import Image
import ExifTags
from pprint import pprint

img = Image.open('img.jpg')

exif = {
    ExifTags.TAGS[k]: v
    for k, v in img._getexif().items()
    if k in ExifTags.TAGS
}

pprint(exif['DateTime'])