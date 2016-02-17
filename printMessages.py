
def printPostInstall(ip, hostname, path):
    print('\n###########################################################################')
    print('##  You have just ran the installer.')
    print('##  Make sure you add the Vagrant host to your hosts file.')
    print("##  Eg. echo '"+ ip +"   "+ hostname +"' >> /etc/hosts")
    print("##  Add your ssh key to the new VM. 'ssh-copy-id vagrant@"+ hostname +"', password is `vagrant`")
    print("##  Run 'vagrant up' from '"+ path +"' to install the virtual machine onto your host.")
    print("##  Provision dev Vagrant host by typing 'dev/provision.sh local_dev'.")
    print('###########################################################################\n')
