chown -R root:www-data /home/apps.de
chmod -R 750 /home/apps.de
find /home/apps.de -type f -print0|xargs -0 chmod 740
chmod -R 770 /home/apps.de/tmp/media
find /home/apps.de/tmp/media -type f -print0|xargs -0 chmod 760
chmod 760 /home/apps.de/tmp/django.log
chmod 770 /home/apps.de/tmp
chmod -R 760 /home/apps.de/tmp/db.sqlite3
