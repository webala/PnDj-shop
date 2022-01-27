const user_info_div = document.querySelector('#user-information');


user != 'AnonymousUser' ? user_info_div.classList.add('d-none') : user_info_div.classList.remove('d-none');

completeOrderBtn = document.querySelector('#complete-order');
shipping_formEl = document.getElementById('shipping-form');

shipping_formEl.addEventListener('submit', (e) => {
    e.preventDefault();
    const shipping_form = e.target
    
    const formData = new FormData(shipping_form);

    //gives array of entries with name and value
    const entries = formData.entries();
    //converts array of entries into an object
    const data = Object.fromEntries(entries);
    delete data.csrfmiddlewaretoken;
    console.log(JSON.stringify(data));
    
    

    const url = '/process_order';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(data)
    }).then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.log('Error: ', error))
    
})

