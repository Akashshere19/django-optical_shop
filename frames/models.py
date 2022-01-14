from django.db import models
from datetime import date

# Create your models here.
class Optical(models.Model):
    Company_name = models.CharField(max_length=50)
    frame_pic= models.ImageField(upload_to='profile_pic/FramePic/',null=True)
    #customer_img = models.ImageField(upload_to='images/',null=True)
    status=models.BooleanField(default=False)
    Eyes_checkup_date = models.DateField()
    Glass_delivery_date=models.DateField()
# for model select
    MODEL_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

    Model_size = models.CharField(max_length=1, choices=MODEL_SIZES,null=True)
    # for gender select
    GenderType = (('M','Male'),('F','Female'))
    Gender_select = models.CharField(blank=True, choices=GenderType, max_length=10)

    # frame size select
    frame_size = ('50','53')
    Gender_select = models.IntegerField( n for n in range(50 ,60))



    def __str__(self):
        return self.Company_name
