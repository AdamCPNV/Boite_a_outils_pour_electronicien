import mysql.connector

class IntergationDB():
    
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="user",
        password="Pa$$w0rd",
        database="boite_a_outils_pour_electronicien")
        self.mycursor = self.mydb.cursor()
        

    def select(self):

        requete = "select idSupplier, Name, Address, PhoneNumber from supplier;"
        
        self.mycursor.execute(requete)
        myresult = self.mycursor.fetchall()
        return myresult

    """"
    @param NomDeUtilisateur : string
    @param MotDePasse : string
    return : None
    """
    def insert(self,nom, addresse, numero_telephone):

        
        requete = "insert into supplier (Name,Address,PhoneNumber) value ('{}','{}','{}');"
        self.mycursor.execute(requete .format(nom, addresse, numero_telephone))
        self.mydb.commit()



test = IntergationDB()

print(test.insert(4,4,4))