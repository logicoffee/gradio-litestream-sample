#!/bin/bash

if [ -f data/todo.db ]; then
    echo 'local database file already exists'
elif litestream restore --config litestream.yml data/todo.db; then
    echo 'restoration succeeded'
else
    echo 'restoration failed'
    sqlite3 data/todo.db << EOF
    CREATE TABLE todo (
        id INTEGER PRIMARY KEY,
        title TEXT,
        status TEXT
    );
EOF
    echo 'database created'
fi
