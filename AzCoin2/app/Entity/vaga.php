<?php
namespace app\Entity;

class Vaga{
    /**
     * identificador unico de vaga
     * @var integer
     */
    public $id;
    /**
     * Titulo da vaga
     * @var string
     */

    public $titulo;
    /**
     * descricao da vaga ( pode conter html)
     * @var string
     */

    public $descricao;
    /**
     * Define se a vaga esta ativa
     * @var string (s/n)
     */

    public $ativo;
    /**
     * data de publicacao da vaga
     * @var string
     */

    public $data;
}
?>