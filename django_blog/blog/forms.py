from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content")
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Post title"}),
            "content": forms.Textarea(
                attrs={"rows": 8, "placeholder": "Write your post..."}
            ),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(
                attrs={"rows": 3, "placeholder": "Write your comment here..."}
            ),
        }
