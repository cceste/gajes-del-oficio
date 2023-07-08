import yaml

# Abrir el archivo YAML
with open('yaml/06-cisco.yml', 'r') as archivo:
    # Cargar el contenido YAML en un diccionario
    datos = yaml.safe_load(archivo)

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('06-cisco.j2')
output = template.render(datos=datos)
print(output)

import os
# directorio actual + mi nombre + .txt
filename = os.getcwd() + '/output/'+os.path.basename(__file__) + '.txt'
with open(filename,'w') as file:
    file.writelines(output)

