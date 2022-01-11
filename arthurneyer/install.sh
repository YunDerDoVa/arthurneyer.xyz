#!/bin/bash

echo "Vous avez entré la commande \"$0, $1\""

if [[ $1 == 'all' ]]; then
  #statements
  python -m venv venv
elif [[ $1 == 'requirements' ]]; then
  #statements
  pip install -r requirements.txt
elif [[ $1 == 'statics' ]]; then
  #statements
  yarn install --modules-folder identity/static/node_modules/
elif [[ $1 == 'check' ]]; then
  #statements
  if [[ `ls identity/static/node_modules/ >&1 2>/dev/null` ]]; then
    #statements
    echo "Node Modules Exists"
  else
    echo "No Node Modules :p"
  fi
  # Second Tests
  if [[ `ls venv/bin/activate >&1 2>/dev/null` ]]; then
    #statements
    echo "Venv Exists"
  else
    echo "No Venv :p"
  fi
fi
