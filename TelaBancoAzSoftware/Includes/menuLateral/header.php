<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="utf-8">
        <title>Index</title>
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Tomorrow">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Barlow">
        
        <style>
            :root{
                /*Cores*/
                --cor-fundo-menu: rgb(0, 36, 54);
                --cor-laranja-az: rgb(239, 78, 35);

                /*Transições*/
                --tran-menu: 0.5s all ease;
                --tran-texto: 0.8s all ease;
            }
            .bg{
                right: 0;
                bottom: 0;
                z-index: 0;
                opacity: 0.35;
                position: absolute;
            }
            .home{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: 'Tomorrow', serif;
            }
            /*Propriedades do Menu Lateral*/
            .menulateral{
                border-right-style: solid;
                border-right-color: var(--cor-laranja-az) ;
                border-right-width: 2px;
                z-index: 2;
                position: fixed;
                top: 0;
                bottom: 0;
                width: 250px;
                height: 100vh;
                background-color: var(--cor-fundo-menu);
                transition: var(--tran-menu);
            }

            /*Propriedades da Lista Menu*/
            .menulateral .listamenu{
                gap: 40px;
                display: flex;
                flex-flow: column;
                list-style-type: none;
                justify-content: space-between;
            }

            /*Propriedades do SVG AzMerit*/
            .menulateral .listamenu .logoazmerit{
                position: relative;
                margin-left: -15px;
                transition: var(--tran-menu);
            }
            .menulateral .listamenu .logoazmerit #logoazmerit{
                align-items: center;
                display: flex;
                transition: width 0.5s;
            }
            .menulateral .listamenu .logoazmerit #logoazmerit .path_merit{
                padding-bottom: 4px;
                padding-left: 7px;
            }

            /*Botão Maximizar Menu*/
            .menulateral .listamenu .toggle{
                display: none;
                margin-top: 70%;
            }

            /*Propriedades dos itens da lista*/
            .menulateral .listamenu .itemlista{
                width: 100%;
            }
            .menulateral .listamenu .itemlista .itemmenu{
                align-items: center;
                display: flex;
                cursor: pointer;
                width: 100%;
            }
            .menulateral .listamenu .itemlista .itemmenu .textoicon{
                color: white;
                text-decoration: none;
                position: absolute;
                font-size: 1rem;
                font-weight: 500;
                padding: 2px 15px;
                margin-left: 50px;
                border-radius: 30px;
            }
            .menulateral .listamenu .itemlista .itemmenu .icon{
                width: 25px;
                height: 25px;
            }

            /*Propriedades do hover dos itens*/
            .menulateral .listamenu .itemlista .itemmenu:hover{
                color: var(--cor-laranja-az);
            }
            .menulateral .listamenu .itemlista .itemmenu:hover .pathicon{
                fill: var(--cor-laranja-az);
            }

            /*Botão Cadastrar*/
            .menulateral .listamenu .itemlista .cadastrar{
                text-decoration: none;
                color: rgb(255, 255, 255);
                align-items: center;
                display: flex;
                cursor: pointer;
                width: 100%;
            }
            .menulateral .listamenu .itemlista .cadastrar .textoicon{
                position: absolute;
                font-size: 1rem;
                font-weight: 500;
                padding: 2px 15px;
                margin-left: 50px;
                border-radius: 30px;
            }
            .menulateral .listamenu .itemlista .cadastrar .icon{
                width: 25px;
                height: 25px;
            }
            .menulateral .listamenu .itemlista .cadastrar .setabaixo{
                justify-content: center;
                align-items: center;
                transform: translateY(-50%);
                display: flex;
                width: 25px;
                height: 25px;
                position: absolute;
                font-size: 22px;
                right: 10px;
                margin-top: 30px;
            }
            .menulateral .listamenu .itemlista .cadastrar .setabaixo.rotate{
                transform: translateY(-50%) rotate(-180deg);
            }

            /*Propriedades do hover de Cadastrar*/
            .menulateral .listamenu .itemlista .cadastrar:hover{
                color: var(--cor-laranja-az);
            }
            .menulateral .listamenu .itemlista .cadastrar:hover .pathicon{
                fill: var(--cor-laranja-az);
            }
            .menulateral .listamenu .itemlista .cadastrar:hover .setabaixo path{
                fill: var(--cor-laranja-az);
            }

            /*Tamanho das Ondas*/
            .menulateral .logout_div{
                position: relative;
                height: 100vh;
                margin-top: 50px;
                overflow: hidden;
            }

            /*Propriedades das Ondas https://www.cssscript.com/animated-waves-svg/*/
            .logout_div .waves{
                position: relative;
                height: 10vh;
                margin-bottom: -7px;
                min-height: 100px;
                max-height: 550px;
            }
            .parallax > use{
                animation: move-forever 10s cubic-bezier(.55,.5,.45,.5) infinite;
            }
            .parallax > use:nth-child(1){
                animation-delay: -1s;
                animation-duration: 10s;
            }
            .parallax > use:nth-child(2){
                animation-delay: -7s;
                animation-duration: 10s;
            }
            .parallax > use:nth-child(3){
                animation-delay: -5s;
                animation-duration: 10s;
            }
            @keyframes move-forever{
                0% {
                    transform: translate3d(-90px,0,0);
                }
                100% { 
                    transform: translate3d(85px,0,0);
                }
            }
            /*Shrinking for mobile*/
            @media (max-width: 768px){
                .waves {
                    height:40px;
                    min-height:40px;
                }
            }
            .logout_div .boxlogout{
                position: relative;
                height: 100vh;
                width: 100vw;
                background-color: var(--cor-laranja-az);
            }
            .logout_div .boxlogout .itemlogout{
                position: fixed;
                margin-left: 40px;
                text-decoration: none;
                color: white;
                align-items: center;
                display: flex;
                cursor: pointer;
                bottom: 3%;
            }
            .logout_div .boxlogout .itemlogout .iconlogout{
                width: 25px;
                height: 25px;
            }
            .logout_div .boxlogout .itemlogout .textologout{
                position: absolute;
                font-size: 1rem;
                font-weight: 500;
                padding: 2px 15px;
                margin-left: 50px;
                border-radius: 30px;
            }

            /*Propriedades do Cabeçalho*/
            .cabecalho{
                display: flex;
                z-index: 1;
                align-items: center;
                height: 100px;
                margin-left: 250px;
                border-bottom-width: 3px;
                border-bottom-style: solid;
                border-bottom-color: var(--cor-laranja-az);
            }

            /*Propriedades da área do usuário*/
            .cabecalho .user_box{
                position: fixed;
                right: 0;
                padding-top: 10px;
                padding-right: 20px;
                display: flex;
                flex-direction: row;
                align-items: center;
            }
            .cabecalho .user_box .nome_user{
                font-size: 1rem;
                font-weight: bold;
            }
            .cabecalho .user_box .img_user{
                width: 84px;
                height: 84px;
                padding-left: 10px;
                border-radius: 50%;
            }
            .cabecalho .tela_atual{
                margin-top: 2%;
                margin-left: 60px;
                font-size: 20px;
                font-weight: bolder;
                text-transform: uppercase;
            }

            /*Propriedades do Rodapé*/
            .rodape{
                left: 45%;
                bottom: 0%;
                z-index: 0;
                opacity: 0.35;
                padding: auto;
                font-size: 14px;
                position: absolute;
                text-align: center;
                font-weight: bolder;
                color: rgb(0, 0, 0);
            }

            /*Propriedades da Página Exemplo*/
            .Conteiner-principal{
                z-index: 0;
                position: fixed;
                width: auto;
                left: 300px;
                right: 50px;
                height: 75vh;
                border-radius: 30px;
            }

            /*Configurações do Site Responsivo*/
            @media only screen and (max-width: 1000px){
                .menulateral.closed{
                    width: 80px;
                }
                .menulateral .listamenu .toggle{
                    display: flex;
                    position: absolute;
                    top: 35px;
                    right: -15px;
                    transform: translateY(-50%);
                    height: 25px;
                    width: 25px;
                    background: var(--cor-laranja-az);
                    align-items: center;
                    justify-content: center;
                    border-radius: 50%;
                    color: white;
                    font-size: 22px;
                }
                .menulateral.closed .listamenu .toggle{
                    transform: translateY(-50%) rotate(180deg);
                }
                .menulateral.closed .listamenu .logoazmerit{
                    margin-left: -30px;
                }
                .menulateral.closed .listamenu .logoazmerit #logoazmerit .path_az{
                    width: 55px;
                }
                .menulateral.closed .listamenu .logoazmerit #logoazmerit .path_merit{
                    display: none;
                }
                .menulateral.closed .textoicon{
                    opacity: 0;
                    display: none;
                }
                .menulateral.closed .listamenu .itemlista .cadastrar .setabaixo{
                    display: none;
                }


                .cabecalho{
                    margin-left: 80px;
                    height: 80px;
                }
                .cabecalho .user_box .img_user{
                    width: 65px;
                    height: 65px;
                }
                .cabecalho .tela_atual{
                    margin-top: 0;
                    max-width: 200px;
                }
                .cabecalho .tela_atual span{
                    text-align: justify;
                }
                .paginaexemplo{
                    left: 100px;
                    right: 20px;
                }
                .menulateral .listamenu .itemlista{
                    margin-left: -15px;
                }
                .logout_div .boxlogout .itemlogout{
                    margin-left: 30px;
                }
                .menulateral.closed .logout_div .boxlogout .itemlogout .textologout{
                    display: none;
                    pointer-events: none;
                }
                .rodape{
                    left: 25%;
                    padding-right: 20px;
                }
                
            }




            .itemlista .submenu{
                display: none;
                transition: var(--tran-menu);
            }
            .itemlista .submenu.show{
                display: flex;
                gap: 40px;
                padding-top: 40px;
                flex-flow: column;
                list-style-type: none;
                justify-content: space-between;
            }
            .itemlista .submenu.show .textosub{
                color: white;
                text-decoration: none;
                position: absolute;
                font-size: 1rem;
                font-weight: 500;
                padding: 2px 15px;
                margin-left: 20px;
                border-radius: 30px;
            }
            .itemlista .submenu.show li a:hover .textosub{
                color: var(--cor-laranja-az);
            }
            .itemlista .submenu.show li a:hover .pathicon{
                fill: var(--cor-laranja-az);
            }

            /*
            https://www.codingnepalweb.com/side-menu-bar-with-sub-menu-javascript/
            https://www.youtube.com/watch?v=O9l75KOB2pE*/

            /*RODAPÉ*/
            .rodape{
                left: 40%;
                bottom: 0%;
                z-index: 0;
                opacity: 0.35;
                padding: auto;
                font-size: 14px;
                position: absolute;
                text-align: center;
                font-weight: bolder;
                color: rgb(0, 0, 0);
            }
        </style>