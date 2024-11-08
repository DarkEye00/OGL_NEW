function sendMail(){
    var params = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        subject: document.getElementById("subject").value,
        message: document.getElementById("message").value
    }
    const SERVICE_ID = "service_tfb6x0i";
    const TEMPLATE_ID = "template_e2ym2rr";

    emailjs.send(SERVICE_ID, TEMPLATE_ID, params).then(

        res => {
            document.getElementById("name").value="";
            document.getElementById("email").value="";
            document.getElementById("subject").value="";
            document.getElementById("message").value="";
            console.log(res);

            
            
        }
    ).catch((err) => console.log(err))
}

function quoteMail(){
    var params = {
        Company: document.getElementById("company").value,
        Email: document.getElementById("Email").value,
        Phone: document.getElementById("phone").value,
        message: document.getElementById("message").value
    }
    const SERVICE_ID = "service_j2n7h76";
    const TEMPLATE_ID = "template_t5qq68l";

    emailjs.send(SERVICE_ID, TEMPLATE_ID, params).then(

        quote => {
            document.getElementById("company").value="";
            document.getElementById("Email").value="";
            document.getElementById("phone").value="";
            document.getElementById("message").value="";
            console.log(quote);

            alert("Your Quote has been recieved and we shall get back to you!");
        }
    ).catch((err) => console.log(err))
}

