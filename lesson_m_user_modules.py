#python searches for a file and import it. note that without __main__ the import is executing the global scope code.
import lesson_m_module
#i can import individual functions from a file
#from lesson_m_module import jargon
#i can put a file inside a directory. a directory is a module
from directory_is_module import file_b
#i can import a directory and it will import __init__.py
import directory_is_module

def vogon():
    return None

directory_is_module.herring()

print('susanoo!!!!')
print(f'executing: {__name__}')