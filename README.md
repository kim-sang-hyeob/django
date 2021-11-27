# like-lion
11/6 2주간 작업 완료
너무 허접해서 아쉽지만 수정&보완해 나가는거 뿐만 아니라 
장고에 대해서 실력향상을 한 뒤에 더 꾸며보는 것도 좋고...
이래저래 결과물이 조금 아쉽다

<다시 참조할 부분>
1. Queryset ==> 검색기능 ( https://docs.djangoproject.com/en/3.2/ref/models/querysets/ ) (이건 queryset 배운후에 다시 해결함 )
2. 페이징 기능 구현 ( 다른 분이 구현)
3. 모델이 조금 허접한점. -> 사용자 기능 추가 & n:m 기능을 추가해 보기 위해서 개인페이지 설정
4. 디자인 적인 부분에서 조금 마음에 안들거나 이미 구현한 부분에서 배울 부분이 많음 ( 다른분이 해결 )
5. 각각 좌표를 변혼해서 넣는다던지 사진을 여러개 첨가 할 수 있다던지 조금더 디테잃한 부분의 수정이필요해보임.



<clone 으로 받고 나서 해야 할 것>
1. venv 생성 
python -m venv venv 
2. pip 업그레이드 / django 설치
pip install --upgrade pip
pip install django
3. pillow 설치 
python -m pip install Pillow
5.python manage.py migrate
6. python manage.py createsuperuser
6. runserver 확인
7. 데이터 새로 넣어주기(admin에서 넣어주면 됨/company_data , category , product, 등등...)

