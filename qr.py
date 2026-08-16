import qrcode

url = "https://github.com/Wilian-Casasbuenas/sapifrut-menu.git"

img = qrcode.make(url)
img.save("logo.png")