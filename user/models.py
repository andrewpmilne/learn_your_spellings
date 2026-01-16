from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom user model with just Parent and Child roles
class User(AbstractUser):
    ROLE_CHOICES = [
        ('parent', 'Parent'),
        ('child', 'Child'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.role})"


# Link parents to children
class AdultChildLink(models.Model):
    adult = models.ForeignKey(User, on_delete=models.CASCADE, related_name='children')
    child = models.ForeignKey(User, on_delete=models.CASCADE, related_name='parents')

    def __str__(self):
        return f"{self.adult.username} -> {self.child.username}"
