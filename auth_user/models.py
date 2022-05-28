from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserDetail(models.Model):
    phone = models.CharField(max_length=12)
    iin = models.DecimalField(max_digits=12, decimal_places=0)
    email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name = 'UserDetail'
