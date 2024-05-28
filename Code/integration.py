"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.5
Date : 28.05.2024
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

        requete = "select supplier_id, Name, Address, phone_number from supplier;"
        
        self.mycursor.execute(requete)
        myresult = self.mycursor.fetchall()
        return myresult


    def insertion(self,nom, addresse, numero_telephone):       
        requete = "insert into supplier (Name,Address,phone_number) value ('{}','{}','{}');"
        self.mycursor.execute(requete .format(nom, addresse, numero_telephone))
        self.mydb.commit()

    def insertion_produit(self,type, valeur, taille, prix, numer_article):       
        requete = "INSERT INTO product (Type, Value, Size, Price, `manufacturer-reference`)VALUES('{}','{}','{}','{}','{}')"
        self.mycursor.execute(requete.format(type, valeur, taille, prix, numer_article))
        self.mydb.commit()     
    
    def suppertion(self, numero_telephone):
        requete = "DELETE FROM supplier WHERE phone_number = {};"
        self.mycursor.execute(requete .format(numero_telephone))
        self.mydb.commit()
    def supprimer_produit(self, numer_article):
        requete = "delete from product where `manufacturer-reference` = '{}';"
        self.mycursor.execute(requete .format(numer_article))
        self.mydb.commit()


    def modification(self,numero_actuelle, nom, addresse, nouveaux_numero_telephone):

        requete = "UPDATE supplier SET Name = {}, Address = {}, phone_number = {} WHERE phone_number = {};"
        self.mycursor.execute(requete .format(nom, addresse, nouveaux_numero_telephone, numero_actuelle ))
        self.mydb.commit()

    def modification_produit(self,type, valeur, taille, prix, numero_article, nouveaux_numero_article):
        
        requete = "update product set type = {}, value = {}, Size = {}, price = {}, `manufacturer-reference` = {} where `manufacturer-reference` = {};"
        print(requete)
        self.mycursor.execute(requete .format(type, valeur, taille, prix, nouveaux_numero_article,  numero_article,))
        self.mydb.commit()

    def rechercher_produit(self,type, valeur, taille):
        requete = """select  product.Price, product.`manufacturer-reference`,product.Type,  product.Value, product.Size, supplier.Name
        from product
        inner join product_has_supplier ON product_id = product_id inner join supplier on supplier_id = product_has_supplier.supplier_id
        where (product.Type = {}) and (product.Value between {} and {}) and (product.Size between {} and {});"""

        self.mycursor.execute(requete.format(type, valeur - 0.001, valeur , taille - 0.001, taille ))
        myresult = self.mycursor.fetchall()
        return myresult
    
    def rechercher_resistance(self, valeur):
        requete = """select  product.Price, product.`manufacturer-reference`,product.Type,  product.Value, product.Size, supplier.Name
        from product
        inner join product_has_supplier ON product_id = product_id inner join supplier on supplier_id = product_has_supplier.supplier_id
        where (product.Type = 1) and (product.Value between {} and {});"""
        self.mycursor.execute(requete.format(valeur - 0.001, valeur))
        myresult = self.mycursor.fetchall()
        return myresult
