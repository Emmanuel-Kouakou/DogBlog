from django import forms

from blog.models import BlogPost

JOBS = (
("python" , "Développeur Python"),
("javascript", "Développeur JS"),
("csharp", "Développeur C#")
)

class SignupForm(forms.Form):
    pseudo = forms.CharField(max_length=8, strip=True, required=False)
    email = forms.EmailField()
    password = forms.CharField(min_length=6, widget=forms.PasswordInput())
    job = forms.ChoiceField(choices=JOBS)
    cgu_accept = forms.BooleanField(initial=True)
    
    def clean_pseudo(self):
        
        pseudo = self.cleaned_data["pseudo"]
        
        if "$" in pseudo:
            raise forms.ValidationError('Le pseudo ne doit pas contenir le signe $.')
        
        return pseudo
    

class BlogForm(forms.ModelForm):
    
    class Meta:
        model = BlogPost
        exclude = {'slug'}
        
        labels = {"title":"titre", "content":"contenu"}   
        
        widgets = {"date": forms.SelectDateWidget(years=range(1998,2040))} 
    
    