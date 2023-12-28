from django.db import models

from game.models.system import System
from game.models.connectiontypes import ConnectionType

class Connection(models.Model):
    con_type = models.ForeignKey('ConnectionType', on_delete=models.CASCADE, related_name='type')
    systems = models.ManyToManyField('System', related_name='connections')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    class Meta:
        db_table = 'connections'
        verbose_name_plural = 'connections'

    def __str__(self):
        return '{0}: {1}'.format(self.con_type, ', '.join([system.name for system in self.systems.all()]))