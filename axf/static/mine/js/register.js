$(document).ready(function () {




    account = document.getElementById("account")
    accounterr = document.getElementById("accounterr")
    checkerr = document.getElementById("checkerr")


    pass = document.getElementById("pass")
    passerr = document.getElementById("passerr")


    passwd = document.getElementById("passwd")
    passwderr = document.getElementById("passwderr")




    account.addEventListener("focus",function () {
        accounterr.style.display = "none"
        checkerr.style.display = "none"
    },false)

    account.addEventListener("blur",function () {
        var  inputStr = this.value
        if (inputStr.length < 6 || inputStr.length > 12){
           accounterr.style.display = "block"
            return
        }

        $.post("/checkuserid/",{"userid":inputStr},function (data) {
            if (data.status == "error"){
                checkerr.style.display = "block"
            }
        })

    },false)





    pass.addEventListener("focus",function () {
        passerr.style.display = "none"
    },false)

    pass.addEventListener("blur",function () {
        var  inputStr = this.value
        if (inputStr.length < 6 || inputStr.length > 16){
           passerr.style.display = "block"
            return
        }

    },false)

    passwd.addEventListener("focus",function () {
        passwderr.style.display = "none"
    },false)

    passwd.addEventListener("blur",function () {
        var  inputStr = this.value
        // 两次密码是否一样
        if (inputStr != pass.value){
           passwderr.style.display = "block"
            return
        }

    },false)


})

