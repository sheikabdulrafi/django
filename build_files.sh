apt-get update
apt-get install -y python3-pip

pip install -r requirements.txt
python3.12 manage.py collectstatic --noinput