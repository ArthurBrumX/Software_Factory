<?php
    require_once("../Includes/menuLateral/MenuGestor.php");
    require_once("../Includes/menuLateral/Home.php");
    require_once("config.php");
    require_once("../BancoDeDados/ConexaoBancoDeDados.php");
    require_once("../BancoDeDados/Config.php");
?>

<!DOCTYPE html>
<html lang="pt-br">
    <head>
          <meta charset="utf-8">
          <title>Index</title>
          <link rel="stylesheet" href="../Menu Lateral/Menu.css">
          <link rel="stylesheet" href="Styles/General_Screen_7.css">
          <!-- <link rel="stylesheet" href="Styles/Screen-14-15-16_6.css">
          <link rel="stylesheet" href="Styles/Screen-23_6.css"> 
          <link rel="stylesheet" href="Styles/Screen-cell_6.css"> -->
          <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Tomorrow">
          <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Barlow">
          <link rel="stylesheet" href="modal/modal.css">
          <script src="modal/modal.js" defer></script>
    </head>
<body class="home">
    <main class="Conteiner-principal">
        <div class="conteiner-titulo">
            <h1 class="letra_titulo_uni_s">Saldo Total</h1>
            <h1 class="letra_titulo_uni_r">Recolhidos</h1>
        </div>

        <nav class="conteiner_cartao">
            <!--Saldo_total-->
            <!------------------------------------------------------------->
            <div class="cartao_1">
                <div class="logo_az_cartao">
                    <img class="logo-cartao" src="img/Simbolo-Az-Cartao.png" alt="Carregando...">
                    <h1 class="merit_letra">MERIT</h1> 
                    <p class="barra">/</p>
                    <img class="logo_final" src="img/AZmerit-Simbolo-Cartao.png" alt="carregando...">
                </div>
                <!------------------------------------------------------------->

                <div>
                    <p class="valor-cartao">R$0</p>
                </div>
                <!------------------------------------------------------------->
                
                <div class="adm">
                    <h1 class="adm_letra">Administrador</h1>
                </div>

            </div>
            <!------------------------------------------------------------->

            <!--seta-->

            <div class="seta" id="arrowAnim">
                <div class="arrowSliding">
                    <div class="arrow"></div>
                </div>
                <div class="arrowSliding delay1">
                    <div class="arrow"></div>
                </div>
                <div class="arrowSliding delay2">
                    <div class="arrow"></div>
                </div>
                <div class="arrowSliding delay3">
                    <div class="arrow"></div>
                </div>
                </div>

            <!-------------------------------------------------------------->

            <!--Recolhidos-->
            <!------------------------------------------------------------->
            <div class="cartao_2">
                <div class="logo_az_cartao"> 
                    <img class="logo-cartao" src="img/Simbolo-Az-Cartao.png" alt="Carregando...">
                    <h1 class="merit_letra">MERIT</h1> 
                    <p class="barra">/</p>
                    <img class="logo_final" src="img/AZmerit-Simbolo-Cartao.png" alt="carregando...">
                </div>
                <!------------------------------------------------------------->
                <div>
                    <p class="valor-cartao">R$0</p>
                </div>
                <!------------------------------------------------------------->
                <div class="adm">
                    <h1 class="adm_letra">Administrador</h1>
                </div>
            </div>
            <!------------------------------------------------------------->
        </nav>

        <!--Ver detalhes-->
        <!------------------------------------------------------------->

        <nav>
            <div class="Conteiner-link">

                <div class="bolinha-link">
                    <p class="bolinha-do-link"></p>
                    
                    <div>
                        <a class="link-detalhes" href="#">Ver Detalhes</a>
                    </div>
                </div>

            </div>
        </nav>

        <!--Fim Ver detalhes-->
        <!------------------------------------------------------------->

        <nav class="conteiner_bolinha_1">
            <di class="bolinha_uma">
                <div class="bolinha_1">
                    <p class="bolinha-paragrafo">0%</p>
                </div>
            </di>
        </nav>

        <nav class="conteiner_bolinhas_2">
            <div class="bolinha_duas">
                <div class="bolinha_2">
                    <p class="bolinha-paragrafo">0%</p>
                </div>
                <div class="bolinha_2">
                    <p class="bolinha-paragrafo">0%</p>
                </div>
            </div>
        </nav>
    </main>

    <footer class="rodape"><p>2023 © AZ Tecnologia em Gestão. Todos os direitos reservados.</p></footer>

    <script src="script.js"></script>
</body>
</html>
