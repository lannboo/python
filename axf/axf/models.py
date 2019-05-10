#coding:utf8

from django.db import models



class Wheel(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)




class Nav(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)

class Mustbuy(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)

class Shop(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)


class MainShow(models.Model):
    trackid = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    img = models.CharField(max_length=100)
    categoryid = models.CharField(max_length=10)
    brandname = models.CharField(max_length=20)

    img1 = models.CharField(max_length=100)
    childcid1 = models.CharField(max_length=10)
    productid1 = models.CharField(max_length=10)
    longname1 = models.CharField(max_length=50)
    price1 = models.CharField(max_length=10)
    marketprice1 = models.CharField(max_length=10)

    img2 = models.CharField(max_length=100)
    childcid2 = models.CharField(max_length=10)
    productid2 = models.CharField(max_length=10)
    longname2 = models.CharField(max_length=50)
    price2 = models.CharField(max_length=10)
    marketprice2 = models.CharField(max_length=10)

    img3 = models.CharField(max_length=100)
    childcid3 = models.CharField(max_length=10)
    productid3 = models.CharField(max_length=10)
    longname3 = models.CharField(max_length=50)
    price3 = models.CharField(max_length=10)
    marketprice3 = models.CharField(max_length=10)



class FoodType(models.Model):
    typeid = models.CharField(max_length=60)
    typename = models.CharField(max_length=100)
    childtypenames = models.CharField(max_length=200)
    typesort = models.IntegerField(default=1)



class Goods(models.Model):
    # 商品的id
    productid = models.CharField(max_length=16)
    # 商品的图片
    productimg = models.CharField(max_length=200)
    # 商品的名称
    productname = models.CharField(max_length=100)
    # 商品的长名字
    productlongname = models.CharField(max_length=200)
    #是否买一赠一
    isxf = models.IntegerField(default=1)
    #
    pmdesc = models.CharField(max_length=100)
    # 规格
    specifics = models.CharField(max_length=100)
    #价格 # 商品的折后价格
    price = models.FloatField(default=0)
    # 商品的原价
    marketprice = models.FloatField(default=1)
    # 组id
    categoryid = models.CharField(max_length=16)
    # 子分类组的id
    childcid = models.CharField(max_length=16)
    # 子分类的名称
    childcidname = models.CharField(max_length=100)
    # 详情页 id
    dealerid = models.CharField(max_length=16)
    # 库存
    storenums = models.IntegerField(default=1)
    # 销量排序
    productnum = models.IntegerField(default=1)

#用户模型
class User(models.Model):
    #用户账号，要唯一
    userAccount = models.CharField(max_length=20,unique=True)
    #密码
    userPasswd = models.CharField(max_length=20)
    #昵称
    userName = models.CharField(max_length=20)
    #手机号
    userPhone = models.CharField(max_length=20)
    #地址
    userAddress = models.CharField(max_length=100)
    #头像地址
    userImg = models.CharField(max_length=150)
    #等级
    userRank = models.IntegerField()
    #touken 验证值，每次登录都会跟新
    userToken = models.CharField(max_length=100)
    @classmethod
    def createuser(cls,account,passwd,name,phone,address,img,rank,token):
        u = cls(userAccount=account,userPasswd=passwd,userName=name,
                userPhone=phone,userAddress=address,userImg=img,
                userRank=rank,userToken=token)
        return u


    # class Meta:
    #     db_table = 'axf_user'
    #


class CartManaage1(models.Manager):
    def get_queryset(self):
        return super(CartManaage1, self).get_queryset().filter(isDelete = False)


# class CartManaage2(models.Manager):
#     def get_queryset(self):
#         return super(CartManaage2, self).get_queryset().filter(isDelete = True)



#购物车表

# 用户id   商品id  数量   总价 是否选中   图片 长名字  属于哪个订单 isDelete


class Cart (models.Model):
    userAccount = models.CharField(max_length=20)
    productid = models.CharField(max_length=10)
    productnum = models.IntegerField()
    productprice = models.CharField(max_length=10)
    isChose = models.BooleanField(default=True)
    productimg = models.CharField(max_length=150)
    productname = models.CharField(max_length=200)
    orderid = models.CharField(max_length=20,default="0")
    isDelete = models.BooleanField(default=False)

    objects = CartManaage1()
    # obj2 = CartManaage2()

    @classmethod
    def createcart(cls,userAccount,productid,productnum,
                   productprice,isChose,productimg,productname,orderid,isDelete):
        c = cls(userAccount = userAccount,productid = productid,productnum = productnum,
                productprice = productprice,isChose = isChose,productimg = productimg,
                productname = productname,orderid = orderid,isDelete = isDelete)
        return c





#订单表
# 订单id (唯一的)   用户 id    进度

class Order(models.Model):
    orderid = models.CharField(max_length=20)
    userid = models.CharField(max_length=20)
    progress = models.IntegerField()

    @classmethod
    def createorder(cls,orderid,userid,progress):
        o = cls(orderid=orderid,userid=userid,progress=progress)
        return o




