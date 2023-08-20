from django import forms

class CommentForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Please enter your full name : ",'class':'form-control'})
    )

    job = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Please enter your job :",'class':'form-control'})
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Please enter your email :",'class':'form-control'})
    )

    subject = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Please enter your subject :",'class':'form-control'})
    )

    comment = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Please enter your comments :",'class':'form-control','height':"10px"})
    )

    show_massage = forms.BooleanField()