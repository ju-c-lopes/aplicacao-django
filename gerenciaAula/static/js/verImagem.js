const imagem = document.querySelector('.user-img--foto');
const verImg = document.querySelector('.img-menu--button');
const fullImg = document.querySelector('.full-user--img');
const header = document.querySelector('.navbar');
const footer = document.querySelector('.footer-custom');
const close = document.querySelector('.logout-img');
const noPhoto = document.querySelector('.no-user--img');
const menuButtons = document.querySelector('.menu-buttons');

if (fullImg != null) {
    verImg.addEventListener('click', () => {
        header.style.zIndex = '0';
        if (footer.style.display != 'none') {
            footer.style.display = 'none';
        }
        fullImg.classList.add('full-image--active');
        fullImg.style.display = "flex";
    });
} else {
    verImg.addEventListener('click', () => {
        noPhoto.style.display = "block";
        setTimeout(() => {
            noPhoto.style.animation = "0.4s apagar linear forwards";
        }, 4000)
        noPhoto.style.animation = "reset";
    });
}

if (close != null) {
    close.addEventListener('mouseover', () => {
        close.style.animation = "0.1s closeBtUp linear forwards";
    });
    close.addEventListener('mouseout', () => {
        close.style.animation = "0.1s closeBtDown linear forwards";
    });
    close.addEventListener('click', () => {
        fullImg.style.display = "none";
        footer.style.display = 'block';
    });
}

imagem.addEventListener('mouseover', () => {
    menuButtons.style.animation = "0.5s fadeIn linear forwards";
});

imagem.addEventListener('mouseout', () => {
    menuButtons.style.animation = "0.5s fadeOut linear forwards";
});
