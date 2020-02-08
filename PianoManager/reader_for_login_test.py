# 주현이가 훗날 구현하게 될 DB 연결 모듈
# 어떤 식으로 인터페이스가 구현 될지는 모르나
# 로그인 페이지 테스트를 위해 임의로 만들어보았다.
# 와! 객체지향!

class TestDatabaseReader:

    def __init__(self):

        # 데이터 방식이 어떨지 모르지만 임의로 만든 예시 데이터.
        # 세계적인 피아니스트가 꿈인 진영이의 연습량을 표현해보았다.
        self.data = {
            "name": "이진영",
            "time_used" : "17:12:35"
            }


    def passInDatabase(self, password):

        # 원래대로라면 DB에 요청해서
        # 학번에 맞는 인물이 존재하는지
        # 확인 후 Data를 주어야겠지만
        # 여기서는 "12345678"이면
        # bool과 Data를 주는 것으로....
        if password == "12345678":
            return (True, self.data)
        else:
            return (False, None)
    
