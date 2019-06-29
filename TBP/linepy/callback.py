# -*- coding: utf-8 -*-
class Callback(object):

    def __init__(self, callback):
        self.callback = callback

    def PinVerified(self, pin):
        self.callback("Masukkan PIN ini\n" + pin + "'•Salin Qr paling lambat 2menit \n•buka di line dan Login sb block spam by Dhenza\n")

    def QrUrl(self, url, showQr=True):
        if showQr:
            notice='Atau pindai QR ini'
        else:
            notice=''
        self.callback('Buka tautan ini\n' + notice + '•Salin Qr paling lambat 2menit \n•buka di line dan Login sb block spam by Dhenza\n' + url)
        if showQr:
            try:
                import pyqrcode
                url = pyqrcode.create(url)
                self.callback(url.terminal('green', 'white', 1))
            except:
                pass

    def default(self, str):
        self.callback(str)