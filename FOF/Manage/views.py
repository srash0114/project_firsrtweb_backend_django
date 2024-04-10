from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate 
from django.http import HttpResponse, HttpResponseBadRequest
from .models import *
from django.contrib import messages
from django.http import JsonResponse
from django import forms



def userin4(request):
   if request.user.is_authenticated:
      return render(request, 'Manage/userin4.html')
   else:
      return HttpResponse("Bạn cần phải đăng nhập để gửi phản hồi")

def Logout_page(request):
   logout(request)
   return redirect('logins')

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        eml = request.POST.get('email')
        pw = request.POST.get('password')
        try:
           user = User.objects.get(username=uname)
           messages.error(request, 'Tài khoản đã tồn tại.')
           return redirect('logins')
        except:
           data = User.objects.create_user(uname, eml, pw)
           data.save()
           messages.success(request, 'Tạo tài khoản thành công.')
        return redirect('logins')
    else:
        return render(request, 'Manage/signup.html', {})
    
def logins(request):
   if request.method == 'POST':
      uname = request.POST.get('user')
      pw = request.POST.get('password')
      user = authenticate(request, username=uname, password=pw)
      if user is not None:
        login(request, user)
        return redirect('index')
      else:
         messages.error(request, 'Tài khoản hoặc mật khẩu không đúng.')
   return render(request, 'Manage/login.html', {})


def index(request):
   return render(request, 'Manage/index.html')


def search(request):
    searched = ""  # Default value for searched
    keys = []  # Default value for keys
    if request.method == "POST":
        searched = request.POST["searched"]
        keys = Product.objects.filter(name__contains = searched)
    return render(request, 'Manage/search.html', {"searched":searched , "keys":keys})


def manage(request):
    return render(request, 'app/manage.html')

def get_season_info(request, season_id):
  """
  API endpoint to retrieve information for a specific season.
  """
  try:
    season = Season.objects.get(pk=season_id)
  except Season.DoesNotExist:
    return JsonResponse({'error': 'Season not found'}, status=404)

  data = {
    "season_name": season.season_name,
    "start_time": season.time_start,
    "end_time": season.time_end,
    "profit": season.profit,
  }

  return JsonResponse(data)

def get_land_info(request, land_id):

  try:
    land = Land.objects.get(pk=land_id)
  except Season.DoesNotExist:
    return JsonResponse({'error': 'Land not found'}, status=404)

  data = {
    "id": land.id,
      "name": land.land_name,
      "area": land.land_area,  
      "ph": land.land_pH,
      "moisture": land.land_doAm,  
      "position": land.land_pos
  }

  return JsonResponse(data)

def get_land_by_season(request, season_id):
  """
  Lấy danh sách mảnh đất theo mùa vụ.
  """

  # Lấy dữ liệu mảnh đất
  lands = Land.objects.filter(season=season_id)  # Access season using double underscore

  # Chuẩn bị dữ liệu JSON
  data = []
  for land in lands:
    data.append({
      "id": land.id,
      "name": land.land_name,
      "area": land.land_area,  # Add additional properties as needed
      "ph": land.land_pH,
      "moisture": land.land_doAm,  # Assuming doAm represents moisture
      "position": land.land_pos
    })

  return JsonResponse(data, safe=False)

def get_plant_by_land(request, land_id):
  """
  Lấy danh sách cây trồng theo mảnh đất.
  """

  # Lấy dữ liệu mảnh đất
  plants = Plant.objects.filter(land=land_id)
  

  # Chuẩn bị dữ liệu JSON
  data = []
  for plant in plants:
    data.append({
      "id": plant.id,
      "name": plant.plant_name,
      "timeDev": plant.plant_dev,  # Add additional properties as needed
      "type": plant.plant_type,
      "nd": plant.plant_ND,  # Assuming doAm represents moisture
      "bp": plant.plant_bp
    })

  return JsonResponse(data, safe=False)

def land_form(request):
    if request.method == 'POST':
        land_name = request.POST['land_name']
        land_pos = request.POST['land_pos']
        land_area = request.POST.get('land_area', 0)  # Default value if not provided
        land_pH = request.POST.get('land_pH', 7)  # Default value if not provided
        land_doAm = request.POST.get('land_doAm', 50.00)  # Default value if not provided
        selected_season_id = request.POST['id_mv']

        try:
            season = Season.objects.get(pk=selected_season_id)
        except Season.DoesNotExist:
            return HttpResponseBadRequest('Invalid season ID')

        land = Land.objects.create(
            land_name=land_name,
            land_pos=land_pos,
            land_area=land_area,
            land_pH=land_pH,
            land_doAm=land_doAm,
            season=season
        )

        messages.success(request, "Land created successfully!")
        return redirect("manage")  # Redirect to your desired page after success

    # Get all seasons for the dropdown (if needed in the template)
    season_list = Season.objects.all()
    context = {'season_list': season_list}

    return render(request, "Manage/land_form.html", context)



def plant_form(request):
    if request.method == 'POST':
        plant_name = request.POST['plant_name']
        plant_dev = request.POST.get('plant_dev', 0)  # Default 0 months
        plant_type = request.POST['plant_type']  # Assuming ID for plant type
        plant_ND = request.POST.get('plant_ND', 0)
        plant_bp = request.POST.get('plant_bp', 0)
        selected_land_id = request.POST.get('land_id', None)
        try:
          land = Land.objects.get(pk=selected_land_id)
        except Land.DoesNotExist:
          return HttpResponseBadRequest('Invalid season ID')
       

        # Create new Plant object
        plant = Plant.objects.create(
            plant_name=plant_name,
            plant_dev=plant_dev,
            plant_type=plant_type,
            plant_ND=plant_ND,
            plant_bp=plant_bp, 
            land=land
        )

        messages.success(request, "Plant created successfully!")
        return redirect("manage")  # Redirect to success page (replace with your URL)

    # Get all lands for the dropdown (if needed in the template)
    land_list = Land.objects.all()
    context = {'land_list': land_list}

    return render(request, "Manage/plant_form.html", context)




def home(request):
    season = Season.objects.all()
    land = Land.objects.all()
    plant = Plant.objects.all()
    context = {'season': season, 'land':land, 'plant':plant}
    return render(request, "Manage/manage.html", context)

def m_form(request):
    if request.method == 'POST':
        # Get form data and perform validation (improved)
        season_name = request.POST['name']
        time_start = request.POST['time_s']
        time_end = request.POST['time_e']
        profit = request.POST.get('num', 0)  # Get profit, default to 0

        # Validate data (example)
        if not season_name:
            messages.error(request, "Please enter a season name.")
            return render(request, "Manage/m_form.html")

        # Create and save Season
        season = Season.objects.create(
            season_name=season_name,
            time_start=time_start,
            time_end=time_end,
            profit=profit,
            user=request.user  # Assuming User model is linked
        )

        messages.success(request, "Season created successfully!")  # Success message
        return redirect("manage")  # Redirect to manage page

    else:
        return render(request, "Manage/m_form.html")




def infor(request):
    if request.method == 'GET':
        season_id = request.GET.get('id')



def maker(request):
    thitruong_list= thitruong.objects.filter()
    return render(request, 'Manage/maker.html', {'thitruong_list':thitruong_list})

def maker_sell(request):
    if request.method == 'POST':  # Kiểm tra xem request là phương thức POST hay không
            # Lấy dữ liệu người dùng nhập từ form
        ten_caytrong = request.POST.get('ten_caytrong')
        ten_thitruong = request.POST.get('mo_ta')
        gia = request.POST.get('gia')
            
            # Tạo một bản ghi mới trong bảng thitruong_ban
        thitruong_ban_obj = thitruong_ban.objects.create(
                ten_caytrong=ten_caytrong, ten_thitruong=ten_thitruong, gia=gia)
            
            # Lưu lại thông báo thành công
        context = {"message": "Cập nhật thành công!"}
        return render(request, 'Manage/maker_sell.html', context)
    else:
            # Trả về trang contact.html khi request là GET
        return render(request, 'Manage/maker_sell.html')


def contact(request):
    if request.user.is_authenticated:
        if request.method == 'POST':  # Kiểm tra xem request là phương thức POST hay không
            # Lấy dữ liệu người dùng nhập từ form
            hoten = request.POST.get('hoten')
            email = request.POST.get('email')
            loinhan = request.POST.get('loinhan')
            # Tạo một bản ghi mới trong bảng Contact
            lienhe = Contact.objects.create(
                hoten=hoten, email=email, loinhan=loinhan)
            # Lưu lại thông báo thành công
            context = {"message": "Phản hồi của bạn đã được gửi!"}
            return render(request, 'Manage/contact.html', context)
        else:
            # Trả về trang contact.html khi request là GET
            return render(request, 'Manage/contact.html')
    else:
        return HttpResponse("Bạn cần phải đăng nhập để gửi phản hồi")
    



