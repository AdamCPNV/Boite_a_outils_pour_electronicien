"""
Auteur : Adam Sifate
Projet : Boîte à outils pour électronicien
Version : 0.6
Date : 30.05.2024
"""

import mysql.connector

class IntergationDB():
    
    def __init__(self):
        """Prépare la connexion a la base de donnée"""
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="user",
        password="Pa$$w0rd",
        database="boite_a_outils_pour_electronicien")
        self.mycursor = self.mydb.cursor()

    def insertion(self,nom, addresse, numero_telephone):    
        """enrgistre dans la bd un nouveaux founrisseur

        Args:
            nom (string)
            addresse (string)
            numero_telephone (int)
        """        """"""   
        requete = "insert into supplier (Name,Address,phone_number) value ('{}','{}','{}');"
        self.mycursor.execute(requete .format(nom, addresse, numero_telephone))
        self.mydb.commit()

    def insertion_produit(self,type, valeur, taille, prix, reference_farbiquant, telephone, numer_article): 
        """enrgistre un produit dans la BD

        Args:
            type (int)
            valeur (float)
            taille (flaot)
            prix (float)
            reference_farbiquant (string)
            telephone (int)
            numer_article (string)
        """        """"""      
        requete1 =  """insert into product (Type, Value, Size, Price, `manufacturer-reference`) VALUES('{}','{}','{}','{}','{}');"""
        requete2 = """insert into product_has_supplier (product_id,  Article_number, supplier_id)
                        value (LAST_INSERT_ID(),'{}', (select id from supplier where phone_number = '{}'));"""
        self.mycursor.execute(requete1. format(type, valeur, taille, prix, reference_farbiquant))
        self.mydb.commit()     

        self.mycursor.execute(requete2. format(numer_article,telephone))
        self.mydb.commit()   
    
    def suppertion(self, numero_telephone):
        """suprime un fournisseur de la BD

        Args:
            numero_telephone (int)
        """
        requete = "DELETE FROM supplier WHERE phone_number = {};"
        self.mycursor.execute(requete .format(numero_telephone))
        self.mydb.commit()
    
    def supprimer_produit(self, numer_article):
        """supprime un produit de la bd

        Args:
            numer_article (string)
        """
        requete = "delete from product where `manufacturer-reference` = '{}';"
        self.mycursor.execute(requete .format(numer_article))
        self.mydb.commit()

    def modification(self,numero_actuelle, nom, addresse, nouveaux_numero_telephone):
        """modifie un fournisseur dans la BD

        Args:
            numero_actuelle (int)
            nom (string)
            addresse (string)
            nouveaux_numero_telephone (int)
        """
        requete = "UPDATE supplier SET Name = {}, Address = {}, phone_number = {} WHERE phone_number = {};"
        self.mycursor.execute(requete .format(nom, addresse, nouveaux_numero_telephone, numero_actuelle ))
        self.mydb.commit()

    def modification_produit(self,type, valeur, taille, prix, numero_article, nouveaux_numero_article):
        """modifie un produit dans la BD

        Args:
            type (int)
            valeur (float)
            taille (float)
            prix (float)
            numero_article (string)
            nouveaux_numero_article (string)
        """
        requete = "update product set type = {}, value = {}, Size = {}, price = {}, `manufacturer-reference` = {} where `manufacturer-reference` = {};"
        print(requete)
        self.mycursor.execute(requete .format(type, valeur, taille, prix, nouveaux_numero_article,  numero_article,))
        self.mydb.commit()

    def rechercher_produit(self,type, valeur, taille):
        """recherche la liste des produit ayant les mêmes caractairistique

        Args:
            type (int)
            valeur (float)
            taille (float)

        Returns:
            myresult (list)
        """        """"""
        requete = """select  product.Price, product.`manufacturer-reference`,product.Type,  product.Value, product.Size, supplier.Name
        from product
        inner join product_has_supplier ON product_id = product_id inner join supplier on supplier_id = product_has_supplier.supplier_id
        where (product.Type = {}) and (product.Value between {} and {}) and (product.Size between {} and {});"""

        self.mycursor.execute(requete.format(type, valeur - 0.001, valeur , taille - 0.001, taille ))
        myresult = self.mycursor.fetchall()
        return myresult
    
    def rechercher_resistance(self, valeur):

        """recherche une resistance

        Args:
            valeur (float)

        Returns:
            myresult (list)
        """        """"""
        requete = """select DISTINCT product.Price, product.`manufacturer-reference`,product.Type,  product.Value, product.Size, supplier.Name
        from product
        inner join product_has_supplier ON product_has_supplier.product_id inner join supplier on product_has_supplier.supplier_id
        where (product.Type = 1) and (product.Value between {} and {});"""
        self.mycursor.execute(requete.format(valeur - 0.001, valeur))
        myresult = self.mycursor.fetchall()
        return myresult