from django.shortcuts import get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views import generic

from .models import Post, Comment
from .forms import PostModelForm, CommentModelForm


class PostListView(generic.ListView):
    """
    Generic ListView for the front page/feed of a user.
    """
    model = Post
    template_name = 'posts/front-page.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        """Return posts in queryset by newest posted_date."""
        return Post.objects.order_by('-posted_date')


class UserPostListView(generic.ListView):
    """
    Generic ListView for the displaying all the posts of a
    specific user.
    """
    model = Post
    template_name = 'posts/user-posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        """
        Return queryset of specific user. User is identified through
        kwargs in url.
        """
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-posted_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        user_info = User.objects.get(username=user)
        context['user_info'] = user_info
        return context


class PostDetailView(generic.DetailView):
    """
    Generic DetailView for posts.
    """
    model = Post
    template_name = 'posts/post-detail.html'


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    """
    Generic CreateView for users to create posts.
    """
    model = Post
    template_name = 'posts/post-form.html'
    form_class = PostModelForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    """
    Generic CreateView for users to update posts.
    """
    model = Post
    template_name = 'posts/post-form.html'
    form_class = PostModelForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """
    Generic DeleteView for users to delete posts.
    """
    model = Post
    template_name = 'posts/post-delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    """
    Generic CreateView for users to create comments.
    """
    model = Comment
    template_name = 'posts/comment-form.html'
    form_class = CommentModelForm

    def form_valid(self, form):
        post = get_object_or_404(Post, id=self.kwargs.get('pk'))
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    """
    Generic CreateView for users to update comments.
    """
    model = Comment
    template_name = 'posts/comment-form.html'
    form_class = CommentModelForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """
    Generic DeleteView for users to delete comments.
    """
    model = Comment
    template_name = 'posts/comment-delete.html'
    success_url = '/'

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False

    def get_success_url(self):
        post = self.object.post.id
        return reverse('post-detail', kwargs={'pk': post})
