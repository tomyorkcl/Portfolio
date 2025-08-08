document.addEventListener("DOMContentLoaded", () => {
  const toggleButton = document.getElementById("theme-toggle");

  toggleButton.addEventListener("click", () => {
    document.body.classList.toggle("light-mode");
  });
});

const menuToggle = document.getElementById('menu-toggle');
const navLinks = document.getElementById('nav-links');

menuToggle.addEventListener('click', () => {
  navLinks.classList.toggle('show');
});
