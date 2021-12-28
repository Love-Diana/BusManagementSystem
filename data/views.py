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


# 查询车队下的司机 TODO
def select_drivers(request):
    try:
        drivers=[]
        roads=Road.objects.filter(belongs=request.POST.get("ID"))
        for road in roads:
            drivers.append(Driver.objects.filter(belongs=road.ID))
        return render(request,"showDriver.html",{"drivers":drivers})
    except:
        return render(request, "error.html")


# 查询司机违章的详细信息 
def select_fine(request):
    try:
        driverID=request.POST.get("ID")
        driver=Driver.objects.get(ID=driverID)
        name=driver.name
        start=request.POST.get("start")
        end=request.POST.get("end")
        fines=Punishment.objects.filter(driverID=driverID,time__range=(start,end))
        return render(request,"showFines.html",{"name":name,"fines":fines})
    except:
        return render(request, "error.html")

# 统计一个车队下的违章 TODO
def fine_count(request):
    try:
        fines=[]
        roads=Road.objects.filter(belongs=request.POST.get("ID"))
        start=request.POST.get("start")
        end=request.POST.get("end")
        for road in roads:
            fines.append(fines=Punishment.objects.filter(belongs=road.ID,time__range=(start,end)))
        # das 
    except:
        return render(request, "error.html")
