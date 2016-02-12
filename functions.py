import re

def copyTemplate(source, dest, params):

    # Read from source file
    f = open(source, 'r')
    lines = f.read()
    f.close()

    # Replace config options
    for (key, value) in params.items():
        lines = re.sub('{{'+ key +'}}', value, lines)

    # Write new file
    f = open(dest, 'w')
    f.write(lines)
    f.close()
