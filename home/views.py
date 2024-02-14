from email.message import EmailMessage
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from minddoc.settings import EMAIL_HOST_USER
from .forms import  EventForm, SignUpForm, AddRecordForm, EventFormAdmin, GbcForm
from .models import QuizSubmissions, Record, Event, Venue, Appointments, Goalbasedcare, Goalbasedcare2, Goalbasedcare3
from django.contrib.auth.decorators import login_required
#import user model from django
from django.contrib.auth.models import User
from django.db.models import Count
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .forms import VenueForm, EventForm
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.paginator import Paginator
from django.template import Context
from django.template.loader import render_to_string, get_template
import datetime
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        email = request.POST.get('footer-email')
        mail=EmailMessage("Newsletter from MindDoc!!!!!!", "Thankyou for visiting MindDoc", settings.EMAIL_HOST_USER, [email])
        file_path = "Newsletter from MindDoc.pdf"
        with open(file_path, "rb") as file:
            mail.attach("Newsletter from MindDoc.pdf", file.read(), 'application/pdf')
        mail.send()
        messages.success(request, "Your newsletter is waiting in your gmail.")
        return redirect('home')
        
    return render(request, 'home/index.html', {'records': records})

@login_required
def goal_based_care_premium(request):
    gbc = Goalbasedcare.objects.all()
    # set up pagination
    p= Paginator(Goalbasedcare.objects.all(), 1)
    page=request.GET.get('page')
    gbc=p.get_page(page)
    nums="a"*gbc.paginator.num_pages

    if request.method == 'POST':
        gbc = Goalbasedcare.objects.all()
        task_number = request.POST.get('task_number')
        # Assuming task_number is unique and fetching one specific task
        task = Goalbasedcare.objects.get(task_number=task_number)
        task.finished = True  # Marking the task as finished
        task.save()  # Save the changes
        messages.success(request, f"You Completed the Task for Day {task_number}.")
        return redirect('goal_based_care_premium')
    
    return render(request, 'gbc/goal_based_care_premium.html', {"gbc": gbc, "nums":nums})

@login_required
def goal_based_care_premium_level2(request):
    gbc = Goalbasedcare2.objects.all()
    # set up pagination
    p= Paginator(Goalbasedcare2.objects.all(), 1)
    page=request.GET.get('page')
    gbc=p.get_page(page)
    nums="a"*gbc.paginator.num_pages

    if request.method == 'POST':
        gbc = Goalbasedcare2.objects.all()
        task_number = request.POST.get('task_number')
        # Assuming task_number is unique and fetching one specific task
        task = Goalbasedcare2.objects.get(task_number=task_number)
        task.finished = True  # Marking the task as finished
        task.save()  # Save the changes
        messages.success(request, f"You Completed the Task for Day {task_number}.")
        return redirect('goal_based_care_premium')
    
    return render(request, 'gbc/goal_based_care_premium_level2.html', {"gbc": gbc, "nums":nums})

@login_required
def goal_based_care_premium_level3(request):
    gbc = Goalbasedcare3.objects.all()
    # set up pagination
    p= Paginator(Goalbasedcare3.objects.all(), 1)
    page=request.GET.get('page')
    gbc=p.get_page(page)
    nums="a"*gbc.paginator.num_pages

    if request.method == 'POST':
        gbc = Goalbasedcare3.objects.all()
        task_number = request.POST.get('task_number')
        # Assuming task_number is unique and fetching one specific task
        task = Goalbasedcare3.objects.get(task_number=task_number)
        task.finished = True  # Marking the task as finished
        task.save()  # Save the changes
        messages.success(request, f"You Completed the Task for Day {task_number}.")
        return redirect('goal_based_care_premium')
    
    return render(request, 'gbc/goal_based_care_premium_level3.html', {"gbc": gbc, "nums":nums})
Goalbasedcare
def report(request):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to access this page.")
        return redirect(reverse('login'))  # Assuming your login URL is named 'login'
    
    return render(request, 'gbc/report.html')

@staff_member_required 
def update_gbc(request, gbc_id):
    goal = get_object_or_404(Goalbasedcare, pk=gbc_id)
    form = GbcForm(request.POST or None, instance=goal)
    if form.is_valid():
        form.save()
        messages.success(request, "Task Updated Successfully")
        return redirect('goal_based_care_premium')
    
    return render(request, 'gbc/update_gbc.html', {'goal':goal, 'form':form})




@login_required
def experts_premium(request):
    if request.method == 'POST':
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        mobile = request.POST.get("mob")
        message = request.POST.get("request")
        appointment = Appointments.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            phone=mobile,
            request=message,
        )
        appointment.save()
        messages.add_message(request, messages.SUCCESS, f"Thanks {fname} for making an appointment, we will email you ASAP!")
        return HttpResponseRedirect(request.path)
    
    return render(request, 'experts/experts_premium.html')

@staff_member_required 
def manage_appointments(request):
    appointments = Appointments.objects.all().order_by('sent_date')
    paginator = Paginator(appointments, 3)  # Change the second argument to the number of items per page you want
    page_number = request.GET.get('page')
    appointments_p = paginator.get_page(page_number)

    if request.method == 'POST':
        date = request.POST.get("date")
        time = request.POST.get("time")  # Retrieve time from the form data
        appointment_id = request.POST.get("appointment_id")
        appointment = Appointments.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.datetime.now()
        # Combine date and time strings into a single datetime object
        appointment.accepted_datetime = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        appointment.save()

        data = {
            "fname": appointment.first_name,
            "date": date,
            'time':time,
        }

        message = get_template('experts/email.html').render(data)
        email = EmailMessage(
            "About your appointment",
            message,
            settings.EMAIL_HOST_USER,
            [appointment.email],
        )
        email.content_subtype = "html"
        email.send()

        messages.add_message(request, messages.SUCCESS, f"You accepted the appointment of {appointment.first_name}")
        return HttpResponseRedirect(request.path)

    return render(request, "experts/manage_appointment.html", {'appointments_p':appointments_p})

@login_required
def experts_premium2(request):
    if request.method == 'POST':
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        mobile = request.POST.get("mob")
        message = request.POST.get("request")
        appointment = Appointments.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            phone=mobile,
            request=message,
        )
        appointment.save()
        messages.add_message(request, messages.SUCCESS, f"Thanks {fname} for making an appointment, we will email you ASAP!")
        return HttpResponseRedirect(request.path)
    
    return render(request, 'experts/experts_premium2.html')

@staff_member_required 
def manage_appointments2(request):
    appointments = Appointments.objects.all().order_by('sent_date')
    paginator = Paginator(appointments, 3)  # Change the second argument to the number of items per page you want
    page_number = request.GET.get('page')
    appointments_p = paginator.get_page(page_number)

    if request.method == 'POST':
        date = request.POST.get("date")
        time = request.POST.get("time")  # Retrieve time from the form data
        appointment_id = request.POST.get("appointment_id")
        appointment = Appointments.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.datetime.now()
        # Combine date and time strings into a single datetime object
        appointment.accepted_datetime = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        appointment.save()

        data = {
            "fname": appointment.first_name,
            "date": date,
            'time':time,
        }

        message = get_template('experts/email2.html').render(data)
        email = EmailMessage(
            "About your appointment",
            message,
            settings.EMAIL_HOST_USER,
            [appointment.email],
        )
        email.content_subtype = "html"
        email.send()

        messages.add_message(request, messages.SUCCESS, f"You accepted the appointment of {appointment.first_name}")
        return HttpResponseRedirect(request.path)

    return render(request, "experts/manage_appointment2.html", {'appointments_p':appointments_p})

def events(request, year=datetime.datetime.now().year, month=datetime.datetime.now().strftime('%B')):
    month=month.capitalize()
    month_number=list(calendar.month_name).index(month)
    month_number=int(month_number)
    cal= HTMLCalendar().formatmonth(year, month_number)

    now=datetime.datetime.now()
    current_year=now.year
    #query the events model for dates
    event_list=Event.objects.filter(
        event_date__year=year,
        event_date__month=month_number
    )
    time=now.time()
    return render(request, 'event/events.html',{ "year":year, "month":month, "month_number":month_number, "cal":cal, "current_year":current_year, "time":time,"event_list":event_list})

def events_list(request):
    events_list=Event.objects.all().order_by('-event_date')
    return render(request, 'event/events_list.html', {'events_list':events_list})

@staff_member_required    
def add_venue(request):
    submitted=False
    if request.method == "POST":
        form = VenueForm(request.POST, request.FILES)
        if form.is_valid():
            venue=form.save(commit=False)
            venue.owner=request.user.id
            venue.save()
            # form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form=VenueForm
        if 'submitted' in request.GET:
            submitted=True

    return render(request, 'event/add_venue.html', {'form':form, 'submitted':submitted})

def list_venue(request):
    # venue_list=Venue.objects.all().order_by('name')
    venue_list=Venue.objects.all().order_by('name')

    # set up pagination
    p= Paginator(Venue.objects.all(), 3)
    page=request.GET.get('page')
    venues=p.get_page(page)
    nums="a"*venues.paginator.num_pages
    return render(request, 'event/venue.html', {'venue_list':venue_list, 'venues':venues, 'nums':nums})

def venue_events(request, venue_id):
    #grab the venue
    venue=Venue.objects.get(id=venue_id)
    #grab the events from that venue
    events=venue.event_set.all()
    return render(request,'event/venue_events.html',{'events':events, 'venue':venue})
    
def show_event(request, event_id):
    event= Event.objects.get(pk=event_id)
    return render(request,'event/show_event.html',{'event':event})

def show_venue(request, venue_id):
    venue= Venue.objects.get(pk=venue_id)
    return render(request, 'event/show_venue.html', {'venue':venue})

def search_venues(request):
    if request.method=="POST":
        searched = request.POST['searched']
        venues=Venue.objects.filter(name__contains=searched)
        return render(request, 'event/search_venues.html',{'searched':searched, 'venues':venues})
    else:
        return render(request, 'event/search_venues.html')

def venue_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=venues.txt'

    venues=Venue.objects.all()
    lines=[]
    for venue in venues:
        lines.append(f'-{venue.name}\n{venue.address}\n{venue.phone}\n{venue.zip_code}\n{venue.phone}\n{venue.web}\n{venue.email_address}\n\n\n')
    # write to text file
    response.writelines(lines)
    return response

@staff_member_required    
def add_event(request):
    submitted=False
    if request.method == "POST":
        if request.user.is_superuser:
            form = EventFormAdmin(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/add_event?submitted=True')
        else:
            form=EventForm(request.POST)

            if form.is_valid():
                # form.save()
                event=form.save(commit=False)
                event.manager=request.user
                event.save()
                return HttpResponseRedirect('/add_event?submitted=True')
    else:
        #just going to the page not submitting
        if request.user.is_superuser:
            form=EventFormAdmin
        else:
            form=EventForm
        if 'submitted' in request.GET:
            submitted=True

    return render(request, 'event/add_event.html', {'form':form, 'submitted':submitted})

@staff_member_required
def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.user.is_superuser:
        form = EventFormAdmin(request.POST or None, instance=event)
    else:
        form = EventForm(request.POST or None, instance=event)

    if form.is_valid():
        form.save()
        messages.success(request, "Event Updated successfully!")
        return redirect('events_list')
    
    return render(request, 'event/update_event.html', {'event':event, 'form':form})

@login_required
def delete_event(request, event_id):
        event = Event.objects.get(pk=event_id)
        if request.user==event.manager:
            event.delete()
            messages.success(request, "Event deleted successfully!")
            return redirect('events_list')
        else:
            messages.success(request, "You are not authorized to delete this event.")
            return redirect('events_list')

@login_required
def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('list_venue')
    
    return render(request, 'event/update_venue.html', {'venue':venue, 'form':form})
    
def my_events(request):
    if request.user.is_authenticated:
        me=request.user.id
        events=Event.objects.filter(attendees=me)
        return render(request, 'event/my_events.html', {"events":events})
    else:
        messages.success(request, "You are not authorized to view this page.")
        return redirect('home')

def mental_state(request):
    return render(request, 'home/mental_state.html')

def generalized_anxiety_disorder(request):
    return render(request, 'home/generalized_anxiety_disorder.html')

def social_anxiety_disorder(request):
    return render(request, 'home/social_anxiety_disorder.html')

def separation_anxiety_disorder(request):
    return render(request, 'home/separation_anxiety_disorder.html')

def psychotic_depression(request):
    return render(request, 'home/psychotic_depression.html')

def major_depressive_depression(request):
    return render(request, 'home/major_depressive_depression.html')

def situational_depression(request):
    return render(request, 'home/situational_depression.html')

def post_traumatic_stress_disorder(request):
    return render(request, 'home/post_traumatic_stress_disorder.html')

def obsessive_compulsive_disorder(request):
    return render(request, 'home/obsessive_compulsive_disorder.html')

def dissociative_identity_disorder(request):
    return render(request, 'home/dissociative_identity_disorder.html')

def phobias(request):
    return render(request, 'home/phobias.html')

def subjects(request):
    return render(request, 'home/subjects.html')

def anthrophobia(request):
    return render(request, 'phobias/anthrophobia.html')
def zoophobia(request):
    return render(request, 'phobias/zoophobia.html')
def coulrophobia(request):
    return render(request, 'phobias/coulrophobia.html')
def genophobia(request):
    return render(request, 'phobias/genophobia.html')
def cacophobia(request):
    return render(request, 'phobias/cacophobia.html')
def automatonophobia(request):
    return render(request, 'phobias/automatonophobia.html')
def ombrophobia(request):
    return render(request, 'phobias/ombrophobia.html')
def kosmikophobia(request):
    return render(request, 'phobias/kosmikophobia.html')
def archnophobia(request):
    return render(request, 'phobias/archnophobia.html')
def ophidiophobia(request):
    return render(request, 'phobias/ophidiophobia.html')
def entomophobia(request):
    return render(request, 'phobias/entomophobia.html')
def hylophobia(request):
    return render(request, 'phobias/hylophobia.html')

def objects(request):
    return render(request, 'home/objects.html')
def noscomephobia(request):
    return render(request, 'phobias/noscomephobia.html')
def hemophobia(request):
    return render(request, 'phobias/hemophobia.html')
def photophobia(request):
    return render(request, 'phobias/photophobia.html')
def trypophobia(request):
    return render(request, 'phobias/trypophobia.html')
def aichmophobia(request):
    return render(request, 'phobias/aichmophobia.html')
def nomophobia(request):
    return render(request, 'phobias/nomophobia.html')
def pyrophobia(request):
    return render(request, 'phobias/pyrophobia.html')
def acidophobia(request):
    return render(request, 'phobias/acidophobia.html')
def kinemortophobia(request):
    return render(request, 'phobias/kinemortophobia.html')
def pediophobia(request):
    return render(request, 'phobias/pediophobia.html')
def eisoptrophobia(request):
    return render(request, 'phobias/eisoptrophobia.html')
def chronomentophobia(request):
    return render(request, 'phobias/chronomentophobia.html')

def situations(request):
    return render(request, 'home/situations.html')
def acrophobia(request):
    return render(request, 'phobias/acrophobia.html')
def claustrophobia(request):
    return render(request, 'phobias/claustrophobia.html')
def aquaphobia(request):
    return render(request, 'phobias/aquaphobia.html')
def glossophobia(request):
    return render(request, 'phobias/glossophobia.html')
def monophobia(request):
    return render(request, 'phobias/monophobia.html')
def nyctophobia(request):
    return render(request, 'phobias/nyctophobia.html')
def astraphobia(request):
    return render(request, 'phobias/astraphobia.html')
def agoraphobia(request):
    return render(request, 'phobias/agoraphobia.html')
def taphophobia(request):
    return render(request, 'phobias/taphophobia.html')
def rhabdophobia(request):
    return render(request, 'phobias/rhabdophobia.html')
def fomo(request):
    return render(request, 'phobias/fomo.html')


def experts(request):
    return render(request, 'home/experts.html')

def premium(request):
    return render(request, 'home/premium.html')

def forgotpassword(request):
    return render(request, 'home/forgotpassword.html')

def goal_based_care(request):
    return render(request, 'home/goal_based_care.html')

def quiz(request):
    if request.method == 'POST':
        submission = QuizSubmissions(
            feeling_overwhelmed=request.POST['feeling_overwhelmed'],
            being_judged=request.POST['being_judged'],
            sleep_patterns=request.POST['sleep_patterns'],
            confront_challenges=request.POST['confront_challenges'],
            comfortable_enclosed_spaces=request.POST['comfortable_enclosed_spaces'],
            public_speaking_anxiety=request.POST['public_speaking_anxiety'],
            anxiety_in_crowded_places=request.POST['anxiety_in_crowded_places'],
            fear_of_missing_out=request.POST['fear_of_missing_out'],
            panic_or_fear=request.POST['panic_or_fear'],
            are_you_satisfied_with_work_life=request.POST['are_you_generally_satisfied_with_your_work_life_balanced'],
            difficulty_concentrating=request.POST['difficulty_concentrating'],
            overthinking_decisions=request.POST['overthinking_decisions'],
        )
        submission.save()
        return redirect('quiz_results')

    return render(request, 'home/quiz.html')

def calculate_mental_health(feeling_overwhelmed, being_judged, sleep_patterns, confront_challenges, comfortable_enclosed_spaces, public_speaking_anxiety, anxiety_in_crowded_places, fear_of_missing_out, panic_or_fear, are_you_satisfied_with_work_life, difficulty_concentrating, overthinking_decisions):
    # Example scoring system, you can customize it based on your criteria
    score = 0

    if feeling_overwhelmed == 'Frequently':
        score += 3
    elif feeling_overwhelmed == 'Sometimes':
        score += 2
    elif feeling_overwhelmed == 'Rarely':
        score += 1

    # Scoring for 'being_judged'
    elif being_judged == 'Yes':
        score += 2
    elif being_judged == 'No':
        score += 1

    # Scoring for 'sleep_patterns'
    elif sleep_patterns == 'Poor':
        score += 3
    elif sleep_patterns == 'Average':
        score += 2
    elif sleep_patterns == 'Good':
        score += 1

    # Add similar scoring logic for other questions...

    # Define your mental health categories based on the total score
    if score > 6:
        return 'Possible generalized anxiety and it could be cured with accurate precautions and control of sentiments'
    elif 8 < score < 10:
        return 'Moderately Stressed'
    elif 10 <= score <= 12:
        return 'Might be social anxiety'
    elif 4<score<=5:
        return "Possible generalized anxiety"
    elif score<=3:
        return "Maybe few symptoms of social generalized anxiety"
    else:
        return 'Not Stressed'


def quiz_results(request):
    if request.method == 'POST' or request.method == 'GET':
        # Retrieve the latest submission
        latest_submission = QuizSubmissions.objects.latest('id')

        # Pass individual quiz responses as arguments
        mental_health_condition = calculate_mental_health(
            latest_submission.feeling_overwhelmed,
            latest_submission.being_judged,
            latest_submission.sleep_patterns,
            latest_submission.confront_challenges,
            latest_submission.comfortable_enclosed_spaces,
            latest_submission.public_speaking_anxiety,
            latest_submission.anxiety_in_crowded_places,
            latest_submission.fear_of_missing_out,
            latest_submission.panic_or_fear,
            latest_submission.are_you_satisfied_with_work_life,
            latest_submission.difficulty_concentrating,
            latest_submission.overthinking_decisions,
        )

        return render(request, 'home/quiz_results.html', {'mental_health_condition': mental_health_condition})

    return render(request, 'home/quiz_results.html')


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
            return redirect('login')
    
    form = SignUpForm()
    return render(request, 'home/register.html', {'form': form})



# def customer_record(request, pk):
#     # if request.user.is_authenticated:
#     #     # to see records
#     #     # to get single the record col
#     #     customer_record = Record.objects.get(id=pk)
#     #     return render(request, 'home/record.html', {'customer_record': customer_record})

#     # else:
#     #     messages.success(request, "You must be logged in to view that page!")
#         return redirect('home')


# def delete_record(request, pk):
#     if request.user.is_authenticated:
#         delete_it = Record.objects.get(id=pk)
#         delete_it.delete()
#         messages.success(request, "Record deleted successfully!")
#         return redirect('home')

#     else:
#         messages.success(request, "You must be logged in to view that page!")
#         return redirect('home')

# def add_record(request):
#     form = AddRecordForm(request.POST or None)
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             if form.is_valid():
#                 add_record = form.save()
#                 messages.success(request, "Record Added..")
#                 return redirect('home')
#         return render(request, 'home/add_record.html', {"form": form})

#     else:
#         messages.success(request, "You must be logged in to view that page!")
#         return redirect('home')


# def update_record(request, pk):
#     if request.user.is_authenticated:
#         current_record = Record.objects.get(id=pk)
#         form = AddRecordForm(request.POST or None, instance=current_record)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Record has been updated!!!!")
#             return redirect('home')
#         return render(request, 'home/update_record.html', {"form": form})

#     else:
#         messages.success(request, "You must be logged in to view that page!")
#         return redirect('home')