<?php

include 'connect.php';

if(isset($_GET['deleteid'])){
    
    $id = $_GET['deleteid'];

    $sql = "DELETE FROM PRODUTO WHERE id_produto=$id";
    $result = mysqli_query($conn,$sql);

    if($result){
        //echo "Produto excluído com sucesso!!";
        header('location:listaprod.php');
    }
    else{
        die(mysqli_error($conn));
    }
}

?>