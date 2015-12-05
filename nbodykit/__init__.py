from nbodykit.plugins import load
import os.path
path = os.path.abspath(os.path.dirname(__file__))

builtins = ['datasource/', 'storage/']

for plugin in builtins:
    load(os.path.join(path, plugin))
 
