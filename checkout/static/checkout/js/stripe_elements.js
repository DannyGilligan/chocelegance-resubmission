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
        fontSize: '14px',
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


var card = elements.create('card', {
    style: style
});
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

form.addEventListener('submit', function (ev) {

    // Prevents the default 'POST' behaviour when submit button
    // is clicked
    ev.preventDefault();
    card.update({
        'disabled': true
    });

    // Prevents multiple submissions
    $('#submit-button').attr('disabled', true);

    // Triggers loading overlay instead of default behaviour
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    // Variables below apture form data to use in payment intent
    // Boolean value of save info box
    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    // From using {% csrf_token %} in the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

    // Creates bject used to pass information to cache_checkout_data view
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';

    // Posts payment intent data capture above to the cache_checkout_data view
    $.post(url, postData).done(function() {
        // Sends card info securely using confirmCardPayment method
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address: {
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        state: $.trim(form.county.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    postal_code: $.trim(form.postcode.value),
                    state: $.trim(form.county.value),
                }
            },
        }).then(function (result) {
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
    
                // Loading overlay fade
                $('#payment-form').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100);
    
                card.update({
                    'disabled': false
                });
                $('#submit-button').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function () {
        // If there's an error, just reload the page, the error will be in django messages
        location.reload();
    });
});


