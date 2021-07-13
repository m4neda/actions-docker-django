import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(user='root', password='root', database='mintaku', port=3306)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()

conn = cnx
print(conn.is_connected())
cur = conn.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS `test_table` (
    `id` int auto_increment primary key,
    `name` varchar(50) not null,
    `price` int(11) not null
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
    """)

cur.execute("INSERT INTO test_table VALUES (1, 'BTC', 10200)")

cur.execute("SELECT * FROM test_table ORDER BY id ASC")
rows = cur.fetchall()

for row in rows:
    print(row)
