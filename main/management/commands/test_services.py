from django.core.management.base import BaseCommand
from main.services import *

# Se ejecuta usando python manage.py test_client

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        #crear_user('44.444.444-4', 'Cuatro', 'Jor', 'ccc@bbb.ccc', '123456', '123456', 'Pasaje Nueve, Chile')
        #editar_user('44.444.444-4', 'Cuatro', 'Jordan', 'ccc@bbb.ccc', '654321', '654321', 'Street One, Usa', '987654321')
        #crear_inmueble('Casa Grande blanca en Villa Alemaan', 'Esta es la descriocion de propiedad', 90, 180, 3, 3, 2, 'Calle 22', 450000, 'casa', 'Villa Alemana', '22.2222.222-2')
        #eliminar_inmueble(1)
        editar_inmueble(3, 'Parcela Amarilla en Villa Alemana', 'Hermosa parcela amarilla en la esquina', 90, 180, 3, 3, 2, 'Calle 22', 750000, 'parcela', 'Villa Alemana', '22.2222.222-2')
        return 'Resultó'