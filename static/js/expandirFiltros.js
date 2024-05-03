var buttonFilters = document.querySelector(".btn-expand-filters");
var divButtonFilters = document.querySelector(".filters");
var listProfButton = document.querySelector(".list-prof-btn");
var listClassButton = document.querySelector(".list-class-btn");
var divProfList = document.querySelector(".professores-form");
var divClassesList = document.querySelector(".classes-form");
var profList = document.querySelector(".professores");
var classesList = document.querySelector(".classes");
var checkedTeachers = document.querySelectorAll(".check-teacher");
var applyButton = document.querySelectorAll(".div-apply-button>button");
var inputHiddenProf = document.querySelector("#analise-professor");
var inputHiddenTurma = document.querySelector("#analise-turma");

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
            divButtonFilters.style.top = "calc(8em + 4em + 12px)";
            divProfList.style.top = "0";
            divClassesList.style.top = "0";
        } else {
            listProfButton.style.top = "0";
            divButtonFilters.style.top = "0";
            divProfList.style.top = "calc(-8em - 12px)";
            divClassesList.style.top = "calc(-8em - 12px)";
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
        listClassButton.onclick = () => {
            if (classesList.classList.contains("closed")) {
                classesList.style.overflowY = "scroll";
                classesList.style.height = "calc(100vh - 55px - 4em)";
                classesList.style.paddingBottom = "150px";
                classesList.style.zIndex = "5";
                listClassButton.textContent = "Recolher";
            } else {
                classesList.style.top = "0"
                classesList.style.overflowY = "hidden";
                classesList.style.height = "0";
                classesList.style.paddingBottom = "0";
                listClassButton.textContent = "Listar";
            }
            classesList.classList.toggle("closed");
        }
    } else {
        buttonFilters.classList.toggle("btn-expand-filters-open");
        if (buttonFilters.classList.contains("btn-expand-filters-open")) {
            listProfButton.style.top = "0";
            divButtonFilters.style.top = "calc(9em + 4em)";
            divProfList.style.top = "0";
            divClassesList.style.top = "0";
        } else {
            listProfButton.style.top = "0";
            divButtonFilters.style.top = "4.5em";
            divProfList.style.top = "0";
            divClassesList.style.top = "0";
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
        listClassButton.onclick = () => {
            if (classesList.classList.contains("closed")) {
                classesList.style.overflowY = "scroll";
                classesList.style.height = "calc(100vh - 55px - 4em)";
                classesList.style.paddingBottom = "150px";
                classesList.style.zIndex = "5";
                listClassButton.textContent = "Recolher";
            } else {
                classesList.style.top = "0"
                classesList.style.overflowY = "hidden";
                classesList.style.height = "0";
                classesList.style.paddingBottom = "0";
                listClassButton.textContent = "Listar";
            }
            classesList.classList.toggle("closed");
        }
    }
}

for (let i = 0; i < applyButton.length; i++) {
    applyButton[i].onclick = () => {
        if (i == 0) {
            inputHiddenTurma.removeAttribute("name");
        } else if (i == 1) {
            inputHiddenProf.removeAttribute("name");
        }
    }
}