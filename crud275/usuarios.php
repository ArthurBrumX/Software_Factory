<?php

    class Usuario{
        private $conexao;
        public $erro;
        
        public function conectar(){
            $dbname = 'telalogin275';
            $host = 'localhost';
            $user = 'root';
            $pass = '';
        
            try{
                $this->conexao = new PDO("mysql:dbname=".$dbname.";host=".$host,$user,$pass);
            }
            catch(PDOException $e){
                echo $e->getMessage();
            }

        }
    public function cadastrar($nome,$telefone,$email,$senha){
        $query = $this->conexao->prepare("SELECT * FROM usuarios WHERE email = :e");
        $query->bindValue(":e",$email);
        $query->execute();
        if($query->rowCount()>0){
            return false;
        }
        else{
            $query = $this->conexao->prepare("INSERT INTO usuarios(nome, email, telefone, senha) VALUES (:n, :e, :t, :s)");
            $query->bindValue(":n",$nome);
            $query->bindValue(":e",$email);
            $query->bindValue(":t",$telefone);
            $query->bindValue(":s",md5($senha));
            $query->execute();

            return true;
            
        }

    }

    public function get_dados(){
        $query = $this->conexao->query("SELECT * FROM usuarios");
        if($query->rowCount()>0){
            $dados = $query->fetchAll(PDO::FETCH_ASSOC);
            return $dados;
        }
        else{
            return false;
        }
    
    }
    public function excluir($id_usuario){
        $query = $this->conexao->prepare("SELECT * FROM usuarios WHERE id_usuario = :id");
        $query->bindValue(':id',$id_usuario);
        $query->execute();

        if($query->rowCount()>0){
            $query = $this->conexao->prepare("DELETE FROM usuarios WHERE id_usuario= :id");
            $query->bindValue(':id',$id_usuario);
            $query->execute();
            return true;
        }
        else{
            return false;
        }
    }
}


?>