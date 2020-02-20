from PySide2.QtCore import QThread, Signal
from NFC.MFRC522 import MFRC522


class NFCReader(QThread):
    nfc_connect = Signal(str)
    reading = True
    
    def __init__(self):
        super().__init__()
        self.nfc = MFRC522()
        

    def run(self):
        
        print("Thread running")
        while self.reading:
            (status, TagType) = self.nfc.MFRC522_Request(self.nfc.PICC_REQIDL)

            if status == self.nfc.MI_OK:
                print("Card detected")

                # Get the UID of the card
                if status == self.nfc.MI_OK:
                    (status, uid) = self.nfc.MFRC522_SelectTagSN()
                    uid_str = self.uidToString(uid)
                    print(uid_str)
                    self.nfc_connect.emit(uid_str)
                else:
                    self.nfc_connect.emit(None)

            self.msleep(100)
            

    def start(self):
        self.reading = True
        super().start()
                    
    def quit(self):
        self.reading = False
        super().quit()
            
    def uidToString(self, uid):
        uid_str = ""
        for i in uid:
            uid_str = format(i, '02X') + uid_str
        return uid_str
            
