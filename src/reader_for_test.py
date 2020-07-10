# 누구든 훗날 구현하게 될 DB 연결 모듈
# 어떤 식으로 인터페이스가 구현 될지는 모르나
# 로그인 페이지 테스트를 위해 임의로 만들어보았다.
# 와! 객체지향!
from PianoManager import db_for_test as db


class TestDatabaseReader:
    # for Singleton
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(TestDatabaseReader, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        pass

    def is_pass_in_database(self, password):
        contact = "010-" + password[:4] + "-" + password[4:]
        data_found = next((item for item in db.data if item["contact"] == contact), False)
        print(data_found)
        if not data_found:
            return False, None
        else:
            db.temp_data = data_found
            return True, db.temp_data

    def is_uid_in_database(self, uid):

        data_found = next((item for item in db.data if item["NFC_UID"] == uid), False)
        if not data_found:
            return False, None
        else:
            db.temp_data = data_found
            return True, db.temp_data

    def get_current_data(self, key=None):
        if key:
            return db.temp_data[key]
        else:
            return db.temp_data
