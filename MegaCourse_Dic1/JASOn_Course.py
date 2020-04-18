import json
import mysql.connector

from difflib import get_close_matches
from mysql import connector

data = json.load(open("data.json"))

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

word = 'deres'
cursor = con.cursor()
#query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = 'inlay'")
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)


results = cursor.fetchall()


if results:
    for result in results:
        print(result)
else:
    print("no word ")
