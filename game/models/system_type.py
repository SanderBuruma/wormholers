from django.db import models

class SystemType(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'system_types'
        verbose_name_plural = 'system_types'
    def __str__(self):
        return self.name