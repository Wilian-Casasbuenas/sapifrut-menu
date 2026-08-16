import qrcode

url = "https://Wilian-Casasbuenas.github.io/sapifrut-menu/"

img = qrcode.make(url)
img.save("qr_salpifrut.png")