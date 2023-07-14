class produto
{
    constructor()
    {
        this.id=1;
        this.arrayProduto=[];
    }

    validarCampos(produto)
    {  
        let msg=''; /*let - uma variavel local*/
        if(produto.nomeProduto=='')
        {
            msg += 'Informe o Preço do Produto';
            alert(msg);
        }

        if(msg != '')
        {
            return false;
        }

        return true
    }

    cancelar(){
        
    }

    adicionar(produto)
    {
        this.arrayProduto.push(produto);
        this.id ++;
    }

    lerDados()
    {
        let produto = {};

        produto.id = this.id;
        produto.nomeProduto = document.getElementById('produto').value;
        produto.preco = documento.getElementById('preco').value;

        return produto;
    }

    listarTabela()
    {
        let tbody = document.getElementById('tbody');
        tbody.innerText = '';

        for (let i=0; i<this.arrayProduto.length;i++);
        {
            let tr = tbody.insertRow();

            let td_id = tr.insertCell();
            let td_produto = tr.insertCell();
            let td_valor = tr.insertCell();

            td_id.innerText = this.arrayProduto[i].id;
            td_produto.innerText = this.arrayProduto[i].nomeProduto;
            td_valor.innerText = this.arrayProduto[i].preco;
        }
    }

    Salvar()
    {
        let produto = this.lerDados();
        if(this.validarCampos(produto));
        {
            this.adicionar(produto);
        }

        this.listarTabela();

    }
}

var produto = new produto;













































