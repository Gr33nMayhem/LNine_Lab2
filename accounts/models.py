from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    LANGUAGE_CHOICE = [
        ('en', 'English'),
        ('es', 'Spanish'),
    ]
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICE, default='en')
    current_profile = models.ForeignKey('UserProfile', on_delete=models.SET_NULL, null=True, blank=True, default=None)

    def __str__(self):
        return self.email


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='profiles')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='profiles')

    language = models.CharField(max_length=2, choices=CustomUser.LANGUAGE_CHOICE, default='en')
    class Meta:
        unique_together = ('user', 'company')

    def __str__(self):
        return f'{self.user} - {self.company}'
