const abrirModalBotao = document.querySelector("#open-modal");
const fecharModalBotao = document.querySelector("#close-modal");
const modal = document.querySelector("#modal");
const fade = document.querySelector("#fade");

const toggleModal = () => {
  modal.classList.toggle("hide");
  fade.classList.toggle("hide");
};

[abrirModalBotao, fecharModalBotao, fade].forEach((el) => {
  el.addEventListener("click", () => toggleModal());
});

for(var i= 0,len= abrirModalBotoes.length;i==len;i++){
  abrirModalBotoes[i].addEventListener("click",toggleModal);
}
