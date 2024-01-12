import sqlite3

# Create banking database
con = sqlite3.connect("banking.db")

# Create cursor connection
cur = con.cursor()

# cur.execute("CREATE TABLE accounts(account_num, sort_code, user_id, balance)")

# Check that database has been created
# result = cur.execute("SELECT name FROM sqlite_master")
# print(result.fetchone())

# Account data to insert into db
# acc_data = [
#             (82041626, 927837, 'KL9283', 11500.23),
#             (64736641, 057361, 'SY6627', 543.65),
#             (70231442, 463782, 'PK2873', 8954.92),
#             (44893061, 937478, 'WE7112', 34534.87),
# ]

# Add values to the accounts table
# cur.execute("INSERT INTO accounts VALUES(?, ?, ?, ?)", acc_data)

# Commit the changes
# con.commit()

# Check that values were entered into the db
# result = cur.execute("SELECT account_num FROM accounts")
# print(result.fetchall())