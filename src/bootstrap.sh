set -x
libtoolize --force && aclocal && autoheader && automake --add-missing --copy && autoconf
