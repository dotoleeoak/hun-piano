from PySide2.QtCore import QThread, Signal


class NFCReader(QThread):
    nfc_connect = Signal(str)
    reading = True
    
    def __init__(self):
        super().__init__()

    def run(self):
        
        print("Thread running")
        while self.reading:
            self.msleep(1000)
            pass

    def start(self):
        self.reading = True
        super().start()
                    
    def quit(self):
        self.reading = False
            
    @staticmethod
    def uid_to_string(uid):
        uid_str = ""
        for i in uid:
            uid_str = format(i, '02X') + uid_str
        return uid_str
