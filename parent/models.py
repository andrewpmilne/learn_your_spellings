from django.db import models
from django.conf import settings

class Assignment(models.Model):
    # The parent who created the assignment
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='assignments_created'
    )
    # The child who this assignment is for
    child = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='assignments'
    )
    # Timestamp when the assignment was created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Assignment {self.id} for {self.child.username}"
