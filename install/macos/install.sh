#!/bin/sh

# This cannot work for the network reason.
#sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
#/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

while getopts 'r' opts
do
    case $opts in
    r)
        reinstall=1;;
    esac
done

brew install vim
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

brew install docker
brew install docker-machine
brew install docker-compose
brew install docker-swarm

brew install autojump
brew cask install dash
brew cask install iterm2

brew install wget
brew install plantuml
brew install pandoc
brew install nmap
brew install ctags-exuberant
brew install cscope
brew install telnet
brew install iftop

brew install cmake
brew install golang
brew install openjdk
brew install npm
brew install mysql-connector-c++
brew install tmux


brew cask install firefox
brew cask install google-chrome
brew cask install gitter

if [[ ! ${reinstall} ]]; then
    sudo ln -sfn /usr/local/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk
    defaults write com.apple.finder _FXShowPosixPathInTitle -bool YES
    xcode-select --install
fi

git clone https://github.com/Kashomon/vimporter.git ~/.vim/plugin/vimporter
git clone git@github.com:bobobozzz/snippets.git ~/.vim/snippets
git clone https://github.com/otsaloma/markdown-css.git ~/markdown-css

brew cask install osxfuse
brew install sshfs

brew cask install virtualbox
brew cask install docker

# React Native
brew install --cask osxfuse
brew install watchman
brew install cocoapods
npm install -g yarn
brew install react-native-cli
