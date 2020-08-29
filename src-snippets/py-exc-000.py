modulename = __name__
modulefilename = __file__


# import sys
# print(sys.modules)


# import module_name as module_name
import importlib
pylib000 = importlib.import_module('py-lib-000')


print(modulename)
print(modulefilename)
print("Hello, World!")

# print(pylib000.modulefilename)


