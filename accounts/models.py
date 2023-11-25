from django.db import models
from django.core.validators import validate_email
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group


class CustomUser(AbstractUser):
    email = models.EmailField(
        unique=True,
        validators=[validate_email],
        error_messages={
            "unique": ("A user with that email already exists."),
        },
    )
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    

class Class(models.Model):
    class_name = models.CharField(max_length=255)

    def __str__(self):
        return self.class_name

class Stream(models.Model):
    class_name = models.ManyToManyField(Class,through="ClassStream")
    stream_name = models.CharField(max_length=225)

    def __str__(self):
        return self.stream_name

class ClassStream(models.Model):
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    stream_name = models.ForeignKey(Stream, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.class_name} {self.stream_name}"