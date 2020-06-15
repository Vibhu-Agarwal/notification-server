#!/usr/bin/env bash

rm -rf deploy/
mkdir deploy
cp -fR src/ deploy/

source venv/bin/activate
pip freeze > requirements.txt
sed -i '/pkg-resources/d' ./requirements.txt

git add requirements.txt
git commit -m "Updated requirements.txt"

cp requirements.txt deploy/src/requirements.txt

git checkout heroku-production-test
cp -fR deploy/src/* .
sed -i '14iimport django_heroku' notification_server/settings.py
echo "# Activate Django-Heroku." >> notification_server/settings.py
echo "django_heroku.settings(locals())" >> notification_server/settings.py

rm -rf deploy/

source prod-venv/bin/activate
pip install -r requirements.txt
pip freeze > requirements.txt
sed -i '/pkg-resources/d' ./requirements.txt

git status
git add -A
git commit -m "Deploy"
git push -f

rm -rf notification_server/__pycache__/
rm -rf __pycache__/
rm -rf notifications/
rm db.sqlite3

git checkout master
source venv/bin/activate
clear
