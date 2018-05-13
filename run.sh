#!/bin/sh

BASEDIR=$( (cd -P "`dirname "$0"`" && pwd) )

cd $BASEDIR
exec php -S localhost:8080
