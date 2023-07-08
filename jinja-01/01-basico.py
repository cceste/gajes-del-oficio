from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('basico.j2')
output = template.render(nombre='Pelado', edad=33)
print(output)


