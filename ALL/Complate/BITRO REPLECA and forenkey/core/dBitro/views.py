from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *
# Create your views here.
def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/index')
        else:
            return redirect('/')
   
    return render(request,'sign_in.html')
    
def sign_up(request):
      if request.method=="POST":
        first_name=request.POST['name']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                print('username allready exist')
                return redirect('/sign_up')
            else:
                User.objects.create_user(first_name=first_name,username=username,password=password)
                return redirect('/')     
        else:
            print('password not match')
            return redirect('/sign_up')
      return render(request,'sign_up.html')


def index(request):
    return render(request,'index.html')

def location(request):
    return render(request,'location.html')

def country_table(request):
    data=Country_master.objects.all()
    return render(request,'country_table.html',{'data':data})

def add_country(request):
    if request.method=="POST":
        position=request.POST['position']
        country_name=request.POST['country_name']
        is_active=request.POST['is_active']
        country_master=Country_master(position=position,country_name=country_name,is_active=is_active)
        country_master.save()
        return redirect('/country_table')
    return render(request,'add_country.html')


def DeactiveCountry(request, id):
    country_master=Country_master.objects.get(id=id)
    country_master.is_active=False
    country_master.save()
    return redirect('/country_table')

def ActiveCountry(request, id):
    country_master=Country_master.objects.get(id=id)
    country_master.is_active=True
    country_master.save()
    return redirect('/country_table')

def country_delete(request, id):
    country_master=Country_master.objects.get(id=id)
    country_master.delete()
    return redirect('/country_table')

def country_update(request,id): 
    country_master=Country_master.objects.get(id=id)
    if request.method=="POST":
        position=request.POST['position']
        country_name=request.POST['country_name']
        is_active=request.POST['is_active']
        country_master.position=position
        country_master.country_name=country_name
        country_master.is_active=is_active
        country_master.save()
        return redirect('/country_table')
    return render(request,'country_update.html',{'country_master':country_master})

def state_table(request):
    data=State_master.objects.all()
    return render(request,'state_table.html',{'data':data})

def add_state(request):
    countryobj=Country_master.objects.all()
    if request.method=="POST":
        position=request.POST['position']
        state_name=request.POST['state_name']
        is_active=request.POST['is_active']

        country_id=request.POST['country_name']
        countryobj=Country_master.objects.get(id=country_id)

        state_master=State_master(position=position,state_name=state_name,is_active=is_active,country=countryobj)
        state_master.save()
        return redirect('/state_table')
    return render(request,'add_state.html',{'countryobj':countryobj})

def state_delete(request,id):
    state_master=State_master.objects.get(id=id)
    state_master.delete()
    return redirect('/state_table')

def state_update(request,id):
    state_master=State_master.objects.get(id=id)
    country=Country_master.objects.all()
    if request.method=="POST":
        position=request.POST['position']
        state_name=request.POST['state_name']
        is_active=request.POST['is_active']

        country_id=request.POST['country_name']
        contryobj=Country_master.objects.get(id=country_id)

        state_master.position=position
        state_master.state_name=state_name
        state_master.is_active=is_active
        state_master.country=contryobj
        state_master.save()
        return redirect('/state_table')
    return render(request,'state_update.html',{'state_master':state_master})


def DeactiveState(request,id):
    state_master=State_master.objects.all()
    state_master.is_active=False
    state_master.save()
    return redirect('/state_table')

def ActiveState(request,id):
    state_master=State_master.objects.all()
    state_master.is_active=True
    state_master.save()
    return redirect('/state_table')





def education_table(request):
    data=Education_master.objects.all()
    return render(request,'education_table.html',{'data':data})

def add_education(request):
    if request.method=="POST":
        position=request.POST['position']
        education_name=request.POST['education_name']
        is_active=request.POST['is_active']
        education_master=Education_master(position=position,education_name=education_name,is_active=is_active)
        education_master.save()
        return redirect('/education_table')
    return render(request,'add_education.html')

def education_delete(request,id):
    education_master=Education_master.objects.get(id=id)
    education_master.delete()
    return redirect('/education_table')

def education_update(request,id):
    education_master=Education_master.objects.get(id=id)
    if request.method=="POST":
        position=request.POST['position']
        education_name=request.POST['education_name']
        is_active=request.POST['is_active']

        education_master.position=position
        education_master.education_name=education_name
        education_master.is_active=is_active
        education_master.save()
        return redirect('/education_table')
    return render(request,'education_update.html',{'education_master':education_master})


def ActiveEducation(request,id):
    education_master=Education_master.objects.get(id=id)
    education_master.is_active=True
    education_master.save()
    return redirect('/education_table')

def DeactiveEducation(reuest,id):
    education_master=Education_master.objects.get(id=id)
    education_master.is_active=False
    education_master.save()
    return redirect('/education_table')
        

def gender_table(request):
    data=Gender_master.objects.all()
    return render(request,'gender_table.html',{'data':data})

def add_gender(request):
    if request.method=="POST":
        position=request.POST['position']
        gender_name=request.POST['gender_name']
        is_active=request.POST['is_active']
        gender_master=Gender_master(position=position,gender_name=gender_name,is_active=is_active)
        gender_master.save()
        return redirect('/gender_table')
    return render(request,'add_gender.html')

def gender_delete(request,id):  
    gender_master=Gender_master.objects.get(id=id)
    gender_master.delete()
    return redirect('/gender_table')

def gender_update(request,id):
    gender_master=Gender_master.objects.get(id=id)
    if request.method=="POST":
        position=request.POST['position']
        gender_name=request.POST['gender_name']
        is_active=request.POST['is_active']
        gender_master.position=position
        gender_master.gender_name=gender_name
        gender_master.is_active=is_active
        gender_master.save()
        return redirect('/gender_table')
    return render(request,'gender_update.html',{'gender_master':gender_master})

def ActiveGender(request,id):
    education_master=Education_master.objects.get(id=id)
    education_master.is_active=True
    education_master.save()
    return redirect('/gender_table')

def DeactiveGender(reuest,id):
    education_master=Education_master.objects.get(id=id)
    education_master.is_active=False
    education_master.save()
    return redirect('/gender_table')

def icebreak_table(request):
    data=Icebreak_master.objects.all()
    return render(request,'icebreak_table.html',{'data':data})

def add_icebreak(request):
    if request.method=="POST":
        position=request.POST['position']
        icebreak_name=request.POST['icebreak_name']
        is_active=request.POST['is_active']
        icebreak_master=Icebreak_master(position=position,icebreak_name=icebreak_name,is_active=is_active)
        icebreak_master.save()
        return redirect('/icebreak_table')
    return render(request,'add_icebreak.html')

def icebreak_delete(request,id):
    icebreak_master=Icebreak_master.objects.get(id=id)
    icebreak_master.delete()
    return redirect('/icebreak_table')

def icebreak_update(request,id):
    icebreak_master=Icebreak_master.objects.get(id=id)
    if request.method=="POST":
        position=request.POST['position']
        icebreak_name=request.POST['icebreak_name']
        is_active=request.POST['is_active']
        icebreak_master.position=position
        icebreak_master.icebreak_name=icebreak_name
        icebreak_master.is_active=is_active
        icebreak_master.save()
        return redirect('/icebreak_table')
    return render(request,'icebreak_update.html',{'icebreak_master':icebreak_master})

def ActiveIcebreak(request,id):
    icebreak_master=Icebreak_master.objects.get(id=id)
    icebreak_master.is_active=True
    icebreak_master.save()
    return redirect('/icebreak_table')

def DeactiveIcebreak(reuest,id):
    icebreak_master=Icebreak_master.objects.get(id=id)
    icebreak_master.is_active=False
    icebreak_master.save()
    return redirect('/icebreak_table')


def  interest_table(request):
    data=Interest_master.objects.all()
    return render(request,'interest_table.html',{'data':data})

def add_interest(request):
    if request.method=="POST":
        position=request.POST['position']
        interest_name=request.POST['interest_name']
        is_active=request.POST['is_active']
        blue_pic=request.FILES['blue_pic']
        grey_pic=request.FILES['grey_pic']
        Interest_master.objects.create(position=position,interest_name=interest_name,is_active=is_active,blue_pic=blue_pic,grey_pic=grey_pic)
        return redirect('/interest_table')
    return render(request,'add_interest.html')

def interest_delete(request,id):
    interest_master=Interest_master.objects.get(id=id)
    interest_master.delete()
    return redirect('/interest_table')

def interest_update(request,id):
    interest_master=Interest_master.objects.get(id=id)
    if request.method=="POST":
        position=request.POST['position']
        interest_name=request.POST['interest_name']
        is_active=request.POST['is_active']

        blue_pic=request.FILES.get('blue_pic')
        if blue_pic:
            interest_master.blue_pic=blue_pic
        else:
            pass

        grey_pic=request.FILES.get('grey_pic')
        if grey_pic:
            interest_master.grey_pic=grey_pic
        else:
            pass


        interest_master.position=position
        interest_master.interest_name=interest_name
        interest_master.is_active=is_active
        interest_master.save()
        return redirect('/interest_table')
    return render(request,'interest_update.html',{'interest_master':interest_master})

def ActiveInterest(request,id):
    interest_master=Interest_master.objects.get(id=id)
    interest_master.is_active=True
    interest_master.save()
    return redirect('/interest_table')

def DeactiveInterest(reuest,id):
    interest_master=Interest_master.objects.get(id=id)
    interest_master.is_active=False
    interest_master.save()
    return redirect('/interest_table')

def pets_table(request):
    data=Pets_master.objects.all()
    return render(request,'pets_table.html',{'data':data})

def add_pets(request):
    if request.method=="POST":
        position=request.POST['position']
        pets_name=request.POST['pets_name']
        is_active=request.POST['is_active']
        blue_pic=request.FILES['blue_pic']
        grey_pic=request.FILES['grey_pic']
        pets_master=Pets_master(position=position,pets_name=pets_name,is_active=is_active,blue_pic=blue_pic,grey_pic=grey_pic)
        pets_master.save()
        return redirect('/pets_table')
    return render(request,'add_pets.html')

def pets_delete(request,id):
    pets_master=Pets_master.objects.get(id=id)
    pets_master.delete()
    return redirect('/pets_table')

def pets_update(request,id):
    pets_master=Pets_master.objects.get(id=id)
    if request.method=="POST":
        position=request.POST['position']
        pets_name=request.POST['pets_name']
        is_active=request.POST['is_active']

        blue_pic=request.FILES.get('blue_pic')
        if blue_pic:
            pets_master.blue_pic=blue_pic
        else:
            pass

        grey_pic=request.FILES.get('grey_pic')
        if grey_pic:
            pets_master.grey_pic=grey_pic
        else:
            pass

        pets_master.position=position
        pets_master.pets_name=pets_name
        pets_master.is_active=is_active
        pets_master.save()
        return redirect('/pets_table')
    return render(request,'pets_update.html',{'pets_master':pets_master})

def ActivePets(request,id):
    pets_master=Pets_master.objects.get(id=id)
    pets_master.is_active=True
    pets_master.save()
    return redirect('/pets_table')

def DeactivePets(reuest,id):
    pets_master=Pets_master.objects.get(id=id)
    pets_master.is_active=False
    pets_master.save()
    return redirect('/pets_table')

def political_table(request):
    data=Political_master.objects.all()
    return render(request,'political_table.html',{'data':data})

def add_political(request):
    if request.method=="POST":
        position=request.POST['position']
        political_name=request.POST['political_name']
        is_active=request.POST['is_active']
        political_master=Political_master(position=position,political_name=political_name,is_active=is_active)
        political_master.save()
        return redirect('/political_table')
    return render(request,'add_political.html')

def political_delete(request,id):
    political_master=Political_master.objects.get(id=id)
    political_master.delete()
    return redirect('/political_table')

def political_update(request,id):
    political_master=Political_master.objects.get(id=id)
    if request.method=="POST":
        position=request.POST['position']
        political_name=request.POST['political_name']
        is_active=request.POST['is_active']
        political_master.position=position
        political_master.political_name=political_name
        political_master.is_active=is_active
        political_master.save()
        return redirect('/political_table')
    return render(request,'political_update.html',{'political_master':political_master})

def ActivePolitical(request,id):
    political_master=Political_master.objects.get(id=id)
    political_master.is_active=True
    political_master.save()
    return redirect('/political_table')

def DeactivePolitical(reuest,id):
    political_master=Political_master.objects.get(id=id)
    political_master.is_active=False
    political_master.save()
    return redirect('/political_table')


def prompts_table(request):
    data=Prompts_master.objects.all()
    return render(request,'prompts_table.html',{'data':data})

def add_prompts(request):
    if request.method=="POST":
        position=request.POST['position']
        prompts_name=request.POST['prompts_name']
        is_active=request.POST['is_active']
        prompts_master=Prompts_master(position=position,prompts_name=prompts_name,is_active=is_active)
        prompts_master.save()
        return redirect('/prompts_table')
    return render(request,'add_prompts.html')

def prompts_delete(request,id):
    prompts_master=Prompts_master.objects.get(id=id)
    prompts_master.delete()
    return redirect('/prompts_table')

def prompts_update(request,id):
    prompts_master=Prompts_master.objects.get(id=id)
    if request.method=="POST":
        position=request.POST['position']
        prompts_name=request.POST['prompts_name']
        is_active=request.POST['is_active']
        prompts_master.position=position
        prompts_master.prompts_name=prompts_name
        prompts_master.is_active=is_active
        prompts_master.save()
        return redirect('/prompts_table')
    return render(request,'prompts_update.html',{'prompts_master':prompts_master})

def ActivePrompts(request,id):
    prompts_master=Prompts_master.objects.get(id=id)
    prompts_master.is_active=True
    prompts_master.save()
    return redirect('/prompts_table')

def DeactivePrompts(reuest,id):
    prompts_master=Prompts_master.objects.get(id=id)
    prompts_master.is_active=False
    prompts_master.save()
    return redirect('/prompts_table')


def language_table(request):
    data=language_master.objects.all()
    return render(request,'language_table.html',{'data':data})

def add_language(request):
    if request.method=="POST":
        position=request.POST['position']
        language_name=request.POST['language_name']
        is_active=request.POST['is_active']
        lang=language_master(position=position,language_name=language_name,is_active=is_active)
        lang.save()
        return redirect('/language_table')
    return render(request,'add_language.html')

def language_delete(request,id):
    lang=language_master.objects.get(id=id)
    lang.delete()
    return redirect('/language_table')

def language_update(request,id):
    lang=language_master.objects.get(id=id)
    if request.method=="POST":
        position=request.POST['position']
        language_name=request.POST['language_name']
        is_active=request.POST['is_active']
        lang.position=position
        lang.language_name=language_name
        lang.is_active=is_active
        lang.save()
        return redirect('/language_table')
    return render(request,'language_update.html',{'lang':lang})

def ActiveLanguage(request,id):
    lang=language_master.objects.get(id=id)
    lang.is_active=True
    lang.save()
    return redirect('/language_table')

def DeactiveLanguage(reuest,id):
    lang=language_master.objects.get(id=id)
    lang.is_active=False
    lang.save()
    return redirect('/language_table')


def city_table(request):
    data=City_master.objects.all()
    stateobj=State_master.objects.all()
    return render(request,'city_table.html',{'data':data,'stateobj':stateobj})

def add_city(request):
    if request.method=="POST":
        position=request.POST['position']
        city_name=request.POST['city_name']
        is_active=request.POST['is_active']

        state_id=request.POST['state_name']
        stateobj=State_master.objects.get(id=state_id)

        city=City_master(position=position,city_name=city_name,is_active=is_active,state=stateobj)
        city.save()
        return redirect('/city_table')
    return render(request,'add_city.html')

def city_delete(request,id):
    city=City_master.objects.get(id=id)
    city.delete()
    return redirect('/city_table')

def city_update(request,id):
    city=City_master.objects.get(id=id)
    stateobj=State_master.objects.all()
    if request.method=="POST":
        position=request.POST['position']
        city_name=request.POST['city_name']
        is_active=request.POST['is_active']
        state_id=request.POST['state_name']
        stateobj=State_master.objects.get(id=state_id)
        city.position=position
        city.city_name=city_name
        city.is_active=is_active
        city.state=stateobj
        city.save()
        return redirect('/city_table')
    return render(request, 'city_update.html',{'city':city,'state':stateobj})

def ActiveCity(request,id):
    city=City_master.objects.get(id=id)
    city.is_active=True
    city.save()
    return redirect('/city_table')

def DeactiveCity(reuest,id):
    city=City_master.objects.get(id=id)
    city.is_active=False
    city.save()
    return redirect('/city_table')


     



 



 





    
   