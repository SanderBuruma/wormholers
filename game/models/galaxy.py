from django.db import models, transaction

from game.models.system import System

class Galaxy(models.Model):
    name = models.CharField(max_length=50)
    systems = models.ManyToManyField('System', related_name='systems')

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'galaxies'
        verbose_name_plural = 'galaxies'
        
    def __str__(self):
        return self.name