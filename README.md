# like-lion

search.html 에서  20line 에서 
<td><a href="">{{s.company_name}}</a></td> 을 
<td><a href="{% url 'company_detail' company.id %}">{{">{{s.company_name}}</a></td> 이런식으로 수정하고 싶으나 
오류가 생김==> 해결해야함 



해야할 것:
카테고리 분류 / 
검색기능에 카테고리 별로 가능하도록 /
사용자 생성 % 좋아요 표시 % 개인 페이지에 정렬-> n:m /
모델보강(안에 적혀있음) /


css & 디자인


<clone 으로 받고 나서 해야 할 것>
1. venv 생성 
python -m venv venv 
2. pip 업그레이드 / django 설치
pip install --upgrade pip
pip install django
3. pillow 설치 
4. migrations
python manage.py migrations
python manage.py migrate
6. runserver 확인


