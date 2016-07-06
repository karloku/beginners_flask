import yaml
from mongoengine import connect

stream = file('config/mongoengine.yaml', 'r')    # 'document.yaml' contains a single YAML document.
data = yaml.load(stream)

connect(
    host=data['development']['host']
    )

from user import User