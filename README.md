# arcerojas
Entrevista de trabajo
Solucion del problema 
la solucion  del problema conto con una base datos relacional, con una capa backend ralizado desde el framework de django  y una capa frontend realizado en los templates de django.
no se vio  la necesidad de implementar una capa Rest y si se pidiera esta se realizaria con djago rest framework (DRF) y una capa de libreria o framework frontend como lo es Angula,Reactjs,Vue.




Pasos para instalar el sistema

- docker-compose build
- compose-compose up(talvez pueda repetir este paso dos veces dependiendo de las configuraciones de su entorno)

Entrar al contenedor para realizar las migraciones 
- docker exec -ti ddb /bin/bash
  
- Consultas sql 
    - INSERT INTO public."TipoCliente_tipocliente"(nombre)VALUES ('Empresa');
    - INSERT INTO public."TipoCliente_tipocliente"(nombre)VALUES ('Persona');
    - INSERT INTO public."TipoGeografia_tipogeografia"(nombre)VALUES ('Rural');
    - INSERT INTO public."TipoGeografia_tipogeografia"(nombre)VALUES ('Urbano');
    - INSERT INTO public."TipoIdentificacion_tipoidentificacion"(nombre)VALUES('CC');
    - INSERT INTO public."TipoIdentificacion_tipoidentificacion"(nombre)VALUES('NIT');    


Muchas gracias y agradecimientos
