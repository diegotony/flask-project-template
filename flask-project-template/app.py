import yaml

with open('data.yml','r') as f:
    data = yaml.load(f)
    print(data)


import json
json.dumps()