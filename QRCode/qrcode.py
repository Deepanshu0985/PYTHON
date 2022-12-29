import pyqrcode
import png
from pyqrcode import QRCode

s="www.geeksforgeeks.org"

url = pyqrcode.create(s)

url.svg("myqr.svg",scale=8)
url.svg("myqr.png",scale=6)

