#!/bin/bash

find . ! -path '*svn*' ! -path '*lib*' ! -path '*target*' ! -path '*class' ! -path '*pyc' ! -path '*idea*' ! -path '*swp' ! -path '*iml' | sed -e 's;[^/]*/;|____;g;s;____|; |;g'
