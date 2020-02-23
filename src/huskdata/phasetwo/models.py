from django.db import models
from django.contrib.auth.models import User
class UserUploads(models.Model):
    username = models.ForeignKey(to=User,
                                 to_field='username',
                                 on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    file_comming = models.FileField(upload_to=f'{username}/')
