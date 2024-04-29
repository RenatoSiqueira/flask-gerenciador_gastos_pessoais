export FLASK_APP=api
export FLASK_ENV=development
flask run --debug

flask db init
flask db migrate -m "Initial migration."
flask db upgrade
