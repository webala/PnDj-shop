function getCartCookie () {
    let name = 'cart';

    var cookieArray  = document.cookie.split(';');

    for (var i = 0; i < cookieArray.length; i++) {
        var cookiePair = cookieArray[i].split('=');

        if (name == cookiePair[0].trim()) {
            return decodeURIComponent(cookiePair[1]);
        }
    }
    return null;
}

var cart = JSON.parse(getCartCookie());

if (cart == undefined) {
    cart = {};
    document.cookie = 'cart=' + JSON.stringify(cart) + ';domain=;path=/';
}


let cart_items = 0;
let cartItemsParagraph = document.querySelector('#cart_items')

//get cart items
fetch('/cart_items').then(response => response.json())
.then(data => {
    cart_items = data.cart_items;
    cartItemsParagraph.innerHTML = cart_items;  
}).catch(error => console.log('Error: ', error));



updateBtns = Array.from(document.getElementsByClassName('update-cart'));


updateBtns.forEach((btn)=> {
    btn.addEventListener('click', ()=> {
        var action = btn.dataset.action;
        var productId = btn.dataset.product

        console.log('user:', user)
        if (user != 'AnonymousUser') {
            updateUserCart(action, productId);
        }
        else {
            addCookieItem(action, productId)
        }
    })
})

const addCookieItem = (action, productId) => {
    if (action == 'add'){
        if (cart[productId] == undefined) {
            cart[productId] = {'quantity': 1};
        } else {
            cart[productId]['quantity'] += 1;
        }
    }else if (action == 'remove') {
        cart[productId]['quantity'] -= 1;

        if (care['productId'] <= 0) {
            delete cart[productId];
        }
    }
    console.log(cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ';domain=;path=/';
}

const updateUserCart = (action, productId) => {
    console.log('User authenticated')
    
    const url = '/update_cart';

    fetch(url, {
        method: 'POST',
        headers: {
            "Content-type": 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({ action, productId})
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        location.reload();
    })
    .catch(error => console.log("Error: ", error));
}