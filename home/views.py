from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import QuizSubmissions, Record
from django.db.models import Count
from django.http import HttpResponse

# from dns import message
def home(request):
    records = Record.objects.all()
    return render(request, 'home/index.html', {'records': records})

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
    if being_judged == 'Yes':
        score += 2
    elif being_judged == 'No':
        score += 1

    # Scoring for 'sleep_patterns'
    if sleep_patterns == 'Poor':
        score += 3
    elif sleep_patterns == 'Average':
        score += 2
    elif sleep_patterns == 'Good':
        score += 1

    # Add similar scoring logic for other questions...

    # Define your mental health categories based on the total score
    if score >= 10:
        return 'Possible generalized anxiety and it could be cured with accurate precautions and control of sentiments'
    elif 8 < score < 10:
        return 'Moderately Stressed'
    elif 10 <= score <= 12:
        return 'Might be social anxiety'
    elif score<=5:
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
    else:
        form = SignUpForm()
        return render(request, 'home/register.html', {'form': form})

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