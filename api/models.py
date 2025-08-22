import datetime

from django.db import models

# Create your models here.

#공지사항 또는 뉴스 테이블
class Notice(models.Model):
    title = models.CharField(max_length=50, null=False) #공지 사항 제목
    categori = models.CharField(max_length=10, null=False, default='notice')#분류 notice, news
    content = models.TextField(null=True)#본문 내용 ( 게시판 형태 ) 이미지 추가 구현 예정 html로 기록
    upload_date = models.DateTimeField(auto_now=True, default=datetime.datetime.now())#게시글 업로드 (2025.04.01 11:23)
    update_date = models.DateTimeField(auto_now=True)# 상위 upload_date와 동일

    def __str__(self):
        return self.pk

#협력기관 테이블
class Cooperating(models.Model):
    title = models.CharField(max_length=10, null=False) #협력 기관 이름
    img = models.ImageField(upload_to='img/Cooperating') #기본 이미지 사이즈 제한 논의 필요
    thumnail = models.ImageField(upload_to='img/Cooperating/thm') #기본 이미지 사용 또는 섬네일 전용 이미지 사용 여부 - 1안의 경우 자동으로 축소방안
    upload_date = models.DateTimeField(auto_now=True, default=datetime.datetime.now())  # 게시글 업로드 (2025.04.01 11:23)
    update_date = models.DateTimeField(auto_now=True)  # 상위 upload_date와 동일

    def __str__(self):
        return self.img

#문의 시 데이터 축적(메일 발송 형식 x)
class Mail_table(models.Model):
    name = models.CharField(max_length=10, null=False)  #작성자 명
    phone = models.CharField(max_length=15, null=False)
    company_name = models.CharField(max_length=100, null=True) #회사 명
    e_mail = models.CharField(max_length=50, null=False) # 담당자 메일
    upload_file = models.FileField(upload_to='connect_data/{company_name}') #파일 제한 및 유형 협의 필요
    content = models.TextField(null=True) #데이터 사용 html활용 할 예정이나 가져다 쓸것 있나 찾아봐야함 게시판 형태로 진행 예정
    upload_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name




# 이미지 사용 하는 테이블의 경우 저장시 이미지 자르는 기능 추가 필요! 필수 :) 안하면 망해요
# 파일 저장 하는 부분도 동일 하게 진행 하여야함.