/*
    Core logic/payment flow for this comes from here:
    https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=elements#web-collect-payment-details

    CSS from here: 
    https://docs.stripe.com/elements/appearance-api#rules
*/


var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: { 
        color: '#000',
        fontFamily: '"Urbanist", "Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            // The value '60' has been appended to the color code '#551b8c' below to change the opacity
            color: '#551b8c60',
            fontFamily: '"Urbanist, "Helvetica Neue", Helvetica, sans-serif',
        },
    },
    invalid: {
        color: '#eb1c26',
        iconColor: '#dc3545'
    }
};


var card = elements.create('card', {style: style});
card.mount('#card-element');


// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <div id='card-error-container'>
                <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>${event.error.message}</span>
            </div>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});


// Handle form submit

// Gets the form element and stores it
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {

    // Prevents the default 'POST' behaviour
    ev.preventDefault();
    card.update({ 'disabled': true});

    // Prevents multiple submissions
    $('#submit-button').attr('disabled', true);

    // Sends card info securely using confirmCardPayment method
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <div id=card-error-container>
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>
                </div>`;
            $(errorDiv).html(html);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});