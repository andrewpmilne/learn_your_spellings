from django.db import models
from django.conf import settings
from parent.models import Assignment  # link to parent assignments

class AssignedWord(models.Model):
    # The assignment this word belongs to
    assignment = models.ForeignKey(
        Assignment,
        on_delete=models.CASCADE,
        related_name='assigned_words'
    )
    # The child this word is for
    child = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='assigned_words'
    )
    # The spelling word
    word = models.CharField(max_length=255)
    # Whether the child can spell it correctly
    can_spell = models.BooleanField(default=False)
    # Optional example sentence for context
    example_sentence = models.TextField(blank=True)
    # Optional mnemonic to help remember
    mnemonic = models.TextField(blank=True)

    def __str__(self):
        return f"{self.word} ({self.child.username})"
