import pprint 
import collections

from functions import *
from modules.apache import *
from modules.php7 import *
from modules.add_ppas import *

def createTasks(tasks, outputPath):

    od = collections.OrderedDict(sorted(tasks.items()))
    for (key, value) in od.items():
        eval('include_'+ key)(outputPath, value)
        pprint.pprint(key)
        pprint.pprint(value)
        if value is None:
            print(key +' not null')

