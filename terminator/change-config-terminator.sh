#!/bin/bash

echo "Removendo arquivo config em /home/$USER/.config/terminator/config"
rm /home/$USER/.config/terminator/config

echo "Crinado link para o arquivo $1"
ln -s  /work/dotfiles/terminator/$1 /home/$USER/.config/terminator/config

ls -la /home/$USER/.config/terminator/config
 
