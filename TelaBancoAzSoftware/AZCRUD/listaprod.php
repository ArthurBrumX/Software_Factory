<?php
include 'connect.php';
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
</head>
<body>

    <div class="container">

        <table class="table">
            <thead>
              <tr>
                <th scope="col">#id</th>
                <th scope="col">nome</th>
                <th scope="col">descricao</th>
                <th scope="col">preco</th>
                <th scope="col">qtde</th>
                <th scope="col">excluir</th>
              </tr>
            </thead>
            <tbody>
            <?php
                $sql = "SELECT * FROM PRODUTO";
                $result = mysqli_query($conn,$sql);

                if($result){
                  //var_dump($result);
                  while($row = mysqli_fetch_assoc($result)){
                    $id = $row['id_produto'];
                    $nome = $row['nome'];
                    $desc = $row['descricao'];
                    $preco = $row['preco'];
                    $qtde = $row['qtde'];
                    $foto = $row['foto'];

                    echo '
                      <tr>
                      <td> '.$id.' </td>
                      <td> '.$nome.' </td>
                      <td> '.$desc.' </td>
                      <td> '.$preco.' </td>
                      <td> '.$qtde.' </td>
                      <td> <img src="'.$foto.'"> </td>
                      </tr>
                    ';
                  }
                }

            ?>
            </tbody>
          </table>

    </div>

   

</body>
</html>