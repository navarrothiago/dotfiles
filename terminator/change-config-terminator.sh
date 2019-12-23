#!/bin/bash
TERMINATOR_DIR=/home/$USER/.config/terminator

echo "Removendo arquivo config em /home/$USER/.config/terminator/config"
rm -r $TERMINATOR_DIR

echo "Crinado link para o arquivo $1"
#ln -s  /home/$USER/dotfiles/terminator/$1 /home/$USER/.config/terminator/config
mkdir $TERMINATOR_DIR
ln -s  /home/$USER/dotfiles/terminator/$1 $TERMINATOR_DIR/config

ls -la $TERMINATOR_DIR/config
 
