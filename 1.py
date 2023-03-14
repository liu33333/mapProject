import qrcode
import datetime
import json

qr = qrcode.QRCode(border=0)
data = {
    'id': '123',
    'time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
}
qr.add_data(json.dumps(data))
qr.make(fit=True)
img = qr.make_image(fill_color=(255,255,255), back_color=(35,61,91))
img.save('test1.png')
