from django import forms
from frontend.models import *
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
   
class CategoryForm(forms.ModelForm):
    cat_name = forms.CharField(label="Category Name*",
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Enter Category'}))
    cat_desc = forms.CharField(label='Description', required=False,
                           widget=forms.Textarea(
                               attrs={'class': 'form-control'}
                           ))
    catch_bot = forms.CharField(required=False,
                                widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    # clean_<fieldname> is use to validate for just one field

    def clean_cat_name(self):
        cat = self.cleaned_data.get('cat_name').capitalize()
        if Category.objects.filter(cat_name=cat).exists():
            raise forms.ValidationError(f'{cat} already exist')
        return cat

    class Meta():
        fields = '__all__'
        model = Category


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Username :', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Username'}))
    email = forms.EmailField(label='Email :',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
    first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Firstname'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Lastname'}))
    password1 = forms.CharField(label='Enter Password :', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
    botfield = forms.CharField(required=False, widget=forms.HiddenInput(),
                               validators=[validators.MaxLengthValidator(0)])

    def clean_email(self):
        email_field = self.cleaned_data.get('email')
        if User.objects.filter(email=email_field).exists():
            raise forms.ValidationError('Email already exist')
        return email_field

    class Meta():
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            return user


class BlogForm(forms.ModelForm):


    class Meta():
        exclude = ['date', 'user']
        model = Blog

        widgets={
            'blg_title': forms.TextInput(attrs={'class': 'form-control'}),
            'blg_content' : forms.Textarea(attrs={'class': 'form-control'}),
            'blg_image': forms.FileInput(attrs={'class': 'form-control'}),
            'appear_home' : forms.Select(attrs={'class': 'form-control'}),
           

        }

   

class EditUserForm(forms.ModelForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder': 'Enter Username' }))

    first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Firstname'}))

    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Lastname'}))
    
    email = forms.EmailField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
   

    botfield = forms.CharField(required=False, widget=forms.HiddenInput(),
                               validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = User
        fields = ['username',  'first_name', 'last_name', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        
        if commit:
            user.save()
            return user

class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old password', widget=forms.PasswordInput(
        attrs={'class':'form-control', 'placeholder':'Enter Password'}))
    new_password1 = forms.CharField(label='New password', widget=forms.PasswordInput(
        attrs={'class':'form-control', 'placeholder':'Enter Password'}))
    new_password2= forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class':'form-control', 'placeholder':'Enter Password'}))

    botfield = forms.CharField(required=False, widget=forms.HiddenInput(),
                               validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = User
        fields = ['password1', 'password2']

        # widgets = { 
        #         'password1': forms.NumberInput(attrs={'class': 'form-control'}),
        #         'password2': forms.NumberInput(attrs={'class': 'form-control'}),
            
        #     }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']
        
        if commit:
            user.save()
            return user


class EditBlog(forms.ModelForm):
    
    class Meta():
        model = Blog
        fields = ['blg_title', 'blg_image', 'blg_content']

        widgets={
        'blg_title': forms.TextInput(attrs={'class': 'form-control'}),
        'blg_image': forms.FileInput(attrs={'class': 'form-control'}),
        'blg_content' : forms.Textarea(attrs={'class': 'form-control'}),
        }
        

class EditListing(forms.ModelForm):
  
    class Meta():
        model = Hotel
        exclude = ['date', 'user']

        widgets = {
            'pst_title': forms.TextInput(attrs={'class': 'form-control'}),
            'pst_image': forms.FileInput(attrs={'class': 'form-control'}),
            'pst_image1': forms.FileInput(attrs={'class': 'form-control'}),
            'pst_image2': forms.FileInput(attrs={'class': 'form-control'}),
            'pst_image3': forms.FileInput(attrs={'class': 'form-control'}),
            'pst_image4': forms.FileInput(attrs={'class': 'form-control'}),
            'pst_image5': forms.FileInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'place': forms.TextInput(attrs={'class': 'form-control'}),
            'appear_home' : forms.Select(attrs={'class': 'form-control'}),
            
        }

   

class CommentForm(forms.ModelForm):
    user_name = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    comment_content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4'
    }))
    class Meta:
        model = Comment
        exclude = ['user', 'post']
        # fields = ('content', )


   
class ListingForm(forms.ModelForm):

    class Meta():
        model = Hotel
        fields = ['pst_title', 'pst_image', 'pst_image1', 'pst_image2','pst_image3','pst_image4', 
        'pst_image5', 'price','rate','content', 'appear_home','cat_id', 'place', 'featured', 'sponsored', ]
        exclude = ['date', 'user', 'location_id']
        widgets = {
            'pst_title': forms.TextInput(attrs={'class': 'form-control'}), 
            'pst_image': forms.FileInput(attrs={'class': 'form-control'}),
            'pst_image1': forms.FileInput(attrs={'class': 'form-control'}),
            'pst_image2': forms.FileInput(attrs={'class': 'form-control'}),
            'pst_image3': forms.FileInput(attrs={'class': 'form-control'}),
            'pst_image4': forms.FileInput(attrs={'class': 'form-control'}),
            'pst_image5': forms.FileInput(attrs={'class': 'form-control'}),
            'price': forms.Select(attrs={'class': 'form-control'}),
            'rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'place': forms.TextInput(attrs={'class': 'form-control'}),
            'appear_home' : forms.Select(attrs={'class': 'form-control'}),
            
            
        }


class ReviewForm(forms.ModelForm):
    ONE = 'one'
    TWO = 'two'
    THREE = 'three'
    FOUR = 'four'
    FIVE = 'five'
    CHOOSE = ''
    RATING_FIELD = [
        (ONE, '1'),
        (TWO, '2'),
        (THREE, '3'),
        (FOUR, '4'),
        (FIVE, '5'),
        (CHOOSE, 'Choose Rating'),
    ]

    user_name = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    email = forms.EmailField( widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    review_content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your review',
        'id': 'userreview',
        'rows': '4'
    }))
    class Meta:
        model = Review
        exclude = ['timestamp', 'post', 'email']
        widgets={
            'rating': forms.Select(attrs={'class': 'form-control'}),
        }
    
    
class FilterForm(forms.ModelForm):
    
    ONE = "10000"
    TWO = "15000"
    THREE = "20000"
    FOUR = "25000"
    FIVE = "30000"
    SIX = "35000"
    SEVEN = "40000"
    EIGHT = "45000"
    NINE = "50000"
    TEN = "55000"
    ONE1 = "60000"
    TWO2 = "65000"
    THREE3 = "70000"
    FOUR4 = "75000"
    FIVE5 = "80000"
    SIX6 = "85000"
    SEVEN7 = "90000"
    EIGHT8 = "95000"
    NINE9 = "100,000"    
    CHOOSE = ""

    PRICE= [
         (ONE, ' 10000'),
         (TWO, ' 15000'),
         (THREE, ' 20000'),
         (FOUR, ' 25000'),
         (FIVE, ' 30000'),
         (SIX, ' 35000'),
         (SEVEN, ' 40000'),
         (EIGHT, ' 45000'),
         (NINE, ' 50000'),
         (TEN, ' 55000'),
         (ONE1, ' 60000'),
         (TWO2, ' 65000'),
         (THREE3, ' 70000'),
         (FOUR4, ' 75000'),
         (FIVE5, ' 80000'),
         (SIX6, ' 85000'),
         (SEVEN7, ' 90000'),
         (EIGHT8, ' 95000'),
         (NINE9, ' 100000'),
         (CHOOSE, 'Price')
    ]
     
    ONE = "Ajah"
    TWO = "Agege"
    THREE = "Ikeja"
    FOUR = "Lekki Phase 1"
    FIVE = "Lekki Phase 2"
    SIX = "Ikoyi"
    SEVEN = "Oshodi"
    EIGHT = "Magodo"
    NINE = "Victoria Island"
    TEN = "Oniru VI"
    ONE1 = "Mowe"
    TWO2 = "Ikorodu"
    THREE3 = "Festac"
    FOUR4 = "Ojodu"
    FIVE5 = "Banana Island"
    SIX6 = "Maryland"
    SEVEN7 = "Ogba"
    EIGHT8 = "Barracks" 
    CHOOSE = ""

    LOCATION= [
          (ONE, "Ajah"),
        (TWO, "Agege"),
        (THREE, "Ikeja"),
        (FOUR, "Lekki Phase 1"),
        (FIVE, "Lekki Phase 2"),
        (SIX, "Ikoyi"),
        (SEVEN, "Oshodi"),
        (EIGHT, "Magodo"),
        (NINE, "Victoria Island"),
        (TEN, "Oniru VI"),
        (ONE1, "Mowe"),
       (TWO2, "Ikorodu"),
       (THREE3, "Festac"),
        (FOUR4, "Ojodu"),
       (FIVE5, "Banana Island"),
       (SIX6, "Maryland"),
       (SEVEN7, "Ogba"),
       (EIGHT8, "Barracks"), 
       (CHOOSE, 'Location')
    ]
    ONE = "Hotel"
    TWO = "Single Room"
    THREE = "Double Room"
    FOUR = "Suite Room"   
    CHOOSE = ""

    CATEGORY= [
         (ONE, 'Hotel'),
         (TWO, ' Single Room'),
         (THREE, 'Double Room'),
         (FOUR, 'Suite Room'),
         (CHOOSE, 'Hotel Room')
    ]
    
    

    price = forms.CharField(required=False, label='Price*', widget=forms.Select(choices=PRICE,
        attrs={'class': 'form-control', 'placeholder': 'Price'}))

    place = forms.CharField(required=False, label='Location*', widget=forms.Select(choices=LOCATION,
        attrs={'class': 'form-control', 'placeholder': 'Hotel Location'}))
    cat_id = forms.CharField(required=False, label='Location*', widget=forms.Select(choices=CATEGORY,
        attrs={'class': 'form-control', 'placeholder': 'Hotel Type'}))
    
    # location = forms.ModelChoiceField(
    #     queryset=Location.objects.all(), empty_label='Please Choose',
    #     widget=forms.Select(attrs={'class': 'form-control'}))
   


    class Meta():
        fields = ['price',  'cat_id', 'place']
        model = Hotel
    