from django.db import models
from django.contrib.auth.models import User


class Season(models.Model):
    season_name = models.CharField(max_length=200)
    time_start = models.DateField()
    time_end = models.DateField()
    profit = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.season_name
    


class Land(models.Model):
    land_name = models.CharField(max_length=200)
    land_pos = models.CharField(max_length=1000)
    land_area = models.FloatField()
    land_pH = models.FloatField()
    land_doAm = models.DecimalField(max_digits=5, decimal_places=2)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    def __str__(self):
        return self.land_name


class Plant(models.Model):
    plant_name = models.CharField(max_length=200)
    plant_dev = models.DecimalField(max_digits=5, decimal_places=2, help_text="Thời gian phát triển (tháng)")

    # Use CharField with limited choices for older Django versions
    plant_type = models.CharField(max_length=1, choices=[
        ('0', 'Cây lương thực'),
        ('1', 'Cây ăn quả'),
        ('2', 'Cây rau củ'),
    ])
    plant_ND = models.DecimalField(max_digits=5, decimal_places=2, help_text="Nồng độ khoáng chất cần thiết")
    plant_bp = models.IntegerField(help_text="Chu kỳ bón phân (ngày)")
    land = models.ForeignKey(Land, on_delete=models.CASCADE)

    def __str__(self):
        return self.plant_name
    
    
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    ngaysinh = models.DateField(auto_now=False, auto_now_add=False)
    doituong = models.BooleanField()
    sdt = models.CharField(max_length=20)
    diachi = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, null=True, blank=False)
    price = models.CharField(max_length=200, null=True)
    link = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True)
    adress = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name
    
    
    @property
    def IMG_URL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    


    # Create your models here.
class thitruong (models.Model):
    id_thitruong= models.AutoField(primary_key= True)
    id_caytrong = models.CharField(max_length=10, null=False)
    ten_caytrong= models.CharField(max_length=50, null=False)
    ten_thitruong=models.CharField(max_length=50, null=False)
    ten_nguoiban=models.CharField(max_length=50, null=False)
    gia=models.BigIntegerField(null=True)
def __str__(self):
    return f"{self.id_thitruong}, {self.id_caytrong}, {self.ten_caytrong}, {self.ten_thitruong}, {self.ten_nguoiban}, {self.gia}"

class thitruong_ban (models.Model):
    id_thitruong= models.AutoField(primary_key= True)
    ten_caytrong= models.CharField(max_length=50, null=False)
    ten_thitruong=models.CharField(max_length=50, null=False)
    gia=models.BigIntegerField(null=True)



class Contact(models.Model):
    id_user = models.AutoField(primary_key=True, blank=False)
    hoten = models.CharField(max_length=255)
    email = models.EmailField()
    loinhan = models.TextField()

    def __int__(self):
        return self.id_user





