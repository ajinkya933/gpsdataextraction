
import piexif
exif_dict = piexif.load('/users/ajinkyabobade/downloads/im1.jpg')
for ifd in ("0th", "Exif", "GPS", "1st"):
    for tag in exif_dict[ifd]:
        print(piexif.TAGS[ifd][tag]["name"], exif_dict[ifd][tag])


