# application.py
from flask import Flask
from flask_restful import Api, Resource
import pyodbc

#Connecting to the DB
cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:teamcheckmate.database.windows.net,1433;Database=teamcheckmate;Uid=jon;Pwd=$password123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
def all_fridge_query():
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM fridge_michael")
    output = cursor.fetchone()
    result = {"item_id":output[0], "item_name":output[1]}
    return result

app = Flask(__name__)
api = Api(app)

class all_fridge(Resource):
    def get(self):
        return(all_fridge_query())

api.add_resource(all_fridge, "/all_fridge")


if __name__ == "__main__":
    app.run(debug=True)
