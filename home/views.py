from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# from dns import message
def home(request):
    records = Record.objects.all()
    return render(request, 'home/index.html', {'records': records})

def mental_state(request):
    return render(request, 'home/mental_state.html')

def depression_issues(request):
    return render(request, 'home/depression_issues.html')

def anxiety_issues(request):
    return render(request, 'home/anxiety_issues.html')

def common_diseases(request):
    return render(request, 'home/common_diseases.html')

def phobias(request):
    return render(request, 'home/phobias.html')

def entities(request):
    return render(request, 'home/entities.html')

def objects(request):
    return render(request, 'home/objects.html')

def situations(request):
    return render(request, 'home/situations.html')

def experts(request):
    return render(request, 'home/experts.html')

def login_user(request):

    # this will grab everything from the record table and copy it here
    # to get all the record cols

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # authenticate
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.success(request, "There was an error TRY AGAIN!")
            return redirect('login')

    else:  # in this case they are not posting any data means not logging in direct going home
        return render(request, 'home/login_user.html')


def logout_user(request):
    logout(request)
    messages.success(request, "Logged out")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate and log in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "you are registered!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'home/register.html', {'form': form})

    return render(request, 'home/register.html', {'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        # to see records
        # to get single the record col
        customer_record = Record.objects.get(id=pk)
        return render(request, 'home/record.html', {'customer_record': customer_record})

    else:
        messages.success(request, "You must be logged in to view that page!")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record deleted successfully!")
        return redirect('home')

    else:
        messages.success(request, "You must be logged in to view that page!")
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added..")
                return redirect('home')
        return render(request, 'home/add_record.html', {"form": form})

    else:
        messages.success(request, "You must be logged in to view that page!")
        return redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been updated!!!!")
            return redirect('home')
        return render(request, 'home/update_record.html', {"form": form})

    else:
        messages.success(request, "You must be logged in to view that page!")
        return redirect('home')