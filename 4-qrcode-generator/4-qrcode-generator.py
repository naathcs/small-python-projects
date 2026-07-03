# library installed in the virtual environment to be imported in the code
# qrcode library must be installed with the PIL dependency or the image generator will call for a 'ModuleNotFoundError'
import qrcode

data = input('Enter the text or URL for the QR Code: ').strip()
filename = input('Enter the file name (please add the image extension): ').strip() # The name must have the image extension or it will not be created as image

# Enhancement 01 - let the user choose the color and background color of the QR Code
qrcolor = input('What color do you want QR Code to be?: ').strip()
bgcolor = input('What color do you want the background?: ').strip()

qr = qrcode.QRCode(box_size=10, border=2)
qr.add_data(data)
if qrcolor == "" and bgcolor =="":
    image = qr.make_image(fill_color="black", back_color="white")
else:
    image = qr.make_image(fill_color=qrcolor, back_color=bgcolor)
image.save(filename)

print(f'QR Code has been saved as {filename}')