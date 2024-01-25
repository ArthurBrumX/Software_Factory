<?php

$dbHost = 'localhost';
$dbName = 'azcoin';// Mudar para AZMerit !!
$dbUser = 'postgres';
$dbPass = '9825@04';

try{
    $conexao = new PDO("pgsql:host=$dbHost;dbname=" . $dbName, $dbUser, $dbPass);
    //echo "conexao relizada com sucesso";
}catch(PDOException $err){
    //echo "banco não conectado" . " " .$err->getMessage();
}

?>