import shutil, pprint, subprocess, re

def copyTemplate(source, dest, params):

    # First copy source file to destination
    shutil.copyfile(source, dest)
    regexStr = ''

    for (key, value) in params.items():
        print("{} = {}".format(key, value))
        regexStr = regexStr + 's/{{'+ key +'}}/'+ re.escape(value) +'/g;'


    print('exp: '+ regexStr)

    subprocess.call(['sed -e "'+ regexStr +'" <'+ source +' > '+ dest], shell=True);
