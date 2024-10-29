from django.db import models


class Todo(models.Model):

    PRIORITIES = {
        ('LOW', 'low'),
        ('MEDIUM', 'medium'),
        ('HIGH', 'high'),
    }

    content = models.CharField(max_length=400)
    priority = models.CharField(max_length=10, choices=PRIORITIES)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.content, self.done
