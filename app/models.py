from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to="avatars/")
    bio = models.TextField(max_length=500)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.name






























class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"({self.id}) {self.title}"