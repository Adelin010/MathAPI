# create the venv

FILE=requirements.txt
DIR=venv

[ ! -f "$FILE" ] && touch "$FILE" && pip freeze > "$FILE"
[ ! -d "./venv/" ] && python3 -m venv "$DIR" 


source "./$DIR/bin/activate"

pip install -r "$FILE"




