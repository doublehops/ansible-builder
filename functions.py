import re, json, os.path, sys, shutil, pprint


def copyTemplate(source, dest, params=[]):

    # Read from source file
    f = open(source, 'r')
    file = f.read()
    f.close()

    # Replace config options
    if len(params) > 0:
        for (key, value) in params.items():
            file = re.sub('{{'+ key +'}}', value, file)

    # Write new file
    f = open(dest, 'w')
    f.write(file)
    f.close()


def readJsonFile(source):

    file = source +'.json'
    data = '';

    if not os.path.exists(file):
        print('File not found: '+ file)
        sys.exit(2)

    try:
        with open(file) as json_file:
            data = json.load(json_file)
            json_file.close()
    except ValueError:
        print('Unable to parse JSON data: '+ file)

    return data


def createPath(path):

    os.makedirs(path, exist_ok=True)

def addRoleToPlaybook(outputPath, role):
    
    playbookFile = outputPath +'/provisioners/playbook.yml'
    copyTemplate(playbookFile, playbookFile, {'roles': '- '+ role +"\n    {{roles}}"})

def dd(obj):

    print('---------------------------------------------')
    pprint.pprint(obj)
    print('---------------------------------------------')
