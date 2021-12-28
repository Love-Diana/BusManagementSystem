from django.shortcuts import render
from models import *

# 跳转map
menu_map={"1":"addDriver.html","2":"addMotor.html","3":"addFine.html",
              "4":"drviers.html","5":"select_driver_fines.html","6":"fineCounts.html"}

# 默认页面
def menu(request):
    return render(request, 'menu.html')

# 进入页面
def enter(request):
    if request.method=="POST":
        menu=request.POST.get("menu")       
    return render(request,menu_map[menu])

# 添加司机
def add_driver(request):
    pass

# 添加车辆
def add_motor(request):
    pass

# 添加违章
def add_fine(request):
    pass

# 查询车队下的司机
def select_drivers(request):
    pass

# 查询司机违章的详细信息
def select_fine(request):
    pass

# 统计一个车队下的违章
def fine_count(request):
    pass