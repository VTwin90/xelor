// Disables the ability for the customer to type in a quantity into the quantity input box
$("[type='number']").keypress(function (evt) {
    evt.preventDefault();
});

// Disable +/- buttons outside 1-10 range
    function handleEnableDisable(itemId) {
        const currentValue = parseInt($(`#id_qty_${itemId}`).val());
        const minusDisabled = currentValue < 2;
        const plusDisabled = currentValue > 10;
        $(`#decrement-qty_${itemId}`).prop('disabled', minusDisabled);
        $(`#increment-qty_${itemId}`).prop('disabled', plusDisabled);
    }

    // Ensure proper enabling/disabling of all inputs on page load
    const allQtyInputs = $('.qty_input');
    for(var i = 0; i < allQtyInputs.length; i++){
        const itemId = $(allQtyInputs[i]).data('item_id');
        handleEnableDisable(itemId);
    }

    // Check enable/disable every time the input is changed
    $('.qty_input').change(function() {
        const itemId = $(this).data('item_id');
        handleEnableDisable(itemId);
    });

    // Increment quantity
    $('.increment-qty').click(function(e) {
       e.preventDefault();
       const closestInput = $(this).closest('.input-group').find('.qty_input')[0];
       const currentValue = parseInt($(closestInput).val());
       $(closestInput).val(currentValue + 1);
       const itemId = $(this).data('item_id');
       handleEnableDisable(itemId);
    });

    // Decrement quantity
    $('.decrement-qty').click(function(e) {
       e.preventDefault();
       const closestInput = $(this).closest('.input-group').find('.qty_input')[0];
       const currentValue = parseInt($(closestInput).val());
       $(closestInput).val(currentValue - 1);
       const itemId = $(this).data('item_id');
       handleEnableDisable(itemId);
    });

    