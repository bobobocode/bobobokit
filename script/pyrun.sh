#!/usr/bin/env bash

# BoBoBo

set -ex

curdir=`pwd`
basedir=$(cd "$(dirname "$0")"; pwd)

script_conf= 
script_params=
while getopts 't:c:p:' opts
do
    case $opts in
    t)
        target=$OPTARG;;
    c)
        script_conf=$OPTARG;;
    p)
        script_params=$OPTARG;;
    ?)
        echo "run.sh -s <script>"
        exit 1
    esac
done

cmd_last_part=
add_cmd_last_part(){
    cmd_last_part="${cmd_last_part} $1 $2"
}

cd ${basedir}
if [ "${script_conf}" != "" ]; then
    if [ ! -f ${script_conf} ]; then
        echo "${script_conf} not exists."
        exit 1
    else
        add_cmd_last_part "-c" ${script_conf}
    fi
fi

if [ "${script_params}" != "" ]; then
    add_cmd_last_part "-p" "${script_params//,/ }"
fi

if [ -d ./env/bobobokit-venv ]; then
    source ./env/bobobokit-venv/bin/activate
else
    python3 -m venv ./env/bobobokit-venv
    echo "export PYTHONPATH=${PYTHONPATH}:${basedir}/.." >> ./env/bobobokit-venv/bin/activate
    source ./env/bobobokit-venv/bin/activate
    pip install -r ./env/py-requirements.txt
fi

if echo "${target}" | grep -q -E '\.py$'
then
    target="python/"${target}
    python ./${target} ${cmd_last_part}
fi

cd ${curdir}
