from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    MALE = 1
    FEMALE = 2
    UNSET = 3
    GENDER_CHOICES = [(MALE, "male"), (FEMALE, "female"), (UNSET, "unset")]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=32, blank=True)
    avatar = models.ImageField(verbose_name='Avatar', upload_to='avatars/', blank=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=UNSET)

    class Meta:
        db_table = 'user_profiles'
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

