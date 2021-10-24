from django.db import models

# Create your models here.

class Company_Data(models.Model):
    '''회사 정보 '''

    # 검색 기능에는 회사이름 , 지역 , 속한 제품명 3가지를 통해서 구현할 예정임 -> 어떤식으로 모델을 나누는게 좋을지 아직 못정함

    # 회사 이름
    company_name=models.CharField(
        max_length=100,
        blank=False,
        verbose_name='회사 이름', )
    # 대표자
    ceo_of_company = models.CharField(
        max_length=50,
        verbose_name='회사 대표',)
    #설립연도
    year_of_establishment = models.CharField(
        max_length=15,
    verbose_name='설립 연도',)
    #지역
    area=models.CharField(
        max_length=50,
        verbose_name='지역'
        )
    #전화번호
    number=models.CharField(
        max_length=12,
        verbose_name='전화번호',
        )
    #이메일주소
    email_address=models.CharField(
        max_length=50,
        verbose_name='이메일 주소',
        )
    #홈페이지
    homepage=models.CharField(
        max_length=30,
        verbose_name='홈페이지',
        )
    #회사소개
    introduce_company=models.TextField(
        verbose_name='회사 소개'
    )#제한 자체를 두지 않기 위해서 Textfield 사용.