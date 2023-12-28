from django.db import models

class System(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'systems'
        verbose_name_plural = 'systems'
    def __str__(self):
        return self.name