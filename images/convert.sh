#!/bin/bash
BASEDIR=$( (cd -P "`dirname "$0"`" && pwd) )

for i in "$BASEDIR"/*.{jpg,png,gif}; do
    [ ! -f "$i" ] && continue
    echo '<img src="data:image/png;base64,'$(python -mbase64 < "$i" | tr -d '\n')'"/>' > "$i.html" 
done

