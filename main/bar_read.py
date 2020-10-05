import cv2
import pyzbar.pyzbar as pyzbar
from django.conf import settings

def bar_read(path):
    img = cv2.imread(path)

    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    decoded = pyzbar.decode(imgray)

    for d in decoded:
        cv2.rectangle(img, (d.rect[0], d.rect[1]), (d.rect[0]+d.rect[2], d.rect[1]+d.rect[3]), (0,0,255), 2)
        return d.data.decode('utf-8')
