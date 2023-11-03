-- Crear el usuario "pro" con contraseña "1234"
CREATE USER pro IDENTIFIED BY 1234;

-- Asignar espacio de tablespace al usuario (ajusta la cantidad según tus necesidades)
ALTER USER pro QUOTA UNLIMITED ON USERS;

-- Dar privilegios al usuario
GRANT CREATE SESSION TO pro;
GRANT CREATE TABLE TO pro;
GRANT INSERT, UPDATE, DELETE, SELECT ON nombre_de_tabla TO pro; -- Reemplaza "nombre_de_tabla" con el nombre de la tabla a la que deseas otorgar permisos

-- Otorgar el privilegio DBA para acceso completo (opcional, úsalo con precaución)
-- GRANT DBA TO pro;
