use boite_a_outils_pour_electronicien;
INSERT INTO product (Type, Value, Size, Price, `Manufacturer-reference`)
VALUES
(1,680,250,20,"abc1"),
(1,680,250,10,"abc2"),
(1,390,250,20,"defDEF"),
(1,3.3,250,20,"ghiGHI");





insert into supplier (Name,Address,PhoneNumber) 
values("Fourniseur 1","Rued du moulin 7",001112233),
("Fourniseur 2","Rued du moulin 8",011112233),
("Fourniseur 3","Rued du moulin 9",021112123);

insert into product_has_supplier (product_id, supplier_id, Article_number)
value(1,1,"article 1" ),
(2,1,"article 2"),
(3,2,"article 1");