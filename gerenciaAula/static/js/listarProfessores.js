var buttonFilters = document.querySelector(".btn-expand-filters");
var divButtonFilters = document.querySelector(".filters");
var listProfButton = document.querySelector(".list-prof-btn");
var divProfList = document.querySelector(".professores-form");
var profList = document.querySelector(".professores");
var checkedTeachers = document.querySelectorAll(".check-teacher");

var contChecked = 0;
for (let checkbox of checkedTeachers) {
    checkbox.onclick = () => {
        contChecked++;
        if (contChecked == 5) {
            for (let nonChecked of checkedTeachers) {
                if (nonChecked.checked == false) {
                    nonChecked.disabled = true;
                    nonChecked.nextElementSibling.style.color = "#b2b2b2";
                }
            }
        }
    }
}

buttonFilters.onclick = () => {
    if (screen.width < 768) {
        buttonFilters.classList.toggle("btn-expand-filters-open");
        if (buttonFilters.classList.contains("btn-expand-filters-open")) {
            listProfButton.style.top = "4em";
            divButtonFilters.style.top = "8em";
            divProfList.style.top = "0";
        } else {
            listProfButton.style.top = "0";
            divButtonFilters.style.top = "4em";
            divProfList.style.top = "-4em";
        }
        listProfButton.onclick = () => {
            if (profList.classList.contains("closed")) {
                profList.style.overflowY = "scroll";
                profList.style.height = "calc(100vh - 55px - 4em)";
                profList.style.paddingBottom = "150px";
                profList.style.zIndex = "5";
                listProfButton.textContent = "Recolher";
            } else {
                profList.style.top = "0"
                profList.style.overflowY = "hidden";
                profList.style.height = "0";
                profList.style.paddingBottom = "0";
                listProfButton.textContent = "Listar";
            }
            profList.classList.toggle("closed");
        }
    } else {
        buttonFilters.classList.toggle("btn-expand-filters-open");
        if (buttonFilters.classList.contains("btn-expand-filters-open")) {
            listProfButton.style.top = "calc(4em + 4.5em)";
            divButtonFilters.style.top = "9em";
            divProfList.style.top = "calc(-4.5em + 4.5em)";
        } else {
            listProfButton.style.top = "0";
            divButtonFilters.style.top = "4.5em";
            divProfList.style.top = "0";
        }
        listProfButton.onclick = () => {
            if (profList.classList.contains("closed")) {
                profList.style.overflowY = "scroll";
                profList.style.height = "calc(100vh - 55px - 4em)";
                profList.style.paddingBottom = "150px";
                profList.style.zIndex = "5";
                listProfButton.textContent = "Recolher";
            } else {
                profList.style.top = "0"
                profList.style.overflowY = "hidden";
                profList.style.height = "0";
                profList.style.paddingBottom = "0";
                listProfButton.textContent = "Listar";
            }
            profList.classList.toggle("closed");
        }
    }
}