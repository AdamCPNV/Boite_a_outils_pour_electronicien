"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.2
Date : 17.05.2024
"""

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

    def modification(self,numero_actuelle, nom, addresse, nouveaux_numero_telephone):

        requete = "UPDATE supplier SET Name = {}, Address = {}, PhoneNumber = {} WHERE PhoneNumber = {};"
        self.mycursor.execute(requete .format(nom, addresse, nouveaux_numero_telephone, numero_actuelle ))
        self.mydb.commit()

    def rechercher_produit(self,type, valeur, taille):
        requete = """select  product.Price, product.`Manufacturer-reference`,product.Type,  product.Value, product.Size, supplier.Name
        from product
        inner join product_has_supplier ON idproduct = product_id inner join supplier on idSupplier = product_has_supplier.supplier_id
        where (product.Type = {}) and (product.Value between {} and {}) and (product.Size between {} and {});"""

        self.mycursor.execute(requete.format(type, valeur - 0.001, valeur , taille - 0.001, taille ))
        myresult = self.mycursor.fetchall()
        return myresult
