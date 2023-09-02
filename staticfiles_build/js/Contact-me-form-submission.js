



var contactform = document.getElementById('ContactMeForm');


// let csrftoken = formData.get("csrfmiddlewaretoken")
// // console.log(csrftoken)
// let options = {
//     method: "POST",
//     headers: {
//         "Content-type": "application/json",
//         'X-CSRFToken': csrftoken
//     },
//     body: JSON.stringify(formData),

// }
contactform.addEventListener('submit', event => {
    event.preventDefault();
    const formData = new FormData(contactform)
    console.log(Array.from(formData));
    let formDataObject = Object.fromEntries(formData.entries());
    let csrftoken = formData.get("csrfmiddlewaretoken")
    Options = {
        method: "POST",
        headers: {
            "Content-type": "application/json",
            'X-CSRFToken': csrftoken,
            'encoding': 'utf-8'
        },
        body: JSON.stringify(formDataObject),

    }
    console.log(Options.body)
    let fetchr = fetch("/contact-me/", Options)
    fetchr.then(response => {
        console.log(response);
        if (response.ok) {
            return response.json()
        }
        throw new Error(

        )
    }).then(data => {
        console.log('Success:', data);
        contactform.reset();
        document.getElementById("output-message").innerText = "Your enquiry has been sent!"
        setTimeout(function () {
            document.getElementById("output-message").style.display = "none";
        }, 3000);
        setTimeout(function () {
            document.getElementById("output-message").style.display = "";
        }, 1000);
        // setTimeout(function () {
        //     document.getElementById("closecontactmodal").click()
        // }, 5000);

    })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById("output-message").innerText = "Sorry! There was an error submitting your enquiry. "
            setTimeout(function () {
                document.getElementById("output-message").style.display = "none";
            }, 3000);
            setTimeout(function () {
                document.getElementById("output-message").style.display = "";
            }, 1000);
        });


});



