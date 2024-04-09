const expandButton = document.querySelectorAll(".expand-bt");
const allDescr = document.querySelectorAll(".descricao-habs");

for (let i = 0; i < expandButton.length; i++) {
    expandButton[i].onclick =  (e) => {
        e.preventDefault();
        for (let j = 0; j < expandButton.length; j++) {
            if (j !== i) {
                allDescr[j].classList.remove('descricao-open');
                expandButton[j].style.transform = "scaleY(1)";
            }
        }
        allDescr[i].classList.toggle('descricao-open');
        expandButton[i].style.transform = allDescr[i].classList.contains("descricao-open") ? "scaleY(-1)" : "scaleY(1)";
    };
}
