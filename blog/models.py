from django.urls import reverse
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200, blank=False)
    text = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

class ExamQuestion(models.Model):
    question = models.TextField()
    answer_1 = models.CharField(max_length=255)
    answer_2 = models.CharField(max_length=255)
    answer_3 = models.CharField(max_length=255)
    answer_4 = models.CharField(max_length=255)
    correct_answer = models.PositiveSmallIntegerField(choices=[(1, 'Answer 1'), (2, 'Answer 2'), (3, 'Answer 3'), (4, 'Answer 4')])

    def __str__(self):
        return self.question

from django.contrib.auth.models import User

class Profile(models.Model):
    display_name = models.CharField(max_length=255, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    has_passed_exam = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
