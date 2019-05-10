#coding:utf8


from datetime import datetime, timedelta

from django.core import serializers

from .forms.login import LoginForm

from  django.http import JsonResponse


from .models import Wheel,Nav,Mustbuy,Shop,MainShow,FoodType,Goods,User,Cart,Order

from django.shortcuts import render,redirect


import time
import  random
from  django.conf import  settings
import os

import logging
import django.utils.log
import logging.handlers



log = logging.getLogger('changecart')


def home(request):
    wheelsList = Wheel.objects.all()
    navList = Nav.objects.all()
    mustbuyList = Mustbuy.objects.all()

    shopList = Shop.objects.all()
    shop1 = shopList[0]
    shop2 = shopList[1:3]
    shop3 = shopList[3:7]
    shop4 = shopList[7:11]

    mainList = MainShow.objects.all()





    return render(request,'axf/home.html',{"title":"主页",
                                           "wheelsList":wheelsList,
                                           "navList":navList,
                                           "mustbuyList":mustbuyList,
                                           "shop1":shop1,
                                           "shop2": shop2,
                                           "shop3": shop3,
                                           "shop4": shop4,
                                           "mainList":mainList})


def market(request,categoryid,cid,sortid):
    leftSlider = FoodType.objects.all()

    if cid =='0':
        productList = Goods.objects.filter(categoryid=categoryid)
    else:
        #与的关系,比如是优先水果的的国产水果
        productList = Goods.objects.filter(categoryid=categoryid,childcid=cid)


    #排序
    if sortid == '1':
        productList = productList.order_by("productnum")
    elif sortid == '2':
        productList = productList.order_by("price")
    elif sortid == '3':
        productList = productList.order_by("-price")




    group = leftSlider.get(typeid=categoryid)
    chlidList = []
    #全部分类:0#进口水果:103534#国产水果:103533
    childnames = group.childtypenames

    arr1 = childnames.split("#")
    for str in arr1:
        #全部分类:0
        arr2 = str.split(":")
        obj = {"childName":arr2[0],"chlidId":arr2[1]}
        chlidList.append(obj)


    #拿已经加入购物车的数据
    cartLsit = []
    #判断是否登录
    token = request.session.get("token")
    if token:
        user = User.objects.get(userToken=token)
        cartLsit = Cart.objects.filter(userAccount = user.userAccount)

    #<!--显示加入购物车的该商品的数量--> 增加个一个 num 属性
    for p in productList:
        for c in cartLsit:
            if c.productid == p.productid:
                p.num = c.productnum
                continue



    return render(request,'axf/market.html',{"title":"闪送超市",
                                             "leftSlider":leftSlider,
                                             "productList":productList,
                                             "chlidList":chlidList,
                                             "categoryid":categoryid,
                                             "cid":cid})



def cart(request):
    carslists = []
    #首先判断用户是否登录
    token = request.session.get("token")
    if token != None:
        user = User.objects.get(userToken=token)
        carslists = Cart.objects.filter(userAccount = user.userAccount)


    return render(request,'axf/cart.html',{"title":"购物车","carslists":carslists})

#修改购物车
def changecart(request,flag):
    #首先判断用户是否登录
    token = request.session.get("token")
    if token == None:
        #没登录    ajxs 是不能从定向的
        return JsonResponse({"data":-1,"status":"error"})

    #已经登陆过了
    productid = request.POST.get("productid")

    product = Goods.objects.get(productid = productid)
    user = User.objects.get(userToken = token)

    #开始处理数据
    if flag == "0":
        #存储
        if product.storenums == 0:
            return JsonResponse({"data": -2, "status": "error"})

        carts = Cart.objects.filter(userAccount = user.userAccount)
        c = None

        if carts.count() == 0:
            #直接增加一个一条订单
            # 订单号
            oid = time.time() + random.randrange(1, 10000)
            oid = "%d" % oid

            c = Cart.createcart(user.userAccount, productid, 1, product.price, True, product.productimg, product.productlongname,oid, False )
            c.save()

        else:
            try:
                c = carts.get(productid = productid)
                #修改数量和价格
                c.productnum += 1
                c.productprice = "%.2f"%(float(product.price) * c.productnum)
                c.save()

            except Cart.DoesNotExist as e:
                # 直接增加一个一条订单
                oid = time.time() + random.randrange(1, 10000)
                oid = "%d" % oid

                c = Cart.createcart(user.userAccount, productid, 1, product.price, True, product.productimg,
                                    product.productlongname, oid, False)
                c.save()

        #库存减一
        product.storenums -= 1
        product.save()
        return  JsonResponse({"data":c.productnum,"price":c.productprice,"status":"success"})

    elif flag == "1":

        carts = Cart.objects.filter(userAccount = user.userAccount)
        c = None

        if carts.count() == 0:
            return JsonResponse({"data":-2,"status":"error"})
        else:
            try:
                c = carts.get(productid = productid)
                #修改数量和价格
                c.productnum -= 1
                c.productprice = "%.2f"%(float(product.price) * c.productnum)

                #如果为0 物理删除购物车
                if c.productnum == 0:
                    c.delete()
                else:
                    c.save()

            except Cart.DoesNotExist as e:
                # 没有这条订单
                return JsonResponse({"data": -2, "status": "error"})


        #库存加一
        product.storenums += 1
        product.save()
        return JsonResponse({"data": c.productnum,"price":c.productprice,"status": "success"})


    elif flag == "2":
        carts = Cart.objects.filter(userAccount=user.userAccount)
        c = carts.get(productid=productid)
        c.isChose = not c.isChose
        c.save()
        str = ""
        if c.isChose:
            str = "√"

        return JsonResponse({"data":str, "status": "success"})


    # elif flag == "3":
    #     pass


#保存订单 (下订单)
def saveorder(request):
    #首先判断用户是否登录
    token = request.session.get("token")
    if token == None:
        #没登录
        return JsonResponse({"data":-1,"status":"error"})

    user = User.objects.get(userToken=token)
    carts = Cart.objects.filter(isChose = True)
    if carts.count() == 0:
        return JsonResponse({"data": -1, "status": "error"})

    #订单号
    oid = time.time() + random.randrange(1,10000)
    oid = "%d"%oid
    orders = Order.createorder(oid,user.userAccount,0)
    orders.save()

    for item in carts:
        item.isDelete = True
        item.orderid = oid
        item.save()
    return JsonResponse({"status": "success"})





def mine(request):
    username = request.session.get("username","未登录")

    return render(request,'axf/mine.html',{"title":"我的","username":username})





def login(request):

    if request.method =="POST":
        f = LoginForm(request.POST)
        if f.is_valid():
            #信息的格式是没有多大的问题了，验证账号账号和密码的正确性
            print ("**********")
            nameid = f.cleaned_data["username"]
            pswd = f.cleaned_data["passwd"]



            #去数据库查找数据
            try:
                user = User.objects.get(userAccount=nameid)
                if user.userPasswd != pswd:
                    #
                    return redirect('/login/')

            except User.DoesNotExist as e:
                return redirect('/login/')



            #登录成功的了
            token = time.time() + random.randrange(1, 100000)
            user.userToken = str(token)
            user.save()

            #存 session 保存最新的的 session
            request.session['username'] = user.userName
            request.session['token'] = user.userToken



            return  redirect('/mine/')
        else:
            return render(request, 'axf/login.html', {"title": "登录", 'form': f,
                                                      "error":f.errors})
    else:
        f = LoginForm()

    return render(request,'axf/login.html',{"title":"登录",'form':f})





#注册
def register(request):
    if request.method =="POST":
        userAccount = request.POST.get("userAccount")
        userPasswd = request.POST.get("userPasswd")
        userName = request.POST.get("userName")
        userPhone = request.POST.get("userPhone")
        userAddress = request.POST.get("userAddress")
        userRank = 0

        token = time.time() + random.randrange(1,100000)
        userToken = str(token)



        f = request.FILES["userImg"]
        userImg  = os.path.join(settings.MEDIA_ROOT,userAccount + ".png")
        with open(userImg,'wb') as fp:
            for data in f.chunks():
                fp.write(data)
            fp.close()


        user = User.createuser(userAccount,userPasswd,userName,userPhone,userAddress,userImg,userRank,userToken)
        user.save()


        #注册成功后
        request.session['username'] = userName
        request.session['token'] = userToken

        return redirect('/mine/')

    else:
        pass



    return  render(request,'axf/register.html',{"title":'注册'})

def checkuserid(request):
    userid = request.POST.get("userid")
    try:
        user = User.objects.get(userAccount = userid)
        return JsonResponse({"data":"该用户已经被注册了","status":"error"})
    # 返回json　数据
    except User.DoesNotExist as e:
        return JsonResponse({"data":"可以注册","status":"success"})


#退出登录
from django.contrib.auth import logout
def quit(request):
    logout(request)
    return redirect('/mine/')


