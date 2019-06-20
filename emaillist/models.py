from django.db import models

# Create your models here.
# ORM
class Emaillist(models.Model): # 모든 모델은 model.Model을 상속받는다.
    first_name = models.CharField(max_length=50)  # class 변수 , varchar로 db생성
    last_name = models.CharField(max_length=100)  # class 변수 , varchar로 db생성
    email = models.CharField(max_length=200)  # class 변수 , varchar로 db생성

    def __str__(self):
        return f'Emaillist({self.first_name}, {self.last_name},{self.email})'