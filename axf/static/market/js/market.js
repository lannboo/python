$(document).ready(function () {

    var alltypebtn = document.getElementById("all_types")
    var showsortbtn = document.getElementById("sort_rule")



    var typediv = document.getElementById("all_types_container")
    var sortdiv = document.getElementById("sort_container")


    typediv.style.display = "none"
    sortdiv.style.display = "none"

    alltypebtn.addEventListener("click",function () {
        typediv.style.display = "block"
        sortdiv.style.display = "none"

    },false)


    showsortbtn.addEventListener("click",function () {
        typediv.style.display = "none"
        sortdiv.style.display = "block"

    },false)



    typediv.addEventListener("click",function () {
        typediv.style.display = "none"

    },false)


    sortdiv.addEventListener("click",function () {
        sortdiv.style.display = "none"

    },false)

    //修改购物车
    var subShoppings = document.getElementsByClassName("subShopping")
    var addShoppings = document.getElementsByClassName("addShopping")

    for (var i = 0; i < addShoppings.length; i++){
        addShopping = addShoppings[i]


        addShopping.addEventListener("click",function () {
            //获取自定义属性
            pid = this.getAttribute("ga")
            $.post("/changecart/0/",{"productid": pid},function (data) {

                if (data.status=='success') {

                     if(document.getElementById(pid)){
                         window.document.getElementById(pid).innerHTML = data.data
                         }


                }else {
                    if (data.data == -1) {
                         //跳到登录界面
                         window.location.href = "http://127.0.0.1:8000/login/"
                     }
                }

            })

        })

    }


    for (var i = 0; i < subShoppings.length; i++){
        subShopping = subShoppings[i]


        subShopping.addEventListener("click",function () {
            //获取自定义属性
            pid = this.getAttribute("ga")
            $.post("/changecart/1/",{"productid": pid},function (data) {

                if (data.status=='success') {

                     if(document.getElementById(pid)){
                         window.document.getElementById(pid).innerHTML = data.data
                         }


                }else {
                    if (data.data == -1) {
                         //跳到登录界面
                         window.location.href = "http://127.0.0.1:8000/login/"
                     }
                }

            })

        })

    }













})




//
//
//
// $(document).ready(function () {
//
//     $("#all_types").click(function () {
//
//         $("#all_types_container").show();
//         $("#all_type_logo").removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up");
//         $("#sort_container").hide();
//         $("#sort_rule_logo").addClass("glyphicon-chevron-down").removeClass("glyphicon-chevron-up");
//     })
//
//
//     $("#all_types_container").click(function () {
//         $(this).hide();
//         $("#all_type_logo").addClass("glyphicon-chevron-down").removeClass("glyphicon-chevron-up");
//
//     })
//
//
//     $("#sort_rule").click(function () {
//         $("#sort_container").show();
//         $("#sort_rule_logo").addClass("glyphicon-chevron-up").removeClass("glyphicon-chevron-down");
//         $("#all_types_container").hide();
//         $("#all_type_logo").removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");
//     })
//
//     $("#sort_container").click(function () {
//         $(this).hide();
//         $("#sort_rule_logo").addClass("glyphicon-chevron-down").removeClass("glyphicon-chevron-up");
//     })
//     // $("#all_types_container>div>a").click(function () {
//     //     $('#all_types').find("span").text(($(this).find("span").text()))
//     // })
//     // $("#all_types_container>div>a").each(function () {
//     //     $(this).click(function (e) {
//     //         var typeid = $('#market').attr('name')
//     //         var childtypeid = $(this).prop('name')
//     //         urlStr = '/axf/childtype/?typeid='+typeid+'&childtypeid='+childtypeid
//     //         $.ajax({
//     //             type:"get",
//     //             url:urlStr,
//     //             async:true,
//     //             dateType:'json',
//     //             success:function(obj){
//     //             }
//     //         })
//     //     })
//     // })
//     //
//     // $("#sort_container>div>a").click(function () {
//     //     var typeid = $('#market').attr('name')
//     //     urlStr = '/axf/order/order='+$(this).attr('name')
//     //     $.ajax({
//     //         type:"get",
//     //         url:urlStr,
//     //         async:true,
//     //         dateType:'json',
//     //         success:function(obj){
//     //         }
//     //     })
//     // })
//
// //    添加商品到购物车
//     $(".addShopping").click(function () {
//         //    拿到商品id发送给服务器
//         var addShop = $(this);
//         var goodsid = $(this).attr("goodsid");
//         // console.log(goodsid);
//         // console.log($(this).attr("class"));
//         // console.log("**************")
//         // var goodsid2 = $(this).prop("goodsid");
//         // console.log(goodsid2);
//         // console.log($(this).prop("class"));
//
//         $.getJSON("/axf/addtocart/", {"goodsid": goodsid}, function (data) {
//             console.log(data);
//             if (data["status"] == "901") {
//                 window.open("/axf/userlogin/", target = "_self");
//             } else if (data["status"] == "200") {
//                 var g_num = data["g_num"];
//                 var span_num = addShop.prev();
//                 span_num.html(g_num);
//             }
//         })
//
//     })
//
//
//
//     // 添加商品到购物车
//     $(".subShopping").click(function () {
//         //    拿到商品id发送给服务器
//         var subShop = $(this);
//         var goodsid = $(this).attr("goodsid");
//         // console.log(goodsid);
//         // console.log($(this).attr("class"));
//         // console.log("**************")
//         // var goodsid2 = $(this).prop("goodsid");
//         // console.log(goodsid2);
//         // console.log($(this).prop("class"));
//
//         $.getJSON("/axf/subtocart/", {"goodsid": goodsid}, function (data) {
//             console.log(data);
//             if (data["status"] == "901") {
//                 window.open("/axf/userlogin/", target = "_self");
//             } else if (data["status"] == "200") {
//                 var g_num = data["g_num"];
//                 var span_num = subShop.next();
//                 span_num.html(g_num);
//             } else if (data["status"] == "902") {
//                 alert(data["msg"]);
//             }
//         })
//     })
//
//
// })
