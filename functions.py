import re, json, os.path, sys


def copyTemplate(source, dest, params):

    # Read from source file
    f = open(source, 'r')
    file = f.read()
    f.close()

    # Replace config options
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
