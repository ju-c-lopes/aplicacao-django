var divButtonDark = document.querySelector(".button-theme");
var darkModeRoundedDiv = document.querySelector(".button-dark");
var buttonDark = document.querySelector(".btn-dark");

var bodyElement = document.querySelector("body");
var navHeader = document.querySelector(".navbar");
var menuNav = document.querySelector(".menu-container");
var buttonMenu = document.querySelector("#btn-nav");
var mainFooter = document.querySelector(".footer-custom")
var multipleElements = [
    [document.querySelectorAll(".nav-link"), "nav-link-dark"],
    [document.querySelectorAll("div"), "div-dark"],
    [document.querySelectorAll("input"), "input-dark"],
    [document.querySelectorAll("select"), "select-dark"],
    [document.querySelectorAll("textarea"), "text-area-dark"],
]

function slideButton() {
    buttonDark.classList.toggle("btn-dark-right");
}

function setTheme(tema) {
    localStorage.setItem("tema", tema);
}

buttonDark.addEventListener("click" || "touchstart", (e) => {1
    console.log(e.type)
    slideButton();
    if (buttonDark.classList.contains("btn-dark-right")) {
        localStorage.setItem("tema", "dark");
    } else {
        localStorage.setItem("tema", "light");
    }
    bodyElement.classList.toggle("dark-mode");
    navHeader.classList.toggle("header-dark-mode");
    divButtonDark.classList.toggle("button-dark-component");
    buttonMenu.classList.toggle("btn-nav-dark")
    menuNav.classList.toggle("header-dark-mode");
    for (let elements of multipleElements) {
        for (let el of elements[0]) {
            el.classList.toggle(elements[1]);
        }
    }
    for (let input of document.querySelectorAll("input")) {
        input.addEventListener('focus', () => {
            input.style.backgroundColor = "var(--light-dark)";
        })
    }
    for (let bt of document.querySelectorAll(".bt-edit")) {
        if (localStorage.getItem("tema") == "dark") {
            bt.innerHTML = `<img src="/static/img/lapis-white.png" alt="Adicionar mais informações" />`;
        } else {
            bt.innerHTML = `<img src="/static/img/lapis.png" alt="Adicionar mais informações" />`;
        }
    }
    mainFooter.classList.toggle("footer-dark-mode")
})

setTheme(localStorage.getItem("tema") || "light");
if (localStorage.getItem("tema") == "dark") {
    buttonDark.classList.toggle("btn-dark-right");
    bodyElement.classList.add("dark-mode");
    navHeader.classList.add("header-dark-mode");
    divButtonDark.classList.add("button-dark-component");
    buttonMenu.classList.add("btn-nav-dark")
    menuNav.classList.add("header-dark-mode");
    for (let elements of multipleElements) {
        for (let el of elements[0]) {
            el.classList.add(elements[1]);
        }
    }
    for (let input of document.querySelectorAll("input")) {
        input.addEventListener('focus', () => {
            input.style.backgroundColor = "var(--light-dark)";
        })
    }
    for (let bt of document.querySelectorAll(".bt-edit")) {
        if (localStorage.getItem("tema") == "dark") {
            bt.innerHTML = `<img src="/static/img/lapis-white.png" alt="Adicionar mais informações" />`;
        } else {
            bt.innerHTML = `<img src="/static/img/lapis.png" alt="Adicionar mais informações" />`;
        }
    }
    mainFooter.classList.add("footer-dark-mode")
}