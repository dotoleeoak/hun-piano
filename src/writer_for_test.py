# 누구든 훗날 구현하게 될 DB 연결 모듈
# 어떤 식으로 인터페이스가 구현 될지는 모르나
# 등록 페이지와 다른 여러 테스트를 위해 임의로 만들어보았다.
# 와! 객체지향!
import copy
from PianoManager import db_for_test as db


class TestDatabaseWriter:
    # for Singleton
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(TestDatabaseWriter, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        pass

    def write_new_user_data(self, data):
        db.data.append(data)

    def write_temporary_data(self, data, key=None):
        if key:
            db.temp_data[key] = data
        else:
            db.temp_data = copy.deepcopy(data)
