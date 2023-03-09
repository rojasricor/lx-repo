"use strict";

const actualizarHora = () => {
  const tiempo = new Date();
  let hora = tiempo.getHours();
  let minutos = tiempo.getMinutes();
  let segundos = tiempo.getSeconds();
  hora = hora < 10 ? `0${hora}` : hora;
  minutos = minutos < 10 ? `0${minutos}` : minutos;
  segundos = segundos < 10 ? `0${segundos}` : segundos;
  document.querySelector(".hora").textContent = hora;
  document.querySelector(".minutos").textContent = segundos;
  document.querySelector(".segundos").textContent = segundos;
};

actualizarHora();

setInterval(actualizarHora, 1000);
