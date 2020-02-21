from exif import Image
import datetime 
import urllib3
import numpy as np
import cv2
from base64 import b64decode
# with open('woi.jpg', 'rb') as image_file:
#     my_image = Image(image_file)

# date_image=my_image['datetime'][:13]
# date_image_baru=date_image.replace(":","-")+":00:00"
# print(date_image_baru)


# print(datetime.datetime.now().strftime("%Y-%m-%d %H:00:00"))



        
resp=urllib3.PoolManager()
der=resp.request("GET", "https://akns-images.eonline.com/eol_images/Entire_Site/20191112/rs_634x1024-191212115145-634x1024-bradpitt-gj-12-12-19.jpg?fit=inside|900:auto&output-quality=90")
print("DOR",der.read)

# data=b64decode(der.read)
with open("lapo1.jpg", "wb") as f:
    f.write(der.data)
# image = np.asarray(bytearray(der.read()), dtype="uint8")
# print("JJJ",image)
# image = cv2.imdecode(image, cv2.IMREAD_COLOR)
# return the image

# url_to_image("https://images.fandango.com/ImageRenderer/300/0/redesign/static/img/default_poster.png/0/images/masterrepository/performer%20images/p56988/BradPitt-2016.jpg")



    #IMAGEXIF
    # try:
    #     with open(image_file, 'rb') as image_verify:
    #         my_image = Image(image_verify)
          
    # except:
    #     if "http" in image_file:
    #         with open("admin_photo.jpg", 'rb') as image_verify:
    #             my_image = Image(image_verify)
        
    
    # if my_image.has_exif:
    #     print("SALAH")
    #     date_image=my_image['datetime'][:13]
    #     date_image_baru=date_image.replace(":","-")+":00:00"
    #     date_now=datetime.datetime.now().strftime("%Y-%m-%d %H:00:00")
    # else:
    #     print("WOKA")
    #     date_image_baru = None
    #     date_now=datetime.datetime.now().strftime("%Y-%m-%d %H:00:00")