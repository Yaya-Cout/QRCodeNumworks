"""Encode QRCode to be compatible with Numworks."""
import cv2
import PIL
import pyzbar.pyzbar as pyzbar
import qrcode

cap = cv2.VideoCapture(0)

SCAN = True
while SCAN:
    _, frame = cap.read()

    decodedobjects = pyzbar.decode(frame)
    for obj in decodedobjects:
        data = obj.data
        print("Data :", data)
        SCAN = False
        break

    cv2.imshow("QRCode", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break


qr = qrcode.QRCode(
    version=5,
    box_size=1,
    border=0
)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color='black', back_color='white')
img.save('qrcode.png')
img = PIL.Image.open('qrcode.png')
liste = []
colonne, ligne = img.size
for c in range(colonne):
    liste.append([])
    for line in range(ligne):
        pixel = img.getpixel((c, line))
        if pixel == 255:
            liste[c].append(1)
        elif pixel == 0:
            liste[c].append(0)
with open("qrcodedata.py", "w") as f:
    for c in liste:
        for line in c:
            print(line, end="")
            f.write(str(line))
        f.write("\n")
        print()
