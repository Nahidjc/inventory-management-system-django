document.getElementById('itemPrice').addEventListener('keyup', function () {
    getTotalPrice()
})
document.getElementById('quantity').addEventListener('keyup', function () {
    getTotalPrice()
})


function getTotalPrice() {
    const itemPrice = document.getElementById('itemPrice').value;
    const quantity = document.getElementById('quantity').value;
    const totalPrice = parseInt(quantity) * parseFloat(itemPrice);
    document.getElementById('totalPrice').value = totalPrice;
    console.log(totalPrice);
}