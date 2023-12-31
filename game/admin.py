from django.contrib import admin

# Register your models here.
from game.models.galaxy import Galaxy
from game.models.system import System
from game.models.system_type import SystemType
from game.models.connection import Connection
from game.models.connectiontypes import ConnectionType

admin.site.register([Galaxy, System, Connection, ConnectionType, SystemType])