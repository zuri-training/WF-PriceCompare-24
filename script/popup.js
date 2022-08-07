const BACKDROP = document.createElement('div');
BACKDROP.className = 'backdrop';
document.body.appendChild(BACKDROP);
const COMPARE_BTN = document.querySelectorAll('.compare-btn');
const compareBtnHandler = () => {
   document.querySelector(".popup").classList.toggle("active");
   document.body.classList.toggle('StopScroll');
   BACKDROP.classList.toggle("active");
};

for (const element of COMPARE_BTN) {
   element.addEventListener('click', compareBtnHandler);
}
  document.querySelector(".popup .close-btn").addEventListener("click", compareBtnHandler);

