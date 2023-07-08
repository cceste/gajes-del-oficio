nombre = 'Pelado'
edad = '33'

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('01-basico.j2')
output = template.render(nombre=nombre, edad=edad)
print(output)


