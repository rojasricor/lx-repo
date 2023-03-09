alert("02:56:42");

const circulo = document.querySelector(".circulo");

const rectangulo = document.querySelector(".rectangulo");

// circulo.addEventListener("dragstart", () => console.log(1));
// circulo.addEventListener("drag", () => console.log(2));
// circulo.addEventListener("dragend", () => console.log(3));

rectangulo.addEventListener("dragenter", () => console.log(1));
rectangulo.addEventListener("dragover", (e) => {
  e.preventDefault();
  console.log(2);
});
rectangulo.addEventListener("drop", () => console.log(3));
rectangulo.addEventListener("dragleave", () => console.log(4));
