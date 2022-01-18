from django.db import models

# 1. 클래스
# 2. 모델 상속
# 3. 속성 => 변수 = OOOField 대입
class Course(models.Model):
    name = models.CharField(max_length=30)
    cnt = models.IntegerField()