FROM postgres:16.2-bookworm as db
WORKDIR /app
COPY postgres.sql /app/scripts/db/postgres.sql
COPY init.sh /docker-entrypoint-initdb.d
