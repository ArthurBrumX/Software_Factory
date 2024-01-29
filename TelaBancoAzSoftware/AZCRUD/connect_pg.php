<?php

$hostname = "localhost";
$username = "postgres";
$password = "1234";
$db = "azcrud";

$conn = pg_connect("host=$hostname dbname=$db user=$username password=$password");

if(!$conn){
    echo "Errrorrrorororororo"; 
}
else{
    echo "<h1> Conectado com sucesso!! </h1>";
}

?>