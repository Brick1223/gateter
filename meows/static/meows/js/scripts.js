document.addEventListener("DOMContentLoaded", () => {
  // === Contador de caracteres para textarea ===
  // Este bloque crea y actualiza un contador debajo del textarea,
  // mostrando los caracteres restantes y cambia de color si se excede el límite
  const textarea = document.querySelector("textarea[name='body']");
  if (textarea) {
    const counter = document.createElement("div");
    counter.className = "char-counter";
    textarea.parentNode.appendChild(counter);

    const updateCounter = () => {
      const remaining = 140 - textarea.value.length;
      counter.textContent = `${remaining} caracteres restantes`;
      counter.style.color = remaining < 0 ? "red" : "#aaa";
    };

    textarea.addEventListener("input", updateCounter);
    updateCounter();
  }

  // === Animación de textos alternando ===
  // Este bloque se encarga de mostrar y ocultar de forma cíclica
  // dos textos de introducción, usando clases CSS para transición
  const texts = [
    document.getElementById("introText1"),
    document.getElementById("introText2")
  ];

  let current = 0; // índice del texto activo
  const showDuration = 5500;
  const hideDuration = 1500;
  const intervalDuration = showDuration + hideDuration + 500;

  const animateTexts = () => {
    const activeText = texts[current];
    activeText.classList.remove("exit");
    activeText.classList.add("active");

    setTimeout(() => {
      activeText.classList.remove("active");
      activeText.classList.add("exit");
      current = (current + 1) % texts.length;
    }, showDuration);
  };

  setTimeout(animateTexts, 500); // inicia la animación con retardo
  setInterval(animateTexts, intervalDuration); // repite el ciclo indefinidamente
});
