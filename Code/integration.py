import mysql.connector

class IntergationDB():
    
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="user",
        password="Pa$$w0rd",
        database="boite_a_outils_pour_electronicien")
        self.mycursor = self.mydb.cursor()
        

    def selection(self):

        requete = "select idSupplier, Name, Address, PhoneNumber from supplier;"
        
        self.mycursor.execute(requete)
        myresult = self.mycursor.fetchall()
        return myresult


    def insertion(self,nom, addresse, numero_telephone):       
        requete = "insert into supplier (Name,Address,PhoneNumber) value ('{}','{}','{}');"
        self.mycursor.execute(requete .format(nom, addresse, numero_telephone))
        self.mydb.commit()
    
    def suppertion(self, numero_telephone):
        requete = "DELETE FROM supplier WHERE PhoneNumber = {};"
        self.mycursor.execute(requete .format(numero_telephone))
        self.mydb.commit()

    def modification(self,numero_actuelle, nom = "Name", addresse = "Address", nouveaux_numero_telephone = "PhoneNumber"):
        requete = "UPDATE supplier SET Name = '{}', Address = '{}', PhoneNumber = {} WHERE PhoneNumber = {};"
        self.mycursor.execute(requete .format(nom, addresse, nouveaux_numero_telephone, numero_actuelle ))
        self.mydb.commit()       


test = IntergationDB()

print(test.modification(98, addresse="yopopt"))