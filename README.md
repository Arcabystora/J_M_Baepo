# J_M_Baepo

장고를 이용한 제이라움 키오스크 클론 코딩입니다.

---

## 실행

python 3.12 이상 버전 설치 후

```
# 가상환경 생성
python -m venv venv

# 가상환경 실행
./venv/Scripts/activate

# 필요 package 설치
pip install django
pip install djangorestframework

# migrate 명령어로 DB 생성
python manage.py makemigrations
python manage.py migrate

# 서버 실행
python manage.py runserver

# 브라우저로 접속
http://127.0.0.1:8000/main/
```
