# arcerojas
Entrevista de trabajo


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

