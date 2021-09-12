$(document).ready(function(){
    var form=$('#form_buying_tovar');
    console.log(form);
    form.on('submit', function(e){
         e.preventDefault();
         console.log('123');
         var kol=$('#kolvo').val();
         console.log(kol);
         var btn=$('#submit_btn');
         var product_id=btn.data('tovar_id');
         var product_name=btn.data('tovar_name')
         var product_price=btn.data('tovar_price')

         console.log(product_id);


         $('.basket-it ul').append('<li> '+ +'<li>')
         })

function basketfun(){
$.preventDefault()
$('.basket-it').toggleClass('d-none');
}

        $('.basket-container').on('click', function(e){
        basketfun();
        })

          $('.basket-container').mouseover(function(e){
         basketfun();
         })

           $('.basket-container').mouseout(function(e){
         basketfun();

//или

         $('.basket-container').on('click', function(e){
         $.preventDefault();
         $('.basket-it').addClass('d-none');
         })

         $('.basket-container').mouseover(function(e){
         $('.basket-it').removeClass('d-none');
         })

           $('.basket-container').mouseout(function(e){
         $('.basket-it').addClass('d-none');
         })

});