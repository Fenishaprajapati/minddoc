from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Record, Venue, Event, Goalbasedcare, Goalbasedcare2, Goalbasedcare3

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",
                             widget=forms.TextInput(attrs={'class': 'form-control another','style':'width:730px', 'placeholder': 'Email Address'}))
    firstname = forms.CharField(label="",
                                widget=forms.TextInput(attrs={'class': 'forms-control another', 'style':'width:730px','placeholder': 'Firstname'}))
    lastname = forms.CharField(label="",
                               widget=forms.TextInput(attrs={'class': 'forms-control lastnameanother', 'style':'width:730px','placeholder': 'Lastname'}))

    class Meta:
        model = User
        fields = ('username', 'firstname', 'lastname', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        # help text pops up when errors shows up
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields[
            'password1'].help_text = '<ul class="form-text text-muted small"><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields[
            'password2'].help_text = '<span class="form-text text-muted"></span>'






class AddRecordForm(forms.ModelForm):
    firstname = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "First Name", "class": "form-control"}), label="")
    lastname = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Last Name", "class": "form-control"}), label="")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Email", "class": "form-control"}), label="")
    contactNumber = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Phone Number", "class": "form-control"}), label="")
    zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Zip code", "class": "form-control"}), label="")

    class Meta:
        model = Record
        exclude = ("user",)



class VenueForm(forms.ModelForm):
    class Meta:
        model=Venue
        # fields="__all__"#for all the fields of the venue model
        fields=('name', 'address', 'zip_code','phone', 'web', 'email_address', 'venue_image')
        labels={
            'name':'',
            'address':'',
            'zip_code':'',
            'phone':'',
            'web':'',
            'email_address':'',
            'venue_image':'',
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Venue Name'}),
            'address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Venue Address'}),
            'zip_code':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip code'}),
            'phone':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone number'}),
            'web':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Website'}),
            'email_address':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email address'}),
        }
#Admin superuserEVENT FORM
class EventFormAdmin(forms.ModelForm):
    class Meta:
        model=Event
        # fields="__all__"#for all the fields of the venue model
        fields=('name', 'event_date', 'venue', 'description')
        labels={
            'name':'',
            'event_date':'YYYY-MM-DD HH:MM:SS',
            'venue':'Venue',
            'description':'',
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Name'}),
            'event_date':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Date'}),
            'venue':forms.Select(attrs={'class':'form-select', 'placeholder':'Venue'}),
            'description':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Description'}),
        }

# User event form
class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        # fields="__all__"#for all the fields of the venue model
        fields=('name', 'event_date', 'venue',  'description')
        labels={
            'name':'',
            'event_date':'YYYY-MM-DD HH:MM:SS',
            'venue':'Venue',
            'description':'',
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Name'}),
            'event_date':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Date'}),
            'venue':forms.Select(attrs={'class':'form-select', 'placeholder':'Venue'}),          
            'description':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Description'}),
        }

class GbcForm(forms.ModelForm):
    class Meta:
        model=Goalbasedcare
        # fields="__all__"#for all the fields of the venue model
        fields=('task', 'description')
        labels={
            'task':'',
            'description':'',
        }
        widgets={
            'task':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Task'}),
            'description':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Description'}),
        }

