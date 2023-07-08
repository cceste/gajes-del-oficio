from jinja2 import Environment, FileSystemLoader
import os
import yaml

template_file = '07-ios.j2'
yaml_file = '07-ios.yml'
output_file = os.getcwd() + '/output/'+os.path.basename(__file__) + '.txt'

with open('./yaml/'+yaml_file, 'r') as archivo:
    datos = yaml.safe_load(archivo)

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template(template_file)
output = template.render(datos=datos)
print(output)

with open(output_file, 'w') as file:
    file.writelines(output)
