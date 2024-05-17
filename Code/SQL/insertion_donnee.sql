use boite_a_outils_pour_electronicien;
insert into product (Type,Value,Size,Price,`Manufacturer-reference`)
value(1,1.1,1.2,1.3,"ref1"),
(1,1.2,1.2,1.2,"ref2"),
(2,1.3,1.3,1.3,"ref3");


insert into supplier (Name,Address,PhoneNumber) 
values("Fourniseur 1","Rued du moulin 8",001112233),
("Fourniseur 2","Rued du moulin 8",011112233),
("Fourniseur 3","Rued du moulin 8",021112123);

insert into product_has_supplier (product_id, supplier_id, Article_number)
value(1,1,"ABC1" ),
(2,1,"ABC2"),
(3,2,"CBA1");