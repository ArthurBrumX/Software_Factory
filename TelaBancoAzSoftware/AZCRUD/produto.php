<?php
include 'connect.php';

if(isset($_POST['cadastrar'])){
    $nome = $_POST['nome'];
    $descricao = $_POST['desc'];
    $preco = $_POST['preco'];
    $qtde = $_POST['qtde'];

    $sql = "INSERT INTO produto (nome,descricao,preco,qtde) VALUES ('$nome','$descricao','$preco','$qtde')";

    $result = mysqli_query($conn,$sql);

    if($result){
        echo "CADASTRADO COM SUCESSO!!!";
    }else{
        die(mysqli_error($conn));
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