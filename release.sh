cp app/core/.env.example app/core/.env
python3 manage.py collectstatic --no-input 
python3 manage.py migrate --no-input