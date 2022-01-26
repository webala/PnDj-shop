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

        },
        body: {action, productId}
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.log(error));
}