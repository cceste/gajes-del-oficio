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

