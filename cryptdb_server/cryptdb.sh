#! /bin/sh
# /etc/init.d/cryptdb

# The following part always gets executed.
# echo "execute /etc/init.d/cryptdb"

#
export EDBDIR=/opt/cryptdb

# The following part carries out specific functions depending on arguments. As for now, it only displays the proxy information in the shell. TODO: Logging.
case "$1" in
  start)
    echo "Starting cryptdb"
    "$EDBDIR"/bins/proxy-bin/bin/mysql-proxy --plugins=proxy --event-threads=4 --max-open-files=1024 --proxy-lua-script=$EDBDIR/mysqlproxy/wrapper.lua --proxy-address=0.0.0.0:3307 --proxy-backend-addresses=127.0.0.1:3306
#ps aux | grep 'mysql-proxy'
    ;;
  stop)
    echo "Stopping cryptdb"
    kill $(ps aux | grep 'mysql-proxy' | awk '{print $2}')
    ;;
  *)
    echo "Usage: cryptdb.sh {start|stop}"
    exit 1
    ;;
esac

exit 0
