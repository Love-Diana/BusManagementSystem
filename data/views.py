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
    try:
        drivers = []
        roads = Road.objects.filter(belongs=request.POST.get("ID"))
        for road in roads:
            temp = Driver.objects.filter(belongs=road.ID)
            for i in temp:
                drivers.append(i)
        print(drivers)
        return render(request, "showDriver.html", {"drivers": drivers})
    except:
        return render(request, "error.html")


# 查询司机违章的详细信息 
def select_fine(request):
    try:
        driverID = request.POST.get("ID")
        driver = Driver.objects.get(ID=driverID)
        name = driver.name
        start = request.POST.get("start")
        end = request.POST.get("end")
        fines = Punishment.objects.filter(driverID=driverID, time__range=(start, end))
        return render(request, "showFines.html", {"name": name, "fines": fines})
    except:
        return render(request, "error.html")


# 统计一个车队下的违章
def fine_count(request):
    try:
        toHtml = []
        data = {}
        fines = []
        roads = Road.objects.filter(belongs=request.POST.get("ID"))
        start = request.POST.get("start")
        end = request.POST.get("end")
        for road in roads:
            temp = Punishment.objects.filter(belongs=road.ID, time__range=(start, end))
            for i in temp:
                fines.append(i)
        for i in fines:
            if i.type not in data:
                data[i.type] = 1
            else:
                data[i.type] += 1
        for i in data:
            temp = types()
            temp.type = i
            temp.number = data[i]
            toHtml.append(temp)
        return render(request, "showCounts.html", {"data": toHtml})
    except:
        return render(request, "error.html")
