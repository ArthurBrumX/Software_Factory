<?php

    require_once 'usuarios.php';
    $usuario = new Usuario;
    $usuario->conectar();

    if(isset($_POST['btn_sub'])){
        if(isset($_POST['nome'],$_POST['email'],$_POST['tele'],$_POST['senha'])){
            if($usuario->cadastrar($_POST['nome'],$_POST['email'],$_POST['tele'],$_POST['senha'])){
                echo "Cadastrado com Sucesso";
            }
            else{
                echo "Erro ao Cadastrar";
            }
        }
    }

?>


<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>cadastro</title>
</head>
<body>
    <h1>Tela Cadastro</h1>
    <form action="" method="post">
    <input type="text" name="nome" placeholder="nome">
    <input type="email" name="email" placeholder="email">
    <input type="tel" name="tele" placeholder="telefone">
    <input type="password" name="senha" placeholder="senha">
    <input type="submit" value="Cadastrar" name="btn_sub">
    </form>
    <a href="listar.php"><button>listar</button></a>
</body>
</html>