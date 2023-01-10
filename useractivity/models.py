from django.db import models

# Create your models here.



class User(models.Model):
    first_name = models.CharField(max_length=100,blank=True, null=True)
    last_name = models.CharField(max_length=100,blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender_choices = [('F','Female'),('M','Male'),('O','Other')]
    gender = models.CharField(max_length=1,choices=gender_choices)
    email = models.EmailField(unique=True,null=False,default=1)
    phone_number = models.CharField(max_length=12,unique=True,blank=True, null=True)
    type_choices = [('P','Primary'),('S','Secondary')]
    type = models.CharField(max_length=1,choices=type_choices)
    password = models.CharField(max_length=20,blank=True, null=True)
    confirm_password = models.CharField(max_length=20,blank=True, null=True)
    User_id = models.IntegerField(null=True,blank=True)


    def __str__(self):
        return self.email

        
