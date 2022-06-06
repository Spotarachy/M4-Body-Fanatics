/* 
Js Copied from completed project.
CSS is from: https://stripe.com/docs/stripe-js 

*/

var stripePublickey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublickey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#555',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

// realtime card element to check for errors
card.addEventListener('change', function (event){
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html =`
            <span class="icon" role="alert">
            <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// taken from Stripe, this well Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({'disabled': true});
    $('#submit-button').attr('disabled', true);
    $('#payment-from').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            $('#payment-from').fadeToggle(100);
            $('#loading-overlay').fadeToggle(100);
            card.update({'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});