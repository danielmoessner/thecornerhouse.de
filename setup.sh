# create folder structure
mkdir tmp/
mkdir tmp/static
mkdir tmp/media
touch tmp/django.log
touch tmp/secrets.json
# install everything
apt update
apt install python3-pip python3-venv python3-dev apache2 libapache2-mod-wsgi-py3 libpq-dev
snap install core
snap refresh core
snap install --classic certbot
# create venv
python3 -m venv tmp/venv
# setup apache configs
ln -s /home/thecornerhouse.de/apache.conf /etc/apache2/sites-available/thecornerhouse.de.conf
certbot certonly --apache -d thecornerhouse.de --register-unsafely-without-email
a2enmod ssl
a2enmod rewrite
a2ensite thecornerhouse.de.conf
