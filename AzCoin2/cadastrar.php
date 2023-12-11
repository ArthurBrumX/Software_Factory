<?php

// Assim, quando estiver dentro do mesmo  arquivo
    // require_once('MenuGestor.php');
    // require_once('Header.php');
    // require_once('Body.php');

// Assim quando estiver em outra pasta
require __DIR__.'/vendor/autoload.php';

echo "<pre>"; print_r($_POST); echo "</pre>"; exit;

// Validacao do POST
if(isset($_POST['titulo'],$_POST['descricao'],$_POST['ativo'])){
    die('Cadastrar');
}

include __DIR__.'/includes/MenuGestor.php';
include __DIR__.'/includes/Header.php';
include __DIR__.'/includes/Body.php';
?>

