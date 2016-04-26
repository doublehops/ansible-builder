import pprint 

from functions import *
from modules.apache import *

def createTasks(tasks, outputPath):

    for (key, value) in tasks.items():
        eval('include_'+ key)(outputPath, value)
        pprint.pprint(key)
        pprint.pprint(value)
        if value is None:
            print(key +' not null')

