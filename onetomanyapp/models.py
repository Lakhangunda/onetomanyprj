from django.db import models

# Create your models here.
class University(models.Model):
    u_name=models.CharField(max_length=50)
    u_reg=models.CharField(max_length=50)
    u_address=models.CharField(max_length=50)
    u_email=models.EmailField()
    u_mobile=models.BigIntegerField()

    def __str__(self):
        return self.u_name

class College(models.Model):
    c_name=models.CharField(max_length=50)
    c_address=models.CharField(max_length=50)
    c_mobile=models.BigIntegerField()
    c_code=models.CharField(max_length=50)
    c_email=models.EmailField()

    def __str__(self):
        return self.c_name

    abc=models.ForeignKey(University,on_delete=models.CASCADE)