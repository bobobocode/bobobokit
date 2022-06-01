#!/usr/bin/env sh

# BoBoBo

curdir=`pwd`
script_dir=$(cd "$(dirname "$0")"; pwd)

set -x

cp ~/.zshrc ${script_dir}/../install/etc/zshrc
cp ~/.vimrc ${script_dir}/../install/etc/vimrc
