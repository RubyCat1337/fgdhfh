const countProductInCart = document.querySelector("#countProductInCart");

if (countProductInCart.textContent == "None"){
    countProductInCart.style.display = "none";
}
else{
    countProductInCart.style.display = "flex";
}