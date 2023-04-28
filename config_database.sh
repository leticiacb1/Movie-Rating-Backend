echo " > Conectando com o mysql  ..."

user=$( dotenv -f .env get USERNAME)
password=$( dotenv -f .env get PASSWORD)

echo " > Criando banco de dados e tabelas ..."
mysql -u${user}  -p${password} -e "source script_sql.sql"
mysql -u${user}  -p${password} -e "SHOW DATABASES;"
mysql -u${user}  -p${password} -e "USE movies_ratings; SHOW TABLES;"

echo " > Banco de dados e tabelas criados com sucesso! "