chown -R root:www-data /home/thecornerhouse.de
chmod -R 750 /home/thecornerhouse.de
find /home/thecornerhouse.de -type f -print0|xargs -0 chmod 740
chmod -R 770 /home/thecornerhouse.de/tmp/media
find /home/thecornerhouse.de/tmp/media -type f -print0|xargs -0 chmod 760
chmod 760 /home/thecornerhouse.de/tmp/django.log
chmod 770 /home/thecornerhouse.de/tmp
chmod -R 760 /home/thecornerhouse.de/tmp/db.sqlite3
