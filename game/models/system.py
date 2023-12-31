from django.db import models
from game.models.system_type import SystemType

class System(models.Model):
    name = models.CharField(max_length=50)
    sys_type = models.ForeignKey('SystemType', on_delete=models.CASCADE, related_name='systems')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'systems'
        verbose_name_plural = 'systems'
    def __str__(self):
        return '{0}: {1}'.format(self.sys_type.name, self.name)