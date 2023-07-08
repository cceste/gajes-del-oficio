datos = [
  {
  'nombre' : 'Pelado',
  'edad' : '33'
  },
  {
  'nombre' : 'Keanu Reeves',
  'edad' : '58'
  },
]

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('04-basico-lista.j2')
output = template.render(datos=datos)
print(output)

import os
# directorio actual + mi nombre + .txt
filename = os.getcwd() + '/output/'+os.path.basename(__file__) + '.txt'
with open(filename,'w') as file:
    file.writelines(output)