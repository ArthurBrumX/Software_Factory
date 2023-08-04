<?php
    if(isset($_POST ['enviar'])){
        echo 'Ta vindo alguma coisa Via post';
        echo '<br>';

        $nome = $_POST['nome'];
        $email = $_POST['email'];
        $senha = $_POST['senha'];

        echo "dados recebidos <br>";
        echo $nome."<br>";
        echo $email."<br>";
        echo $senha."<br>";
    }else{
        echo "nenhum dado recebido";
    }

    var_dump($_POST);
?>