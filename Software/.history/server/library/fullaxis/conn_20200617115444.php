<?php


/// Datos de conexión de a la Base de datos mysql 
/* 

La Base de datos esta creada con la siguiente estructura:

Γ Fullaxis 
    ├ Users
        └ ID_user (int)
        ├ Name (str)
        ├ Password ()
        ├ Proyect (str)
        ├ Enable (bol)
        └ DatelastAccess (timestamp)
    └ B2_key
        └ ID_key
        ├ ID_key_user
        ├ KeyName
        ├ KeyPassword
        └ Enable
*/



/// Datos de Conección
$dbhost	= "localhost";      // Remplace con la Direción IP de su db mysql
$dbuser	= "userName";		// Remplace con el nombre de usuario de su base de datos
$dbpass	= "Password1234";	// Remplace con la contraseña de acceso de su baase de datos
$dbname	= "Fullaxis";   // Remplace con la con el nombre de la base de datos

/// Conección a la base de datos

