from django.conf import settings #importa as configurações do settings.py
from django.db import models #importa o módulo models do django
from django.utils import timezone #importa o módulo timezone do django

class Post(models.Model): #nosso objeto
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title