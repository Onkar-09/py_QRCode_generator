import qrcode
import image
qr = qrcode.QRCode(
    version = 3, #version of qr
    box_size = 10, #size of box
    border = 5 #white part of image
)

data = input("enter your link to convert into QRcode : ") #Data to encode in the QR code
#Encoding data into the QR Code
qr.add_data(data)
qr.make(fit = True) #Creating the QR code
img = qr.make_image(fill = "black" ,back_color = "white" ) #Converting the QR code into an image object
img.save("trial.png") #Saving the image as a png file