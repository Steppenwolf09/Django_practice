$(document).ready(function(){
    var form=$('#form-buy');
    form.on('submit', function(e){
         e.preventDefault();

         var kol=$('#kol').val();
          console.log(kol)
          var but=$('#buy-button');
          console.log(but);
          var id=but.data('id');
          var name=but.data('name');
          var price=but.data('price');
          var disc=but.data('discount');


          var data={};

          data.id=id;
          data.kol=kol;
          var csrf_token = $('#form-buy [name="csrfmiddlewaretoken"]').val();
          data["csrfmiddlewaretoken"]=csrf_token;
          var url=form.attr("action");

          $.ajax({
             url:url,
             type:'POST',
             data:data,
             cache:true,
             success:function(data){
             $('.basket-it ul').html("")
                console.log(data);
                $.each(data.tovars, function(k,v){
                $('.basket-it ul').append(' <li class="libasket'+v.tovar_id+'" style="width:300px">'+v.name+' x '+v.nmb+'  <br> '+v.total_price+' рубликов</li><button id="remove_from_baskbut" type="button" class="btn btn-outline-danger deltovbasket"  data-id='+v.tovar_id+' > X </button>')

                });
                console.log("Збс");



                $('#kolvo_tovars_in_basket').text('(' +data.kolvo_tovar_in_basket+ ')')},
             error:function(data){
                console.log("ошибочка вышла");},
                }

            )



//          if (disc !=''){
//             var newprice=price-(price/100)*disc;
//
//             $('.basket-it ul').append('<li class="libasket" style="width:300px">'+name+' x '+kol+' <button type="submit" class="btn btn-outline-danger deltovbasket" > X</button><br>'+price+' рубликов </li>');
//             }
//          else {$('.basket-it ul').append('<li class="libasket" style="width:300px">'+name+' x '+kol+'<button type="submit" class="btn btn-outline-danger deltovbasket" > X</button><br> по цене <br> '+price+' рубликов </li>');}


});


        $('#basketcontimg').on('click', function(e){
        e.preventDefault();
        $('.basket-it').removeClass('d-none');
       })

         $('.basket-it').mouseover(function(){
        $('.basket-it').removeClass('d-none');
       })

        $('.basket-it').mouseout(function(){
        $('.basket-it').addClass('d-none')})

        $('#basketcontimg').mouseover(function(){
        $('.basket-it').removeClass('d-none')})

        $('#basketcontimg').mouseout(function(){
        $('.basket-it').addClass('d-none')})


        $('body').on('click', '#remove_from_baskbut', function(e) {


         var knopka=$('#remove_from_baskbut');
         var id=knopka.data('id');
         var formochka=$('#basket_form');
         var data={};
         data.id=id;

          var csrf_token = $('#basket_form [name="csrfmiddlewaretoken"]').val();
          data["csrfmiddlewaretoken"]=csrf_token;
          var url=formochka.attr("action");




         $.ajax({
             url:url,
             type:'POST',
             data:data,
             cache:true,
             success:function(data){
             var idd=data.remove_tovar
             console.log(data.remove_tovar)
             console.log('.libasket'+idd)
             $('.libasket'+idd).remove();
             $('#remove_from_baskbut').remove();
             $('#kolvo_tovars_in_basket').text('('+data.kolvo_tov_in_bask+')');

             console.log("удалили из корзины");},


             error:function(data){
                console.log("ошибочка вышла с корзиной");},
                }

            )
      } );

function total_basket_price(){
      var total_basket_price=0;
      $('.each_tovar_total_price').each(function(){
      total_basket_price+=parseInt($(this).text());
            });
      $('#total_basket_cost').text(total_basket_price);
         }   ;

      $(document).on('change', ".each_tovar_nmb", function(){
         var nmb=$(this).val();
         var price=$(this).data('price');

         var total_for_each_cost=parseInt(price)*parseInt(nmb);
         current=$(this).closest('.row');
         current.find('.each_tovar_total_price').text(total_for_each_cost);
         total_basket_price();

         });

      total_basket_price();

//      $('body').on('click', '#saving_order', function(e) {
//         var total_cost=$('#total_basket_cost').text();
//
//         nmb=[];
//         $('.each_tovar_nmb').each(function(){
//
//            nmb.push($(this).val());
//            });
//
//         name=[];
//         $('.name_tov_basket').each(function(){
//
//            console.log($(this).text());
//            name.push($(this).text());
//            });
//
//         console.log(name)
//         var data={};
//         data.total=total_cost;
//         data.nmb=nmb
//         data.tovar=name
//         console.log(data)
//         var formochka=$('#saving_order_form');
//         var csrf_token = $('#saving_order_form [name="csrfmiddlewaretoken"]').val();
//         data["csrfmiddlewaretoken"]=csrf_token;
//         var url=formochka.attr("action");
//
//
//
//         $.ajax({
//             url:url,
//             type:'POST',
//             data:data,
//             cache:true,
//             success:function(data){
//             console.log("suc");
//
//             }
//
//
//      })
//      })
});