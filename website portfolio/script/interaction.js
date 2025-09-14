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

const langMenu = document.querySelector(".lang-menu");
const langBtn = document.querySelector(".lang-btn");
const currentFlag = document.getElementById("current-flag");

langBtn.addEventListener("click", () => {
  langMenu.classList.toggle("active");
});

document.querySelectorAll(".lang-dropdown a").forEach(link => {
  link.addEventListener("click", e => {
    e.preventDefault();
    const flagImg = link.querySelector("img").src;
    currentFlag.src = flagImg;
    window.location.href = link.getAttribute("href"); // redirige
  });
});