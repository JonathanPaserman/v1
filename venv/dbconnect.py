import pyodbc

cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:teamcheckmate.database.windows.net,1433;Database=teamcheckmate;Uid=jon;Pwd=$password123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")

def all_fridge_query():
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM fridge_michael")
    output = cursor.fetchone()
    result = {"data":{"item_id":output[0], "item_name":output[1], "expiration_date":output[2]}}
    return result

print(all_fridge_query())