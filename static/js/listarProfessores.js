var listProfButton = document.querySelector(".list-prof-btn");
var profList = document.querySelector(".professores");

listProfButton.onclick = () => {
    if (profList.classList.contains("closed")) {
        profList.style.overflowY = "scroll";
        profList.style.height = "50vh";
        profList.style.paddingBottom = "15px";
        profList.style.zIndex = "5";
        listProfButton.textContent = "Recolher";
    } else {
        profList.style.overflowY = "hidden";
        profList.style.height = "0";
        profList.style.paddingBottom = "0";
        listProfButton.textContent = "Listar";
    }
    profList.classList.toggle("closed");
}