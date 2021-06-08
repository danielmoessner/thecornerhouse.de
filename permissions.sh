chown -R root:www-data /home/thecornerhouse_project
chmod -R 750 /home/thecornerhouse_project
find /home/thecornerhouse_project -type f -print0|xargs -0 chmod 740
chmod -R 770 /home/thecornerhouse_project/thecornerhouse/thecornerhouse/media
find /home/thecornerhouse_project/thecornerhouse/thecornerhouse/media -type f -print0|xargs -0 chmod 760
chmod 770 /home/thecornerhouse_project/thecornerhouse/logs
chmod -R 760 /home/thecornerhouse_project/thecornerhouse/logs/*
chmod 770 /home/thecornerhouse_project/thecornerhouse
chmod -R 760 /home/thecornerhouse_project/thecornerhouse/db.sqlite3
