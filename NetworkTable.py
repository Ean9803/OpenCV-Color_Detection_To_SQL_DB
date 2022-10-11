import mysql.connector
from prettytable import PrettyTable

class NetTable:
    
    def __init__(self):
        self.db = mysql.connector.connect(host = "localhost", user = "root", passwd = "HeroBrine")
        self.cursor = self.db.cursor()
        #cursor.execute("DROP DATABASE IF EXISTS VisionDatabase")
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS VisionDatabase")

        self.db = mysql.connector.connect(host = "localhost", user = "root", passwd = "HeroBrine", database = "VisionDatabase")
        self.cursor = self.db.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS VisionPoints (ID int, xPos FLOAT, yPos FLOAT)")
        self.tablePrint = PrettyTable(['ID', 'X_Pos', 'Y_Pos'])

    def InsertData(self, ID, xPos, yPos, commit = False):
        self.cursor.execute("SELECT * FROM VisionPoints WHERE ID = %s", (ID,))
        if len(self.cursor.fetchall()) == 0:
            self.cursor.execute("INSERT INTO VisionPoints (ID, xPos, yPos) VALUES (%s, %s, %s)", (ID, xPos, yPos))
        else:
            self.cursor.execute("UPDATE VisionPoints SET xPos = %s, yPos = %s WHERE ID = %s", (xPos, yPos, ID))
        if (commit):
            self.db.commit()

    def CommitChanges(self):
        self.db.commit()

    def DeleteData(self, ID):
        self.cursor.execute("DELETE FROM VisionPoints WHERE ID = %s", (ID,))

    def DeleteAllData(self):
        self.cursor.execute("DELETE FROM VisionPoints")

    def GetData(self, ID):
        self.cursor.execute("SELECT * FROM VisionPoints WHERE ID = %s", (ID,))
        Data = self.cursor.fetchall()
        if len(Data) == 0:
            return 0, 0, 0
        else:
            return Data[0][0], Data[0][1], Data[0][2]

    def GetData_XPos(self, ID):
        self.cursor.execute("SELECT * FROM VisionPoints WHERE ID = %s", (ID,))
        Data = self.cursor.fetchall()
        if len(Data) == 0:
            return 0
        else:
            return Data[0][1]

    def GetData_YPos(self, ID):
        self.cursor.execute("SELECT * FROM VisionPoints WHERE ID = %s", (ID,))
        Data = self.cursor.fetchall()
        if len(Data) == 0:
            return 0
        else:
            return Data[0][2]

    def PrintTable(self):
        self.cursor.execute("SELECT * FROM VisionPoints")
        self.tablePrint.clear_rows()
        for x in self.cursor:
            self.tablePrint.add_row([x[0], x[1], x[2]])
        print(self.tablePrint)

    def CloseTable(self):
        self.cursor.close()
        self.db.close()


"""
Table = NetTable()

Table.InsertData(0, 20.2, 3)
Table.InsertData(2, 45.34, 53.354)
Table.InsertData(1, 234.53, 23.34)
Table.InsertData(1, 32, 34.23)

Table.PrintTable()
print("==============")
print(Table.GetData(2))
Table.DeleteAllData()
print("==============")
Table.PrintTable()
"""