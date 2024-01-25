<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="utf-8">
        <title>Index</title>
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Tomorrow">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Barlow">
        <link rel="stylesheet" href="modal/modal.css">
        <script src="modal/modal.js" defer></script>

        <style>
            .Conteiner-principal{
                margin-top: 3%;
                width: 80%;
            }

            .conteiner-titulo{
                display: flex; 
                flex-direction: row; 
                justify-content: space-between;
                text-decoration: none;
                font-size: 70%;
                margin-bottom: 4vh;
            }
            
            .letra_titulo_uni_r{
                margin-right: 17vh;
            }
            
            .letra_titulo_uni_s{
                margin-left: 15vh;
            }
            
            .conteiner_cartao{
                margin-left: 2%;
                display: flex; /*Deixa o item movimentavel*/
                justify-content: space-between; /*Abre espaço entre eles*/
                padding-right: 3vh;
            }
            
            /* ------------------------------------------------------------- */
            /* config Cartao */
            
            .cartao_1{
                background-color: #002436;
                padding: 1%; /*espaco interno*/
                border-radius: 20px; /*Borda Arredondada*/
                width: 25%;
            }
            
            .cartao_2{
                background-color: #002436;
                padding: 1%; /*espaco interno*/
                border-radius: 20px; /*borda arredondado*/
                width: 25%;
            }
            
            /* ------------------------------------------------------------- */
            
            /* configuracao interna do cartao */
            
            .logo_az_cartao{
                display: flex;
                justify-content: flex-start;
            }
            
            .logo-cartao{
                height: 55%;
            }
            
            .merit_letra{
                
                text-decoration: none;
                font-size: 15px;
                color: white;
            
            }
            
            .barra{
                margin-left: 20vh;
                font-size: 13px;
                text-decoration: none;
                color: #FF4242;
            }
            
            .logo_final{
                height: 9px;
                margin-top: 1%;
                /*filter: invert(80%); /*para inverter a cor da imagem de preto para branco*/
                margin-right: 100%;
            }
            
            .adm{
                display: flex;
                margin-left: 2%;
                margin-top: 6vh;
                width: 9vh;
            
            }
            .adm_letra{
                color: white;
                text-decoration: none;
                font-size: 13px;
                
            }
            
            .valor-cartao{
                text-align: center;
                font-size: 5vh;
                margin-top: 4vh;
                color: #FF4242;
                color: var(--cor-laranja-az);
            
            }
            
            /*fim cartao*/
            /* ------------------------------------------------------------- */
            
            /* inicio (ver detalhe) */
            
            .Conteiner-link{
                margin-left: 1vh;
            }
            
            .bolinha-link{
                align-items: center;
                display: flex;
                flex-direction: row;
                margin-left: 107vh;
            
            }
            
            .bolinha-do-link{
                background-color: #002436;
                border-radius: 100%;
                padding: 3%;
                margin-right: 1%;
            
            }
            
            .link-detalhes{
                text-decoration: none;
                color: black;
            }
            /*------------------------------------------------------*/

            /*inicio seta*/

            #arrowAnim {
                width: 1vw;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            
            .arrow {
                width: 2vw;
                height: 2vw;
                border: 1vw solid;
                border-color: black transparent transparent black;
                transform: rotate(-45deg);
            }
            
            
            .arrowSliding {
                position: absolute;
                -webkit-animation: slide 4s linear infinite; 
                animation: slide 4s linear infinite;
                
            }

            .delay1 {
                -webkit-animation-delay: 1s; 
                animation-delay: 1s;
            }
            .delay2 {
                -webkit-animation-delay: 2s; 
                animation-delay: 2s;
            }
            .delay3 {
                -webkit-animation-delay: 3s; 
                animation-delay: 3s;
            }
            
            @-webkit-keyframes slide {
                0% { opacity:0; transform: translateX(15vw); }	
                20% { opacity:0; transform: translateX(9vw); }	
                80% { opacity:0; transform: translateX(-9vw); }	
                100% { opacity:0; transform: translateX(-15vw); }	
            }
            @keyframes slide {
                0% { opacity:0; transform: translateX(15vw); }	
                20% { opacity:0.1; transform: translateX(8vw); }
                80% { opacity:1; transform: translateX(-7vw); }	
                100% { opacity:0; transform: translateX(-5vw); }	
            }

            /*Fim Seta*/

            /*------------------------------------------------------*/


            /*Inicio bolinhas*/

            .bolinha-paragrafo{
                text-align: center;
                font-size: 15px;
                color: var(--cor-laranja-az);
            }

            /*------------------------------------------------------*/

            /* Bolinha 1 */

            .conteiner_bolinha_1{
                display: flex;
                justify-content: center;
                
            }

            .bolinha_uma{
                display: flex;
            }

            .bolinha_1{
                background-color: #002436;
                z-index: 2;
                border-radius: 100%;
                padding: 6vh 6vh 6vh 6vh;
                border: 10px solid #827e7e;
            }

            /*-------------------------------------------------------*/

            /* Bolinha dupla */

            .conteiner_bolinhas_2{
                display: flex;
            }

            .bolinha_duas{
                display: flex;

            }

            .bolinha_2{
                margin-left: 39vh;
                background-color: #002436;
                z-index: 2;
                border-radius: 100%;
                padding: 6vh 6vh 6vh 6vh;
                border: 10px solid #827e7e;
            }

            /*-------------------------------------------------------*/

            /*RODAPÉ*/
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
        </style>