<?php
include 'connect.php';

if(isset($_POST['cadastrar'])){

    $nome = $_POST['nome'];
    $email = $_POST['email'];
    $senha = $_POST['senha'];

    //var_dump($_FILES);

    $arquivo = $_FILES['foto'];
    if($arquivo['error']) die('Falha ao enviar o arquivo');

    //definindo o caminho que a foto será salva
    $pasta = './uploads/fotos/';
    //recebendo o nome do arquivo
    $nome_arquivo = $arquivo['name'];
    //gera um novo nome para a foto
    $new_name = uniqid();
    //extrai a extensao do arquivo
    $extensao = strtolower(pathinfo($nome_arquivo,PATHINFO_EXTENSION));

    if($extensao != 'png' && $extensao != 'jpeg' ) die("Falha ao enviar o arquivo!");
    //concatena o caminho da pasta mais o novo nome e a extensao
    $caminho = $pasta . $new_name . "." . $extensao;

    $foto = move_uploaded_file($arquivo['tmp_name'],$caminho);



    $sql = "INSERT INTO usuario (nome,email,senha,foto) VALUES ('$nome','$email','$senha','$caminho')";

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
    <form method="POST" enctype="multipart/form-data">
        <input type="text" placeholder="digite seu nome" name="nome">
        <br>
        <input type="text" placeholder="digite seu email" name="email">
        <br>
        <input type="text" placeholder="digite seu senha" name="senha">
        <br>

        <input type="file" name="foto"> <br><br>

        <input type="submit" value="Cadastrar" id="cadastrar" name="cadastrar">
        <br>
        <br>
    </form>
</body>
</html>