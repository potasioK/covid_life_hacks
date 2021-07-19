from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """A covid life hack topic input by user."""
    text = models.CharField(max_length=300)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """Return a string."""
        return self.text
    
class Entry(models.Model):
    """Specific covid life hacks."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
        
    def __str__(self):
        """Return a string."""
        if len(self.text) >= 75:
            return f"{self.text[:75]}..."
        else:
            return f"{self.text[:75]}" 
    
    
