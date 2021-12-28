from django.shortcuts import render
from data.models import *


# 默认页面
def menu(request):
    return render(request, 'menu.html')


# 进入页面
def enter(request):
    menu_map = {"1": "addDriver.html", "2": "addMotor.html", "3": "addFine.html",
                "4": "drivers.html", "5": "select_driver_fines.html", "6": "fineCounts.html"}
    if request.method == "POST":
        menu = request.POST.get("menu")
        return render(request, menu_map[menu])
    else:
        return render(request, "error.html")


# 添加司机
def add_driver(request):
    try:
        temp = Driver()
        temp.ID = request.POST.get("ID")
        temp.name = request.POST.get("name")
        temp.sex = request.POST.get("sex")
        temp.belongs = request.POST.get("road")
        Driver.save(temp)
        return render(request, "success.html")
    except:
        return render(request, "error.html")


# 添加车辆
def add_motor(request):
    try:
        temp = Motors()
        temp.ID = request.POST.get("ID")
        temp.seats = request.POST.get("seats")
        Motors.save(temp)
        return render(request, "success.html")
    except:
        return render(request, "error.html")


# 添加违章
def add_fine(request):
    try:
        temp = Punishment()
        driver = Driver.objects.get(ID=request.POST.get("driver"))
        temp.driverID = request.POST.get("driver")
        temp.drivername = driver.name
        temp.belongs = driver.belongs
        temp.carID = request.POST.get("motor")
        temp.station = request.POST.get("station")
        temp.type = request.POST.get("type")
        temp.time = request.POST.get("time")
        Punishment.save(temp)
        return render(request, "success.html")
    except:
        return render(request, "error.html")


# 查询车队下的司机
def select_drivers(request):
    drivers = Driver.objects.filter(belongs="303")
    print(drivers)
    return render(request,"showDriver.html",{"drivers":drivers})


# 查询司机违章的详细信息
def select_fine(request):
    pass


# 统计一个车队下的违章
def fine_count(request):
    pass
