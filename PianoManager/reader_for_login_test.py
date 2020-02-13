# 주현이가 훗날 구현하게 될 DB 연결 모듈
# 어떤 식으로 인터페이스가 구현 될지는 모르나
# 로그인 페이지 테스트를 위해 임의로 만들어보았다.
# 와! 객체지향!

class TestDatabaseReader:
    # for Singleton
    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(TestDatabaseReader, self).__new__(self)
        return self.instance
    
    def __init__(self):
        # 데이터 방식이 어떨지 모르지만 임의로 만든 예시 데이터.
        # 세계적인 피아니스트가 꿈인 진영이의 연습량을 표현해보았다.
        # 평범한 김정원과 비교해보자.
        self.data = {
            "12345678":
            {
                "name": "이진영",
                "time_used" : "17:01:25"
            },
            "11111112":
            {
                "name": "김정원",
                "time_used": "00:30:12"
            }}

        self.currentData = {"name": "None", "time_used": "00:00:00"}


    def passInDatabase(self, password):

        self.currentData = self.data[password]
        if self.currentData is not None:
            return (True, self.currentData)
        else:
            return (False, None)
        

    def getCurrentData(self):

        return self.currentData
    
