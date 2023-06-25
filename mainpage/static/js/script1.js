
    // Ваш JavaScript-код тут
    let count1 = document.querySelector("#countProductInCart");
    let count2 = document.querySelector("#countProductInCart1");

    if (count1.textContent == "None" || count2.textContent == "None") {
        count1.style.display = 'none';
        count2.style.display = 'none';
    } else {
        count1.style.display = 'block';
        count2.style.display = 'block';
    }
