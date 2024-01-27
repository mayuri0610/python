from django.shortcuts import render,redirect
from .models import *


# Create your views here.

def index(request):
    return render(request, 'index.html')

def country_table(request):
    countryobj = Country_model.objects.all()
    return render(request, 'country_table.html', {'countryobj': countryobj})

def country_add(request):
    if request.method == 'POST':
        country_name=request.POST['country_name']
        position=request.POST['position']
        country_pic=request.FILES['country_pic']
        status=request.POST['status']

        Country_model.objects.create(country_name=country_name, position=position, country_pic=country_pic, status=status)
        return redirect('/country_table')
    
    return render(request, 'country_add.html')

def country_delete(request,id):
    countryobj=Country_model.objects.get(id=id)
    countryobj.delete()
    return redirect('/country_table')

def country_active(request,id):
    countryobj=Country_model.objects.get(id=id)
    countryobj.status= True
    countryobj.save()
    return redirect('/country_table')

def country_deactive(request,id):
    countryobj=Country_model.objects.get(id=id)
    countryobj.status= False
    countryobj.save()
    return redirect('/country_table')

def country_update(request,id):
    countryobj=Country_model.objects.get(id=id)
    if request.method == 'POST':
        country_name=request.POST['country_name']
        position=request.POST['position']
        country_pic=request.FILES.get('country_pic')
        status=request.POST['status']

        countryobj.country_name=country_name
        countryobj.position=position
        countryobj.status=status
        if country_pic:
            countryobj.country_pic=country_pic
        else:
            pass
        countryobj.save()
        return redirect('/country_table')

    return render (request, 'country_update.html',{'countryobj':countryobj})
    

def state_table(request):
    stateobj = State_model.objects.all()
    return render (request, 'state_table.html',{'stateobj': stateobj})


def state_add(request):
    countryobj = Country_model.objects.all()
    if request.method == 'POST':
        state_name=request.POST['state_name']
        position=request.POST['position']
        state_pic=request.FILES['state_pic']
        status=request.POST['status']
        country_id=request.POST['country_name']
        countryobj=Country_model.objects.get(id=country_id)
        State_model.objects.create(position=position, state_name=state_name, state_pic=state_pic,status=status,country=countryobj)
        return redirect('state_table')
    return render (request, 'state_add.html',{'countryobj': countryobj})

def state_active(request,id):
    stateobj=State_model.objects.get(id=id)
    stateobj.status = True
    stateobj.save()
    return redirect('/state_table')

def state_deactive(request,id):
    stateobj=State_model.objects.get(id=id)
    stateobj.status = False
    stateobj.save()
    return redirect('/state_table')

def state_delete(request,id):
    stateobj = State_model.objects.get(id=id)
    stateobj.delete()
    return redirect('/state_table')



def state_update(request,id):
    countryobj = Country_model.objects.all()
    stateobj = State_model.objects.get(id=id)
    if request.method == 'POST':
        state_name=request.POST['state_name']
        position=request.POST['position']
        status=request.POST['status']
        state_pic=request.FILES.get('state_pic')
        country_id=request.POST['country_name']
        countryobj = Country_model.objects.get(id=country_id)

        stateobj.position=position
        stateobj.state_name=state_name
        stateobj.status=status
        if state_pic:
            stateobj.state_pic=state_pic
        else:
            pass
        
        stateobj.country = countryobj
        stateobj.save()
        return redirect('state_table')
    return render (request,'state_update.html', {'stateobj':stateobj, 'countryobj':countryobj})
        

def city_table(request):
    cityobj= City_model.objects.all()
    return render(request,'city_table.html', {'cityobj': cityobj})
            
def city_add(request):
    stateobj= State_model.objects.all()
    if request.method == 'POST':
        city_name=request.POST['city_name']
        state_id=request.POST['state_name']
        position=request.POST['position']
        city_pic=request.FILES.get('city_pic')
        status=request.POST['status']
        stateobj=State_model.objects.get(id=state_id)
        City_model.objects.create(state=stateobj,city_name=city_name,position=position,city_pic=city_pic,status=status)
        return redirect('city_table')

    return render(request,'city_add.html', {'stateobj':stateobj})

def city_active(request,id):
    cityobj=City_model.objects.get(id=id)
    cityobj.status=True
    cityobj.save()
    return redirect('city_table')

def city_deactive(request,id):
    cityobj=City_model.objects.get(id=id)
    cityobj.status=False
    cityobj.save()
    return redirect('city_table')

def city_delete(request,id):
    cityobj=City_model.objects.get(id=id)
    cityobj.delete()
    return redirect('city_table')

def city_update(request,id):
    cityobj = City_model.objects.get(id=id)
    stateobj = State_model.objects.all()
    if request.method == 'POST':
        position= request.POST['position']
        city_name= request.POST['city_name']
        city_pic= request.FILES.get('city_pic')
        status= request.POST['status']
        state_id= request.POST['state_name']
        stateobj = State_model.objects.get(id=state_id)

        cityobj.position=position
        cityobj.city_name=city_name
        cityobj.status=status
        cityobj.state = stateobj

        if city_pic:
            cityobj.city_pic=city_pic
        else:
            pass

        cityobj.save()
        return redirect('city_table')


    return render(request, 'city_update.html', {'cityobj':cityobj,'stateobj':stateobj})


