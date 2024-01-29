<?php
include 'connect_pg.php';

if(isset($_POST['cadastrar'])){
    $nome = $_POST['nome'];
    $descricao = $_POST['desc'];
    $preco = $_POST['preco'];
    $qtde = $_POST['qtde'];

    $sql = "INSERT INTO PRODUTO (nome,email,senha,foto) VALUES ('$nome','$descricao','$preco','$qtde')";

    $result = pg_query($conn,$sql);

    if($result){
        echo "CADASTRADO COM SUCESSO!!!";
    }else{
        echo "ERROO AO CONECTAR COM O BANCO";
    }
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form method="POST">
        <input type="text" placeholder="nome do produto" name="nome">
        <br>
        <input type="text" placeholder="descricao" name="desc">
        <br>
        <input type="text" placeholder="preco" name="preco">
        <br>
        <input type="text" placeholder="quantidade" name="qtde">
        <br>
        <input type="submit" value="Cadastrar" id="cadastrar" name="cadastrar">
        <br>
        <br>
    </form>
</body>
</html>