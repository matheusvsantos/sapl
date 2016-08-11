#!/user/bin/python
from django.contrib.auth.models import Group

names = ['Administrador', 'Autor', 'Operador de Administração',
         'Operador de Comissão', 'Operador de Matéria Legislativa',
         'Operador de Norma Juridica', 'Operador de Protocolo',
         'Operador de Sessão', 'Operador Geral']

for n in names:
    Group.objects.create(name=n)
