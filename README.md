음취헌 Piano Manager 🎹
=======

음취헌은 성균관대 자연과학캠퍼스 복지회관 3층에 있는 고전음악 감상실입니다. 주요 활동으로는 그랜드피아노 자유 이용, 주 2시간 내외의 운영, 매년 연주회 및 홈커밍데이 등 여러 행사가 있습니다. 교내 구성원이라면 누구든 가입할 수 있으며, 실원은 상시 모집 중입니다. 관련 문의 사항은 운영진에게 연락 바랍니다.  

이 repository는 음취헌 피아노 사용 기록용 프로그램입니다. 그랜드 피아노 이용 시 사용 기록을 데이터베이스에 기록하며, 이를 웹페이지를 통해 접근할 수 있도록 하는 것이 저희의 목표입니다. 원하는 기능이 있다면 제작진(아래 contributors)에게 메일 등으로 문의하거나, issue로 등록하면 됩니다.  

이 repository는 Raspberry Pi를 위해 만들어졌으며, 주된 기능은 다음과 같습니다.  
- 전화번호 혹은 NFC를 이용한 사용시간 체크
- 사용시간을 DB에 기록 (현재 aws 사용 중)

---

## ✔ Guideline
### Setting ⚙
해당 repository를 다운로드 받으세요. git을 이용해 받는 것을 권장합니다.  
git을 이용해서 받으려면, 우선 [git을 설치](https://git-scm.com/book/ko/v2/%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0-Git-%EC%84%A4%EC%B9%98)하고 원하는 경로에서 다음 명령어를 입력하세요.  
```shell
$ git clone https://github.com/dotoleeoak/skku-hun-2020
```
파일을 모두 받았으면, 제작진([@dotoleeoak](https://github.com/dotoleeoak))에게 db.py를 받아 model 폴더에 넣어주세요.  
(해당 파일은 보안의 문제로 GitHub에 업로드하지 않았습니다.)  

#### Font
font 폴더에 있는 <ins>배달의민족 주아</ins> 글꼴을 설치해주세요.

#### Python
이 프로그램은 Python3으로 동작합니다. [Python3을 설치](https://www.python.org/downloads/)해주세요.  
설치 후, 이 폴더를 열고 가상환경을 만들어주세요. (skku-hun-2020 하위 폴더로 생성하세요)
```shell
(Windows)
$ python -m venv hun

(macOS / Linux)
$ python3 -m venv hun
```
  
그 다음 가상환경을 활성화하고 필요한 패키지를 받아주세요.
```shell
(Windows cmd)
$ hun\Scripts\activate.bat
$ pip install -r requirements.txt

(Windows Powershell)
$ hun\Scripts\Activate.ps1
$ pip install -r requirements.txt

(macOS / Linux)
$ source hun/bin/activate
$ pip3 install -r requirements.txt
```

#### Run
가상환경이 활성화된 상태에서 Python으로 main.py를 실행하면 됩니다.
```shell
(Windows)
$ python main.py

(macOS / Linux)
$ python3 main.py
```
  
### Raspberry Pi & Pins 🔌

#### Raspberry Pi Setting

디스플레이의 번인과 전력 소모를 방지하기 위해 화면이 자동으로 꺼지는 시간을 1분으로 설정합니다.

``` shell
$ sudo vi /etc/lightdm/lightdm.conf
```
를 (또는 원하시는 다른 에디터로) 실행한 후, `#xserver-command=`를 `xserver-command=X -s 1 dpms` 변경해줍니다.

#### Pins

핀 번호에 대한 정보는 [여기](https://www.raspberrypi.org/documentation/usage/gpio/)에서 확인하세요.

- For Raspberry Pi Touch Screen

| Name   | Pin #   | Pin name     |
|:------:|:-------:|:------------:|
| 5V     | 2       | 5V           |
| GND    | 9       | Ground       |

- For Rasberry Pi Case with Cooler

| Name   | Pin #   | Pin name     |
|:------:|:-------:|:------------:|
| 5V     | 4       | 5V           |
| GND    | 6       | Ground       |

- For NFC Module(RFID-RC522)

| Name   | Pin #   | Pin name     |
|:------:|:-------:|:------------:|
| SDA    | 24      | GPIO8        |
| SCK    | 23      | GPIO11       |
| MOSI   | 19      | GPIO10       |
| MISO   | 21      | GPIO9        |
| IRQ    | None    | None         |
| GND    | 20      | Ground       |
| RST    | 22      | GPIO25       |
| 3.3V   | 17      | 3V3          |

### NFC 관련 주의 사항 ⚠
- 라즈베리파이에서 NFC를 사용할 경우:  
    ```python
    from nfc.nfc_reader import NFCReader
    ```
    
- 이외의 경우(windows에서 실행 테스트, 디버깅 등):  
    ```python
    from nfc.nfc_reader_for_test import NFCReader
    ```

---

## 😎 Contributors
- 김정원 [@threedalpeng](https://github.com/threedalpeng) - UI 구현, NFC 연결
- 김주현 [@juhy0987](https://github.com/juhy0987) - DB 구성  
- 이진영 [@HopangLee](https://github.com/HopangLee) - UI 디자인  
- 최재민 [@dotoleeoak](https://github.com/dotoleeoak) - UI, DB 연결  

---

> ~~내용 추가 예정~~
