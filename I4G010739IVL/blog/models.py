from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length=23)
    text = models.TextField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE )
    created_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def __str__(self):
        return self.text

    # def __str__(self):
    #     return self.author

    # def __str__(self):
    #     return self.created_date

    # def __str__(self):
    #     return self.published_date

