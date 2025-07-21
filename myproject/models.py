from django.db import models

class Entry(models.Model):
    """
    Represents a single entry with a title, content, and creation timestamp.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # Automatically sets the creation timestamp

    def __str__(self):
        """
        String representation of the Entry object.
        """
        return self.title

    class Meta:
        """
        Meta options for the Entry model.
        """
        verbose_name_plural = "Entries" # Correct plural name for admin interface
        ordering = ['-created_at'] # Order entries by creation date, newest first
