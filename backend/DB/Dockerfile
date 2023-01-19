# MySQL8系のイメージを指定
FROM mysql:8.0

# MySQLのローカルの設定ファイルをコンテナにコピー
COPY ./backend/DB/conf/my.cnf /etc/mysql/conf.d/my.cnf
# init.sqlをコンテナの/docker-entrypoint-init.db.dと共有
COPY ./backend/DB/conf/init.sql /docker-entrypoint-initdb.d
