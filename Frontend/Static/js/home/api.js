function getCsrf() {
    var inputElems = document.querySelectorAll('input');
    var csrfToken = '';
    for (i = 0; i < inputElems.length; ++i) {
        if (inputElems[i].name === 'csrfmiddlewaretoken') {
            csrfToken = inputElems[i].value;
            break;
        }
    }
    return csrfToken;
};


async function postData(url = '', data = {}) {

    const response = await fetch(url, {

        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            "X-CSRFToken": getCsrf()
        },
        credentials: 'same-origin',
        body: JSON.stringify(data) // body data type must match "Content-Type" header
    });
    return response.json(); // parses JSON response into native JavaScript objects
}

