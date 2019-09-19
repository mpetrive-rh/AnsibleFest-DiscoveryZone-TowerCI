# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |cluster|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.

  # Every Vagrant virtual environment requires a box to build off of./


  # cluster.vm.define "ldapvm" do |config|
  #  config.vm.box = "centos/7"
  #  config.ssh.insert_key = false
  #  config.vm.provider :virtualbox do |vb, override|
  #    vb.customize ["modifyvm", :id, "--memory", "512"]
  #    vb.customize ["modifyvm", :id, "--cpus", "1"]
  #  end
  #  config.vm.hostname = "ldapvm"
  #  config.vm.network :private_network, ip: "172.16.2.53"
  #  config.vm.provision "ansible" do |ansible|
  #    ansible.playbook = "site.yml"
  #    ansible.groups = {
  #      "tag_Vagrant_True" => ["ldapvm"],
  #      "tag_Vagrant_local" => ["ldapvm"],
  #      "tag_Name_ldapvm" => ["ldapvm"],
  #    }
  #  end
  # end

cluster.vm.define "gitlab" do |config|
  config.vm.box = "centos/7"
  config.ssh.insert_key = false
  ##config.hostmanager.enabled = true
  config.vm.provider :virtualbox do |vb, override|
    vb.customize ["modifyvm", :id, "--memory", "2048"]
    vb.customize ["modifyvm", :id, "--cpus", "2"]
  end

  config.vm.provider :libvirt do |libvirt|
    libvirt.memory = 4096
    libvirt.cpus = 2
  end  #end libvirt provider

  config.vm.hostname = "gitlab"
  config.vm.network :private_network, ip: "172.16.2.50"

  config.vm.network "forwarded_port", guest: 443, host: 5443, host_ip: "192.168.1.100"

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "site.yml"
    ansible.groups = {
      "tag_Vagrant_True" => ["gitlab"],
      "tag_Vagrant_local" => ["gitlab"],
      "tag_Name_gitlab" => ["gitlab"],
    }
  end
end

cluster.vm.define "gitlab-runner" do |config|
  config.vm.box = "centos/7"
  ##config.ssh.insert_key = false
  #config.hostmanager.enabled = true
  config.vm.provider :virtualbox do |vb, override|
    vb.customize ["modifyvm", :id, "--memory", "512"]
    vb.customize ["modifyvm", :id, "--cpus", "2"]
  end
  
  config.vm.provider :libvirt do |libvirt|
    libvirt.memory = 4096
    libvirt.cpus = 2
  end  

  config.vm.hostname = "gitlab-runner"
  config.vm.network :private_network, ip: "172.16.2.51"
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "site.yml"
    ansible.groups = {
      "tag_Vagrant_True" => ["gitlab-runner"],
      "tag_Vagrant_local" => ["gitlab-runner"],
      "tag_Name_gitlab-runner" => ["gitlab-runner"],
    }
  end
end

cluster.vm.define "ansible-tower" do |config|
  config.vm.box = "centos/7"
  ##config.ssh.insert_key = false
  #config.hostmanager.enabled = true
  config.vm.provider :virtualbox do |vb, override|
    vb.customize ["modifyvm", :id, "--memory", "2048"]
    vb.customize ["modifyvm", :id, "--cpus", "2"]
  end
  config.vm.hostname = "ansible-tower"
  config.vm.network :private_network, ip: "172.16.2.52"
  config.vm.network :forwarded_port, guest: 443, host: 4443
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "site.yml"
    ansible.groups = {
      "tag_Vagrant_True" => ["ansible-tower"],
      "tag_Vagrant_local" => ["ansible-tower"],
      "tag_Name_ansible-tower" => ["ansible-tower"],
    }
  end
end

end
