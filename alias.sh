# alias settings
alias build='docker-compose build'
alias up='docker-compose up'
alias stop='docker-compose stop'
alias down='docker-compose down'
alias upd='docker-compose up -d' # up with detached mode(background)

alias makemigrations='docker-compose run --rm fastapi poetry run python manage.py makemigrations'
alias migrate='docker-compose run --rm fastapi poetry run python manage.py migrate'
alias createsuperuser='docker-compose run --rm fastapi poetry run python manage.py createsuperuser'
alias collectstatic='docker-compose run --rm fastapi poetry run python manage.py collectstatic --noinput'
alias fastapibash='docker-compose run --rm fastapi bash'
