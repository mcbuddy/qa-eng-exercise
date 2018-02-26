# -*- mode: ruby -*-
# vi: set ft=ruby :

NUM_NODES = [(ENV['NUM_NODES'] || 2).to_i, 4].min
PRIVATE_NETWORK_PREFIX = (ENV['PRIVATE_NETWORK_PREFIX'] || "10.99.0.1")

Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-16.04"

  (1..NUM_NODES).each do |index|
    config.vm.define "node#{index}" do |machine|
      machine.vm.hostname = "node#{index}"
      machine.vm.network :private_network, :ip => "#{PRIVATE_NETWORK_PREFIX}#{index}"
      machine.vm.provision :hosts, :sync_hosts => true
      if index == NUM_NODES
        machine.vm.provision :ansible do |ansible|
		  ansible.limit = "all"
		  ansible.playbook = "provision.yml"
	    end
	  end
    end
  end
end
