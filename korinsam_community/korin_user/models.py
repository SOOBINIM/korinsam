from django.db import models

class Kuser(models.Model):
    user_name = models.CharField(max_length=32, verbose_name='사용자 이름')
    user_id = models.CharField(max_length=32, verbose_name='아이디')
    user_pw = models.CharField(max_length=128, verbose_name='비밀번호')
    user_re_pw = models.CharField(max_length=128, verbose_name='비밀번호 확인')
    
    def __str__(self):
        return self.user_name
    