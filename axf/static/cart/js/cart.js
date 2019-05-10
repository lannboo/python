$(document).ready(function () {



        //修改购物车
    var addShoppings = document.getElementsByClassName("addShopping")
    var subShoppings = document.getElementsByClassName("subShopping")





    for (var i = 0; i < addShoppings.length; i++){
        addShopping = addShoppings[i]
        addShopping.addEventListener("click",function () {
            pid = this.getAttribute("ga")
            $.post("/changecart/0/", {"productid": pid}, function (data) {
                if (data.status == "success") {

                    //增加成功，把中间的span 的innerHTML变成当前的数量
                     if(document.getElementById(pid)){
                         document.getElementById(pid).innerHTML = data.data

                         }
                     if(document.getElementById(pid + "price")){
                         document.getElementById(pid + "price").innerHTML = data.price
                           // console.log("*****price****+1")
                           // console.log(data.price)
                         }

                }

            })

        },false)

    }


        for (var i = 0; i < subShoppings.length; i++){
        subShopping = subShoppings[i]
        subShopping.addEventListener("click",function () {
            pid = this.getAttribute("ga")
            $.post("/changecart/1/", {"productid": pid}, function (data) {
                if (data.status == "success") {

                    //增加成功，把中间的span 的innerHTML变成当前的数量


                    if(document.getElementById(pid)){
                         document.getElementById(pid).innerHTML = data.data
                         }
                         //购物车实时显示到 价格
                    if(document.getElementById(pid + "price")){
                         document.getElementById(pid + "price").innerHTML = data.price
                    }

                    //减到0 把商品 从购物车中删除
                    if (data.data == 0){
                        // window.location.href = "http://127.0.0.1:8000/cart/"

                        var li = document.getElementById(pid + "li")
                        li.parentNode.removeChild(li)


                    }


                }

            })

        },false)

    }

    var iscChoses = document.getElementsByClassName("iscChose")

    //是否选中呀
    for(var i = 0; i < iscChoses.length; i++){

        ischose = iscChoses[i]
        ischose.addEventListener("click",function () {
            pid = this.getAttribute("goodsid")


            // console.log(pid)
            //
            // var  s = document.getElementById(pid+"a")
            // if(s)
            // {
            //     document.getElementById(pid+"a").innerHTML= "√"
            // }

            $.post("/changecart/2/",{"productid": pid},function (data) {
                if (data.status == "success"){

                    //显示没有选中
                    var  s = document.getElementById(pid+"a")
                    if(s)
                    {
                         document.getElementById(pid+"a").innerHTML= data.data
                    }


                }
            })
        },false)
    }


    var ok = document.getElementById("ok")
    ok.addEventListener("click",function () {
        var f = confirm("是否确认下单")
        if(f){
            $.post("/saveorder/",function (data) {
                if (data.status =="success")
                {
                    window.location.href = "http://127.0.0.1:8000/cart/"
                }

            })
        }

    },false)






})
