from django.db import models

# Create your models here.
class User(models.Model):
    user_id=models.CharField(max_length=100)
    user_email= models.EmailField(null=True)
    user_phonenumber= models.IntegerField()
    user_joined_date = models.DateField(auto_now_add=True,null=True)
    user_address=models.CharField(max_length=100)
    user_last_activetime = models.TimeField(auto_now=True)
    user_areaofinterest=models.CharField(max_length=40)
    user_cgpa= models.DecimalField(max_digits=3, decimal_places=2)
    user_arrear= models.IntegerField()

    class Meta:
        db_table = 'my_user'