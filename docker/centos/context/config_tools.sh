#!/bin/bash

git clone https://github.com/bobobozzz/bobobokit.git
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
git clone https://github.com/bobobozzz/snippets.git ~/.vim/snippets
git clone https://github.com/otsaloma/markdown-css.git ~/markdown-css

rm -f ~/.vimrc
cp ./bobobokit/equip/cfg/vimrc ~/.vimrc

vim +PluginInstall +qall

cd ~/.vim/bundle/YouCompleteMe
./install.py --all
cd /var/code

echo -e "y\n" > input.tmp
./install_ohmyzsh.sh < input.tmp
rm -f input.tmp

rm -f ~/.zshrc
cp ./bobobokit/equip/cfg/zshrc ~/.zshrc
