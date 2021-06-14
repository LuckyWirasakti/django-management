mkdir -p core/static
cp core/.env.example core/.env
python3 manage.py collectstatic --no-input
python3 manage.py makemigrations --no-input
python3 manage.py migrate --no-input