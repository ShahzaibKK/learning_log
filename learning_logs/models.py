from django.db import models


# Create your models here.
class Topic(models.Model):
    """A Topic the user is learning about"""

    text = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        """return  a string represtation of the model"""
        return self.text


class Entry(models.Model):
    """something more about releted topic"""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        """Return a simple string representing the entry"""
        return f"{self.text[:50]}..."
