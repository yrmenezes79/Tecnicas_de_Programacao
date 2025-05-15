import sys
import pkgutil

std_lib_paths = [p for p in sys.path if 'site-packages' not in p]

# Lista os módulos nesses caminhos
for importer, modname, ispkg in pkgutil.iter_modules(std_lib_paths):
    print(modname)
