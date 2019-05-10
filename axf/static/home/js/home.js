$(document).ready(function(){

    setTimeout(function () {
          myTopSwiper();
        myMustbySwiper();

    },100)


})


//轮播图不能轮播．．？


function myTopSwiper(){

    var mySwiper1 = new Swiper("#topSwiper", {
        direction:'horizontal',
        loop: true,
        speed:500,
        autoplay:2000,
        pagination:'.swiper-pagination',
        control:true,
    })
}



function myMustbySwiper(){

    var mySwiper1 = new Swiper("#swiperMenu", {
        slidesPerView:3,
        paginationClickable:true,
        spaceBetween:2,
        control:false,
    })
}






