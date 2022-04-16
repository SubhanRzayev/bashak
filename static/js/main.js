////////////////////////////////// dropdown menu

$(".drop-btn .c").on('click', function(){
  let subId = $(this).data('sub');
  if(subId){
  $(".submenu:not(#"+subId+")").removeClass('show');
  $("#"+subId).toggleClass("show");
  }
    
  });


////////////////////////////////// dropdown menu end




$(".bar").click(function () {
$("#navv").toggleClass("active");   
})


var Menu = {

el: {
  ham: $('.menu'),
  menuTop: $('.menu-top'),
  menuMiddle: $('.menu-middle'),
  menuBottom: $('.menu-bottom')
},

init: function() {
  Menu.bindUIactions();
},

bindUIactions: function() {
  Menu.el.ham
      .on(
        'click',
      function(event) {
      Menu.activateMenu(event);
      event.preventDefault();
    }
  );
},

activateMenu: function() {
  Menu.el.menuTop.toggleClass('menu-top-click');
  Menu.el.menuMiddle.toggleClass('menu-middle-click');
  Menu.el.menuBottom.toggleClass('menu-bottom-click'); 
}
};

Menu.init();





  const body2 = document.querySelector(".img-box");
  const li2 = document.querySelectorAll(".card2");



  li2.forEach(el => {
    el.addEventListener("mouseover", () => {
      let bg = el.getAttribute("data-bg");
      body2.style.background = `url(${bg})no-repeat center /cover`;
    });
  });


$(".drop-one-1[data-sub='item1']").click(function () {
if( ! $(this).children(".drop-down").hasClass("rotate")){
    let bg = $(".card3").first().attr('data-bg');
    $(".img-box3").css('background', `url(${bg})no-repeat center /cover`);
}
})

  
  const body3 = document.querySelector(".img-box3");
  const li3 = document.querySelectorAll(".card3");





  li3.forEach(el => {
    el.addEventListener("mouseover", () => {
      let bg = el.getAttribute("data-bg");
      body3.style.background = `url(${bg})no-repeat center /cover`;
    });
  });

    $(".drop-one-1[data-sub='item2']").click(function () {
        if( ! $(this).children(".drop-down").hasClass("rotate")){
            let bg = $(".card2").first().attr('data-bg');
            $(".img-box").css('background', `url(${bg})no-repeat center /cover`);
        }
    })





  jQuery(document).ready(function (e) {
    function t(t) {
        e(t).bind("click", function (t) {
            t.preventDefault();
            e(this).parent().fadeOut()
        })
    }
    e(".dropdown-toggle2").click(function () {
        var t = e(this).parents(".button-dropdown").children(".dropdown-menu").is(":hidden");
        e(".button-dropdown .dropdown-menu").hide();
        e(".button-dropdown .dropdown-toggle2").removeClass("active");
        if (t) {
            e(this).parents(".button-dropdown").children(".dropdown-menu").toggle().parents(".button-dropdown").children(".dropdown-toggle").addClass("active")
        }
    });
    e(document).bind("click", function (t) {
        var n = e(t.target);
        if (!n.parents().hasClass("button-dropdown")) e(".button-dropdown .dropdown-menu").hide();
    });
    e(document).bind("click", function (t) {
        var n = e(t.target);
        if (!n.parents().hasClass("button-dropdown")) e(".button-dropdown .dropdown-toggle2").removeClass("active");
    })
});



  $(".drop-one-1").click(function () {
      $('.drop-one-1').not(this).each(function(){
          $(this).find(".drop-down").removeClass("rotate");
      });

    $(this).find(".drop-down").toggleClass("rotate");
})

$(".lang").click(function () {
  $(this).find(".drop-down").toggleClass("rotate2");
})




$('.main-slide').owlCarousel({
loop:true,
nav:false,
items:1,
video:true

})

$('.second-slide').owlCarousel({
  loop:false,
  dots:false,
  items:2,
  autoWidth: true,
  margin:20,
  nav:false,
  autoplay:false,
  autoplayTimeout:2000,
  autoplayHoverPause:false
  })

  $('.third-slide').owlCarousel({
    loop:false,
    dots:false,
    items:2,
    autoWidth: true,
    margin:20,
    nav:false,
    autoplay:false,
    autoplayTimeout:2000,
    autoplayHoverPause:false
    })






  $(document).ready(function(){
    $(window).scroll(function(){
        var scroll = $(window).scrollTop();
        if (scroll > 300) {
          $(".scrolling").css("background" , "rgba(26, 26, 26, 0.7)" );
        }
  
        else{
            $(".scrolling").css("background" , "transparent");  	
        }
    })
  })


  $(document).ready(function(){
    $(window).scroll(function(){
        var scroll2 = $(window).scrollTop();
        if (scroll2 > 300) {
          $(".scrolling2").css("background" , "rgba(0, 147, 95, 0.7)" );
        }
  
        else{
            $(".scrolling2").css("background" , "transparent");  	
        }
    })
  })


  
// $(document).ready(function(){
// $(window).scroll(function(){
//   var scroll = $(window).scrollTop();
//   if (scroll > 300) {
//     $(".black").css("color" , "white");
//   }

//   else{
//       $(".black").css("color" , "black");  	
//   }
// })
// })


// $(document).ready(function(){
// $(window).scroll(function(){
//   var scroll = $(window).scrollTop();
//   if (scroll > 300) {
//     $(".black a").css("color" , "white");
//   }

//   else{
//       $(".black a").css("color" , "black");  	
//   }
// })
// })


// $(document).ready(function(){
// $(window).scroll(function(){
//   var scroll = $(window).scrollTop();
//   if (scroll > 300) {
//     $(".change-lang-color a").css("color" , "white");
//   }

//   else{
//       $(".change-lang-color a").css("color" , "black");  	
//   }
// })
// })



// $(function(){
// $(window).scroll(function(){
//   if($(this).scrollTop()>300){
//       $(".change-icon  img").attr("src","assets/svg/dropdown-arrow.svg");
//   }

//   else{
//       $(".change-icon  img").attr("src","assets/svg/arrow-black.svg");
//   }
// })
// })



// $(function(){
// $(window).scroll(function(){
//   if($(this).scrollTop()>300){
//       $(".change-icon2  img").attr("src","assets/svg/right-arrow.svg");
//   }

//   else{
//       $(".change-icon2  img").attr("src","assets/svg/arrow-black-right.svg");
//   }
// })
// })


// $(function(){
// $(window).scroll(function(){
//   if($(this).scrollTop()>300){
//       $(".change-logo img").attr("src","assets/svg/logo.svg");
//   }

//   else{
//       $(".change-logo img").attr("src","assets/svg/logo2.svg");
//   }
// })
// })
