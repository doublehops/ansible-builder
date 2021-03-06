import pprint 
import collections

from functions import *
from modules.webserver import *
from modules.php7 import *
from modules.database import *
from modules.add_ppas import *

def createTasks(tasks, outputPath):

    # Process tasks in a specific order. PPAs must be done first
    if 'add_ppas' in tasks:
        eval('include_add_ppas')(outputPath, tasks['add_ppas'])
        tasks.pop('add_ppas')

    # Process any remaining tasks where order not important
    for (key, value) in tasks.items():
        eval('include_'+ key)(outputPath, value)
        if value is None:
            print(key +' not null')

