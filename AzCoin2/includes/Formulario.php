<!-- um formulario para usar o cadastro no crud -->
<main>
    <section>
        <a href="../index.php">
            <button class="btn btn-success">Voltar</button>
        </a>
    </section>

    <h2 class="mt-3">Cadastrar</h2>

    <form method="post">
        <div class="form-group">
            <label>Titulo</label>
            <input type="text" class="form-control" name="titulo">
        </div>

        <div class="form-group">
            <label>Descrição</label>
            <input type="text" class="form-control" name="descricao">
        </div>

        <div class="form-group">
            <label>Status</label>

            <div>
                <div class="form-check form-check-inline">
                    <label class="form-control">
                        <input type="radio" name="ativo" value="s">Ativo
                    </label>
                </div>
            </div>

            <div>
                <div class="form-check form-check-inline">
                    <label class="form-control">
                        <input type="radio" name="inativo" value="n">Inativo
                    </label>
                </div>
            </div>
        </div>
        <div class="form-group">
            <button type="submit" class="btn btn-success">Enviar

            </button>
        </div>
    </form>
</main> 