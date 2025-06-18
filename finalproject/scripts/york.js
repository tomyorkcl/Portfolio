let cart = JSON.parse(localStorage.getItem("cart")) || [];

document.addEventListener("DOMContentLoaded", () => {
  loadProducts();
  updateCart();

  document.getElementById("clear-cart").addEventListener("click", () => {
    cart = [];
    updateCart();
    saveCart();
  });
});

async function loadProducts() {
  try {
    const res = await fetch("data/products.json");
    if (!res.ok) throw new Error("Failed to load catalog");

    const products = await res.json();
    const catalog = document.getElementById("catalog");

    products.forEach(p => {
      const div = document.createElement("div");
      div.className = "product";
      div.innerHTML = `
        <img src="${p.image}" alt="${p.name}" loading="lazy"/>
        <h3>${p.name}</h3>
        <p><strong>Brand:</strong> ${p.brand}</p>
        <p>${p.description}</p>
        <p><strong>Price:</strong> $${p.price.toLocaleString()}</p>
        <button onclick="addToCart(${p.id}, '${p.name}', ${p.price})">Add</button>
      `;
      catalog.appendChild(div);
    });

  } catch (error) {
    console.error("Error loading products:", error);
    const catalog = document.getElementById("catalog");
    catalog.innerHTML = `<p>There was an error loading the products. Please try again later.</p>`;
  }
}

function addToCart(id, name, price) {
  const index = cart.findIndex(item => item.id === id);
  if (index !== -1) {
    cart[index].quantity += 1;
  } else {
    cart.push({ id, name, price, quantity: 1 });
  }
  updateCart();
  saveCart();
  showModal(); // <- show modal
}

function updateCart() {
  const list = document.getElementById("cart-list");
  const total = document.getElementById("total");
  list.innerHTML = '';
  let sum = 0;

  cart.forEach((item, index) => {
    const li = document.createElement("li");
    li.innerHTML = `
      ${item.name} (${item.quantity}) - $${(item.price * item.quantity).toLocaleString()}
      <button onclick="removeItem(${index})">❌</button>
    `;
    list.appendChild(li);
    sum += item.price * item.quantity;
  });

  total.textContent = sum.toLocaleString();
}

function removeItem(index) {
  cart.splice(index, 1);
  updateCart();
  saveCart();
}

function saveCart() {
  localStorage.setItem("cart", JSON.stringify(cart));
}

function showModal() {
  const modal = document.getElementById("modal");
  modal.style.display = "flex";
  setTimeout(() => {
    modal.style.display = "none";
  }, 1500); // closes after 1.5s
}

document.getElementById("close-modal").addEventListener("click", () => {
  document.getElementById("modal").style.display = "none";
});

