#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
#echo $DIR

#sudo apt-get update
#pip install --upgrade pip
#sudo apt-get install python-pip

venv="$DIR/venv"
virtualenv $venv
source $venv/bin/activate

pip install virtualenv
pip install nltk
python -c "import nltk; nltk.download('punkt');"
         