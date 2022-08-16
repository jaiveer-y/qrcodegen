# ⁡⁣⁢⁣​‌‌‍𝗤𝗿 𝗰𝗼𝗱𝗲 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗼𝗿​⁡
# ⁡⁢⁣⁣This takes an input and converts it into a qr code png.⁡


# ⁡⁢⁢⁢​‌‍‌<--𝗜𝗺𝗽𝗼𝗿𝘁𝘀--> ​⁡


import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image


# this is the input which takes the value and returns it into the qr variable.
i = input('Enter the data: ')
# this creates the qr code data;
qr = pyqrcode.create(i)
# this generates the png;
qr.png("code.png", scale=8)

# Output
d = decode(Image.open("code.png"))
print(d[0].data.decode("ascii"))
print('The QR code has been saved : ./code.png')
