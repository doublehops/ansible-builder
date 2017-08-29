import re, json, os.path, sys, shutil, pprint

# Copy a template and replacing vars
# Expects dest to include filename
def copyTemplate(source, dest, params=[]):

    if not os.path.isfile(source):
        printException("Source does not exist: "+ source)
        sys.exit(0)

    # Ensure destination path exists
    pos = dest.rfind('/')
    destPath = dest[:pos]
    if not os.path.isdir(destPath):
        os.makedirs(destPath)

    # Read from source file
    f = open(source, 'r')
    file = f.read()
    f.close()

    # Replace config options
    if len(params) > 0:
        for (key, value) in params.items():
            file = re.sub('{{'+ key +'}}', value, file)

    # Write new file
    try:
        f = open(dest, 'w')
        f.write(file)
        f.close()
    except IOError:
        printException("Cannot write to destination: "+ dest)
        raise


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
        printException('Unable to parse JSON data: '+ file)

    return data


def createPath(path):

    try:
        os.makedirs(path, exist_ok=True)
    except:
        print("unable to create path: "+ path)

def addRoleToPlaybook(outputPath, role):

    playbookFile = outputPath +'/provisioners/playbook.yml'
    copyTemplate(playbookFile, playbookFile, {'roles': '- '+ role +"\n    {{roles}}"})

def dd(obj):

    print('---------------------------------------------')
    pprint.pprint(obj)
    print('---------------------------------------------')

def getFamily(operatingSystem):

    redhatFamily = ['redhat','centos6','centos7']
    debianFamily = ['debian','ubuntu','ubuntu16']

    if operatingSystem in redhatFamily:
        return 'redhat'
    if operatingSystem in debianFamily:
        return 'debian'

# Exception messages are hard to see. This
# attempts to highlight them
def printException(msg):

    print(">>>>>>>>>>  "+ msg  +"  <<<<<<<<<<")
    sys.exit(0)
