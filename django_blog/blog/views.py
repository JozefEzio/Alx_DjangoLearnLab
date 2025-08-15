from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, UserUpdateForm, PostForm, CommentForm
from .models import Post, Comment
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from typing import cast


def home(request):
    return render(request, "blog/home.html", {})


from django.contrib.auth.forms import AuthenticationForm


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect("blog/profile")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, "blog/login.html", {"form": form})


def logout_user(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("blog/home")


def register_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered!")
            return redirect("blog/profile")
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = CustomUserCreationForm()

    return render(request, "blog/register.html", {"form": form})


@login_required(login_url="blog/login")
def profile(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, "blog/profile.html", {"form": form})


class PostListView(ListView):
    model = Post
    template_name = "blog/posts.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        # Extra data: comment form + existing comments
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        # Handle comment submission
        self.object = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = self.object
            new_comment.author = request.user
            new_comment.save()
            return redirect("post-detail", pk=self.object.pk)

        # If form invalid, re-show page with errors
        return self.render_to_response(self.get_context_data(form=form))


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("posts")

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Post created successfully.")
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Post updated successfully.")
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("posts")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Post deleted successfully.")
        return super().delete(request, *args, **kwargs)

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Comment updated successfully.")
        return super().form_valid(form)

    def get_success_url(self):
        comment = cast(Comment, self.get_object())
        return reverse("post-detail", kwargs={"pk": comment.post.pk})


    def test_func(self):
        # Only the author can edit their comment
        comment = cast(Comment, self.get_object())
        return self.request.user == comment.author
    
    
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "blog/comment_confirm_delete.html"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Comment deleted successfully.")
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        # Redirect back to the post detail page
        comment = cast(Comment, self.get_object())
        return reverse("post-detail", kwargs={"pk": comment.post.pk})

    def test_func(self):
        # Only the author can delete their comment
        comment = cast(Comment, self.get_object())
        return self.request.user == comment.author