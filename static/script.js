const menu = document.querySelector(".menu");
const sideMenu = document.querySelector(".sideMenu");
const nav = document.querySelector("nav");

menu.addEventListener("click", () => {
  if (menu.style.getPropertyValue("--right") == 5) {
    opener();
  } else {
    closer();
  }
});

function hider() {
  nav.style.overflow = "hidden";
}

function opener() {
  menu.innerHTML = `<i class="fa-solid fa-xmark"></i>`;
  nav.style.overflow = "visible";
  menu.style.setProperty("--right", 40);
  sideMenu.style.setProperty("--right", 0);
}

function closer() {
  menu.innerHTML = `<i class="fa-solid fa-bars"></i>`;
  menu.style.setProperty("--right", 5);
  sideMenu.style.setProperty("--right", -205);
  setTimeout(hider, 250);
}
