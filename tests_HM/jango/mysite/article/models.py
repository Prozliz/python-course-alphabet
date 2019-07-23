from django.db import models
from account.models import Profile


class Article(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=5000)

    def __str__(self):
        return self.title
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender= Article)
def notify_author(sedner,instance,**kwargs):
    subject ='Article Created'
    body = 'Your all article created'
    send_from = settings.DEFAULT_FROM_EMAIL
    send_to = 'vera1996111@gmail.com'
    send_mail('Articles Created')