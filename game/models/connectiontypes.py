from django.db import models

class ConnectionType(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'connection_types'
        verbose_name_plural = 'connection_types'

    def __str__(self):
        return self.name