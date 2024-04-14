#install all the library
#create a function that collect text and convert into qr code 
# we will save the qr code as image 


import qrcode
def generate_qrcode(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")
    
url=input("Enter the url:")
generate_qrcode(url)