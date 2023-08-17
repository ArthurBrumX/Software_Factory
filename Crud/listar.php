<?php
    require_once 'usuarios.php';
    $usuario= new Usuario;
    $usuario->conectar();

    $dados= $usuario->get_dados();
    $tabela = '';
    foreach($dados as $row_user){
        $tabela .=
        '<tr>
            <td>'.$row_user['nome'].'</td>
            <td>'.$row_user['email'].'</td>
            <td>'.$row_user['telefone'].'</td>
            <td>'.$row_user['senha'].'</td>
            <td><a href="editar.php?id_usuario='.$row_user['id_usuario'].'">Editar</a></td>
            <td><a href="excluir.php?id_usuario='.$row_user['id_usuario'].'">Excluir</a></td>
            
        </tr>';
        
    }
?>



<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRUD 275 - Listar</title>
</head>
<body>

    <h1>LISTAR DADOS</h1>
    <table border="1px">
        <thead>
            <th>Nome</th>
            <th>Telefone</th>
            <th>E-mail</th>
            <th>Senha</th>
            <th>Editar</th>
            <th>Excluir</th>
        </thead>
        <?=$tabela?>
    </table>    
    <a href="cadastro.php"><button>Cadastrar</button></a>
</body>
</html>