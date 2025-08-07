
#! bin/bash
function actv(){

    if [ "$1" == "-d" ]; then 
        deactivate
        echo -e "Virtual env deactivated..."
        return 
    fi

    if [ -z "$1" ]; then 
        echo "The venv must be provided in order to create the virtual env..."
        return
    fi 

    act_path="$(pwd)/${1}/bin/activate"

    [  ! -d "$1" ] && python3 -m venv "$1"
    source "$act_path"
}

if [ -z "$1" ]; then 
    echo -e "Select a mode \n -a (activate) followed by the name of the directory \n -d (deactivate)"
fi 

if [ "$1" == "-d" ]; then 
    actv "-d" 
elif [ "$1" == "-a" ]; then 
    name=$2
    [ -z "$2" ] && echo -e "No name has been provided for the virtual env \n default name: 'venv' " && name='venv'
    actv "$name"

fi 


