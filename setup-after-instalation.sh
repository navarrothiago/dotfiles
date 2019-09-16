sudo apt-get update
sudo apt-get upgrade

echo "Install docker"
sudo apt-get remove docker docker-engine docker.io containerd runc
sudo apt-get install     apt-transport-https     ca-certificates     curl     gnupg-agent     software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository    "deb [arch=amd64] https://download.docker.com/linux/ubuntu  $(lsb_release -cs)  stable"
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io 
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker

echo "Install packages" 
sudo apt-get install terminator gitk meld vim git subversion remmina tmux wireshark network-manager-vpnc-gnome openvpn cppcheck fish default-jre eclipse-pydev eclipse-cdt

echo "Create /work"
sudo mkdir /work
sudo chown navarro:navarro /work
cd /work 

echo "Download dotfiles repository"
git clone http://github.com/navarrothiago/dotfiles

echo "Create bashrc link"
rm $HOME/.bashrc
ln -s /work/dotfiles/bash/.bashrc $HOME/.bashrc

#echo "Create terminator config link"
mkdir -p $HOME/.config/terminator/
ln -s /work/dotfiles/terminator/config $HOME/.config/terminator/config

echo "Create vim link"
ln -s /work/dotfiles/vim $HOME/.vim

echo "Create fish function link"
mkdir -p $HOME/.config/fish
ln -s /work/dotfiles/fish/functions $HOME/.config/fish/functions

echo "Create git link" 
ln -s /work/dotfiles/git/.* $HOME/.  

