let navbar = document.querySelector(".navbar");

document.querySelector("#menu-bar").onclick = () => {
  navbar.classList.toggle("active");
};

document.querySelector("#close").onclick = () => {
  navbar.classList.remove("active");
};
