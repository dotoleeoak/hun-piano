from PySide2.QtCore import QThread, Signal
from nfc.MFRC522 import MFRC522


class NFCReader(QThread):
    tagged = Signal(str) # Emit when nfc is 'tagged' to the module.

    def __init__(self, debug=False):
        super().__init__()
        self.reading = True
        self.debug = debug
        if not self.debug:
            print("nfc init")
            self.nfc = MFRC522()

    def run(self):
        print("Thread running")
        while self.reading:
            if self.debug:
                self.msleep(1000)
            else:
                (status, tag_type) = self.nfc.MFRC522_Request(self.nfc.PICC_REQIDL)

                if status == self.nfc.MI_OK:
                    print("Card detected")

                    # Get the UID of the card
                    if status == self.nfc.MI_OK:
                        (status, uid) = self.nfc.MFRC522_SelectTagSN()
                        uid_str = self.uid_to_string(uid)
                        print(uid_str)
                        self.tagged.emit(uid_str)
                    else:
                        self.tagged.emit(None)

                self.msleep(100)

    def start(self):
        self.reading = True
        super().start()

    def quit(self):
        self.reading = False
        super().quit()

    @staticmethod
    def uid_to_string(uid):
        uid_str = ""
        for i in uid:
            uid_str = format(i, "02X") + uid_str
        return uid_str
