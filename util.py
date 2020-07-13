import yaml
from typing import Dict



def readYAML( path: str ) -> Dict:

    if path[-4:] == '.yml':
        path = path[:-4]

    with open( f'{path}.yml', 'r' ) as f:
        data = yaml.load( f.read())

    return data