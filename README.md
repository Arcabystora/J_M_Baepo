
# J_M_Baepo

현암교회 카페 제이라움의 키오스킙니다.

---

## 실행
python 3.12 이상 버전 설치 후

```
# 가상환경 생성
python -m venv venv

# 가상환경 실행
source ./venv/Scripts/activate

# 필요 package 설치
pip install -r requirements.txt

# migrate 명령어로 DB 생성
python manage.py makemigrations
python manage.py migrate
