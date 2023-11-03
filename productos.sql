create table productos(
    id number(4),
    nombre varchar2(30),
    producto varchar2(30),
    constraint pk_pro primary key(id)
);

insert into productos (id, nombre, producto) values (1, 'Pepe', 'chocolate');

commit;
select * from productos;