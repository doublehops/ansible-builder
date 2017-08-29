HOWTO

# Configure project

Todo

# Setting up hosts for provisioning

Firstly, modify `config.py` to suit your needs and run ./buildProvisioner.py. Note that the
output will be sent to the `outputPath` directory. Do not make this the same as the
config.py file.

This will create the host (in ansible_hosts) and required var files for one host. To create 
addtional hosts (perhaps remote) you need to add them to the ansible_hosts file and create 
corresponding var files for each role. You should also create an entry for each server in ~/.ssh/config

Setting up hosts is necessary for provisioning. Rather than use 
`vagrant provision` it is better to use the `dev/provision.sh <hostname>` 
as it allow you to add parameters and also provision remote servers.

In order to provision a host you need ssh access to it. It's best first to
create a record in your ~/.ssh/config file with a custom hostname and the IP
that matches the one you assigned in Vagrantfile. Something like:

 ``
 Host <host> # Just a shortcut/nickname. eg. VM IP address or alias configured in /etc/hosts.
 User vagrant # `vagrant` is the username for vagrant machines
 Hostname project.api # The hostname you have defined in /etc/hosts
 IdentityFile <working_dir>/.vagrant/somepath_to_private_key // find value with `vagrant ssh-config`
 ``

Once the ssh host has been configured, ssh into box with: `ssh <host>`. Once this
is successful you can then provision host.

# Run the provisioning script

The provisioning script lives in the dev path and you would call it
like `dev/provision.sh <host>` where <host> is the host defined
in ~/.ssh/config.
