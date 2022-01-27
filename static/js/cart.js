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
    })
})

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