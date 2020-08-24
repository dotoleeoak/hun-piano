import os

if os.name == "posix":
    from nfc.nfc_reader import NFCReader
else:
    from nfc.nfc_reader_for_test import NFCReader
