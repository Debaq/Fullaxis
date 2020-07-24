import os

def listPlugins():
    os.listdir("plugins")
modules = ["sys","os","platform","random","time","functools"]

for library in modules:
try:
    exec("import {module}".format(module=library))
except Exception as e:
    print(e)
print(sys.argv)python 
impo