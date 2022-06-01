#!/usr/bin/env sh

# BoBoBo

curdir=`pwd`
scriptdir=$(cd "$(dirname "$0")"; pwd)

rootdir=${curdir}
while getopts 'd:' opts
do
    case $opts in
    d)
        rootdir=$OPTARG;;
    esac
done

for project_dir in `ls ${rootdir}`
do
    if [ -d ${project_dir} ]; then
        cd ${project_dir}
        if [ -d ./.git ]; then
            echo "Bak "${project_dir}
            git fetch --all
            echo "\r\n"
        else
            for level2 in `ls .`
            do
                cd ${level2}
                if [ -d ./.git ]; then
                    echo "Bak "${level2}
                    git fetch --all
                    echo "\r\n"
                fi
                cd ..
            done
        fi
        cd ..
    fi
done
