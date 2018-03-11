import picamera
from PIL import Image
#setup camera such that it closes when we are done with it
print "About to take a picture"
with picamera.PiCamera() as camera:
	
	camera.capture("/home/pi/Downloads/detecting-barcodes-in-images/image4.jpg")
print "Picture Taken"	

