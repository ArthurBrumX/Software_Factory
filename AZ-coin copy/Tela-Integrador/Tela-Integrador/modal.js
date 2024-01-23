const visualiza = document.querySelectorAll('#olho-feedback-historico-colaborador');
const fade = document.querySelector('#fade');
const modal = document.querySelector('#modal-feedback');
const fechaModal = document.querySelector('.fecha-modal');
var remetente = document.querySelector('.remetente-feedback-nome')
var feedback = document.querySelector('.conteudo-modal')

const individuos = ['Sara','Jhanuares','Vinycius','Mara','Tiara','Jaguncio','Zeriki','Crutilde','Berivaldir','Teostion']
const comentarios = ['Aquela que seu rosto mostra, mas sim a que vive no seu coração e faz você.','A questão não é essa, exatamente. Vamos pensar melhor sobre, que tal?','O que é raro tem valor; o abundante, não','O sábio torna seu caráter amplo, puro, de modo a poder dar apoio aos outros homens e às coisas.','Voaram, lado a lado, sem olhar para trás. O passado, agora, não significava mais nada.','Sempre achei que fosse o contrário: você e ela, ao invés de ela e você.','Cada vez que o cachorro latia, o gato miava, e o papagaio repetia a última coisa que disse.','E nem tudo que é caro realmente custa alguma coisa.','Toda vez que ele vem aqui eu fico meio assim, sei lá…','E a revolução começou a partir de um beijo interrompido.']

function vistoFeed(position){
    remetente.textContent = '' + individuos[position];
    feedback.textContent = '' + comentarios[position];
    
    fade.classList.toggle('hide');
    modal.classList.toggle('hide');
    
    if (visualiza[position].classList.contains('feed-visto')){
        console.log(position+' já foi visto')
        return 0
    }
    else{
        visualiza[position].classList.add('feed-visto')
        return 0
    }
}



function toggleModal(){
    fade.classList.toggle('hide');
    modal.classList.toggle('hide');
};

[fade,fechaModal].forEach((el) =>{
    el.addEventListener("click",toggleModal);
})


visualiza.forEach((item, index) => {
    item.addEventListener('click', () => vistoFeed(index))
})