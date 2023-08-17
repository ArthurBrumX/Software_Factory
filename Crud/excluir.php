<?php
    require_once 'usuarios.php';
    $usuario = new Usuario;
    $usuario->conectar();

    if(isset($_GET['id_usuario'])){
        $id_usuario = $_GET['id_usuario'];
        if($usuario->excluir($id_usuario)){
            echo "Ususario Excluido Com Sucesso.";
            header("location: listar.php");
        }
        else{
            echo "Algo De Errado Não Está Correto.";
            header("location: listar.php");
        }
    }


?>