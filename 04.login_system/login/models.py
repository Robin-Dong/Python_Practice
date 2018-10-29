from django.db import models

# Create your models here.
class User(models.Model):
    gender = (
        ('male','Man'),
        ('female','Female'),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default= 'Man')
    #user_created_time
    c_time = models.DateTimeField(auto_now_add=True)
    has_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

    class Meta:
        ordering = ["c_time"]
        verbose_name = 'user'
        verbose_name_plural = 'users'

class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ":   " + self.code

    class Meta:

        ordering = ["-c_time"]
        verbose_name = "Validation code"
        verbose_name_plural = "Validation codes"