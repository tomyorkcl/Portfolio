document.addEventListener("DOMContentLoaded", () => {
  const toggleButton = document.getElementById("theme-toggle");

  toggleButton.addEventListener("click", () => {
    document.body.classList.toggle("light-mode");
  });
});