from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout
from .models import *


# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_superuser==True and user.is_staff==True:
                auth.login(request,user)
                return redirect('index')
            else:
                return redirect('')
        else:
            return redirect('/')
    return render(request, 'appadmin/login.html')

										# <input class="form-control" name="email" type="email" placeholder="Email">

def register(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['password1']

        if password==password1:
            if User.objects.filter(username=username).exists():
                print('username allready exist')
                return redirect('/register')
            else:
                User.objects.create_user(username=username,password=password)
                return redirect('/')
        else:
            print('password dose not match')

    return render(request, 'appadmin/register.html')


def logout(request):
    user=request.user
    auth.logout(request)
    return redirect('/')


def index(request):
    return render(request, 'appadmin/index.html')

def doctor_profile(request):
    if request.method == 'POST':

        username=request.POST['username']
        password=request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
    
        user=User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name, 
            last_name=last_name,
            email=email)

        phone_number = request.POST['phone_number']
        dob = request.POST['dob']
        reg_no = request.POST['reg_no']
        gender = request.POST['gender']
        picture = request.FILES.get('picture')
        status = request.POST['status']
        fees = request.POST['fees']
        salary = request.POST['salary']
        about = request.POST['about']
        speciality = request.POST['speciality']
        service = request.POST['service']
        degree = request.POST['degree']
        university = request.POST['university']
        percentage = request.POST['percentage']
        starting_year = request.POST['starting_year']
        completion_year = request.POST['completion_year']
        seat_no = request.POST['seat_no']


        doctorprofile= DoctorProfile.objects.create(
            phone_number=phone_number,
            dob=dob,
            picture=picture,
            reg_no=reg_no,
            gender=gender,
            status=status,
            fees=fees,
            salary=salary,
            about=about,
            speciality=speciality,
            service=service,
            degree=degree, 
            university=university,
            percentage=percentage, 
            starting_year=starting_year,
            completion_year=completion_year,
            seat_no=seat_no,
            user=user ) 
        
        add_line_1 = request.POST['add_line_1']
        add_line_2 = request.POST['add_line_2']
        state = request.POST['state']
        city = request.POST['city']
        country = request.POST['country']
        postal_code = request.POST['postal_code']

        DoctorAddress.objects.create(
            add_line_1=add_line_1, 
            add_line_2=add_line_2 , 
            state=state, city=city, 
            country=country, 
            postal_code=postal_code,
            doctor=doctorprofile)
        
        degree = request.POST['degree']
        university = request.POST['university']
        percentage = request.POST['percentage']
        starting_year = request.POST['starting_year']
        completion_year = request.POST['completion_year']
        seat_no = request.POST['seat_no']
       

        return redirect('doctor_list')  

    return render(request,'appadmin/doctor_profile.html')

def doctor_list(request):
    doctorprofileobj = DoctorProfile.objects.all()
    return render(request,'appadmin/doctor_list.html', {'doctorprofileobj': doctorprofileobj})

def doctor_active(request,id):
    stateobj=DoctorProfile.objects.get(id=id)
    stateobj.status = True
    stateobj.save()
    return redirect('/doctor_list')

def doctor_deactive(request,id):
    stateobj=DoctorProfile.objects.get(id=id)
    stateobj.status = False
    stateobj.save()
    return redirect('/doctor_list')







def profile(request):
    return render(request, 'appadmin/profile.html')

def appointment_list(request):
    return render(request, 'appadmin/appointment_list.html')



def patient_list(request):
    return render(request, 'appadmin/patient_list.html')

def specialities(request):
    return render(request, 'appadmin/specialities.html')










def blank_page(request):
    return render(request, 'appadmin/blank_page.html')

def components(request):
    return render(request, 'appadmin/components.html')

def data_tables(request):
    return render(request, 'appadmin/data_tables.html')

def error_404(request):
    return render(request, 'appadmin/error_404.html')

def error_500(request):
    return render(request, 'appadmin/error_500.html')

def forgot_password(request):
    return render(request, 'appadmin/forgot_password.html')

def form_basic_inputs(request):
    return render(request, 'appadmin/form_basic_inputs.html')

def form_horizontal(request):
    return render(request, 'appadmin/form_horizontal.html')

def form_input_groups(request):
    return render(request, 'appadmin/form_input_groups.html')

def form_mask(request):
    return render(request, 'appadmin/form_mask.html')

def form_validation(request):
    return render(request, 'appadmin/form_validation.html')

def form_vertical(request):
    return render(request, 'appadmin/form_vertical.html')

def invoice_report(request):
    return render(request, 'appadmin/invoice_report.html')

def invoice(request):
    return render(request, 'appadmin/invoice.html')

def lock_screen(request):
    return render(request, 'appadmin/lock_screen.html')

def reviews(request):
    return render(request, 'appadmin/reviews.html')

def settings(request):
    return render(request, 'appadmin/settings.html')


def tables_basic(request):
    return render(request, 'appadmin/tables_basic.html')

def transactions_list(request):
    return render(request, 'appadmin/transactions_list.html')




# {% extends "appadmin/base.html" %}
# {% load static %}
# {% block content %}

# {% endblock %}


# {% for i in doctorprofileobj %}
# 									<tr>
# 										<td>
# 											<h2 class="table-avatar">
# 												<a href="{% url 'profile' %}" class="avatar avatar-sm mr-2"><img
# 														class="avatar-img rounded-circle"
# 														src="{% static 'assets/img/doctors/doctor-thumb-01.jpg' %}"
# 														alt="User Image"></a>
# 												<a href="{% url 'profile' %}">{{i.user.first_name}}&nbsp;{{i.user.last_name}}</a> 
											
# 											</h2>
# 										</td>
# 										<td>{{i.doctor.speciality}}</td>

# 										<td>{{i.about}}<br><small>{{i.fees}}</small></td>

# 										<td>{{i.salary}}</td>

# 										<td>
# 											{% if i.status%}
# 												<a href="{% url 'doctor_deactive' i.id %}"><button>Active</button></a>    
# 											{% else %}               
# 												<a href="{% url 'doctor_active' i.id %}"><button>Deactive</button></a>    
# 											{% endif %}
# 										</td>
# 									</tr>
# 									{% endfor %}
