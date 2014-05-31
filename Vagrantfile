VAGRANTFILE_API_VERSION = "2"

Vagrant::Config.run(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "hashicorp/precise32"
  
  config.vm.network "forwarded_port", guest: 8000, host: 8000

  config.vm.synced_folder ".", "/home/vagrant/angelhack/"

  config.ssh.private_key_path = "~/.ssh/id_rsa"

end
