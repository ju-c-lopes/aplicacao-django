/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
const btn = document.querySelector("#btn-nav");
const menu = document.querySelector("#menu");
btn.onclick = function() {
  btn.classList.toggle('active')
  menu.classList.contains("open") ? menu.classList.remove("open") : menu.classList.add("open");
};
