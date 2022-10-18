#!/bin/sh

echo "starting migration"
python src/manage.py makemigrations
python src/manage.py migrate

echo "loading fixtures"
echo "loading test user"
python src/manage.py loaddata src/fixtures/test
echo "loading articles"
python src/manage.py loaddata src/fixtures/articles
echo "loading zones"
python src/manage.py loaddata src/fixtures/zones
echo "loading monsters"
python src/manage.py loaddata src/fixtures/monsters
echo "loading items"
python src/manage.py loaddata src/fixtures/items
echo "loading menu"
python src/manage.py loaddata src/fixtures/menu
echo "loading quests"
python src/manage.py loaddata src/fixtures/quests
echo "loading skills"
python src/manage.py loaddata src/fixtures/skills


echo "starting server"
python src/manage.py runserver 0.0.0.0:8000