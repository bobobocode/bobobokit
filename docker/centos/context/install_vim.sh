#!/bin/bash

git clone https://github.com/vim/vim.git
cd vim
git checkout v8.2.0

./configure --with-features=huge \
            --enable-rubyinterp=yes \
            --enable-luainterp=yes \
            --enable-perlinterp=yes \
            --enable-python3interp=yes \
            --with-python3-config-dir=/usr/lib64/python3.6/config-3.6m-x86_64-linux-gnu \
            --enable-fontset=yes \
            --enable-cscope=yes \
            --enable-multibyte \
            --disable-gui \
            --enable-fail-if-missing \
            --prefix=/usr/local \
            --with-compiledby='Professional operations'

make VIMRUNTIMEDIR=/usr/local/share/vim/vim82 && make install
