let count = document.querySelector('#countProductInCart');
if (Number(count.textContent) >= 1) {
    main.style.justifyContent = "flex-start";
} else {
    main.style.justifyContent = "center";
}
