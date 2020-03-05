성균관대 음취헌 2020
=======

PianoManager
------
- 라즈베리파이 + NFC 이용한 사용시간 체크
- 라즈베리파이, 서버 연동
- 데이터 통해 db 및 레포트 생성


#### *.ui -> *.py 변환 방법
1. shift + 우클릭 -> powershell 실행
2. ```pyside2-uic *.ui -o *.py```

#### NFC 관련 주의 사항
- 라즈베리파이에서 NFC를 사용할 경우: 
    main_LogIn.py 에서 NFCReader를 임포트할 때,
    
        from NFC.NFCReader import NFCReader
    
- 이외의 경우(windows에서 실행 테스트, 디버깅 등): 
    main_LogIn.py 에서 NFCReader를 임포트할 때
    
        from NFC.NFCReaderForTest import NFCReader


##### ~~내용 추가 예정~~
