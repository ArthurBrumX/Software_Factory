<?php
// Parâmetros de conexão com o banco de dados
$host = "localhost";
$dbname = "azmerit";
$user = "root";
$password = "";

// String de conexão PDO
$dsn = "pgsql:host=$host;port=$port;dbname=$dbname;user=$user;password=$password";

try {
    // Criar uma nova instância PDO
    $conexao = new PDO($dsn);

    // Configurar o modo de erro para exceções
    $conexao->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Agora você pode executar consultas no banco de dados usando $conexao

    // Exemplo de consulta
    $consulta = $conexao->query("SELECT * FROM sua_tabela");
    $resultados = $consulta->fetchAll(PDO::FETCH_ASSOC);

    // Faça algo com os resultados

} catch (PDOException $e) {
    // Em caso de erro na conexão
    echo "Erro de conexão: " . $e->getMessage();
}
?>
