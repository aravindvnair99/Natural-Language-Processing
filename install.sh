#!/bin/bash

python -m pip install --upgrade pip
pip install virtualenv
virtualenv NLP
. NLP/Scripts/activate
pip install -r requirements.txt
python -m nltk.downloader all
