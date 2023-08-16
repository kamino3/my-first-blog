
# views.py: このファイルにはユーザーのリクエストを処理し、レスポンスを返すロジックが含まれています。
# Djangoでは、ビューは関数ベースまたはクラスベースのいずれかで作成できます。
# 関数ベースのビューはリクエストオブジェクトを取得し、HttpResponseオブジェクトを返します。
# クラスベースのビューは、異なるHTTPメソッド（GET, POSTなど）を処理するためのより整理された方法を提供します。

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import ExamQuestion
from .models import Profile


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-created_date']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # <app>/<model>_<viewtype>.html

class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'text', 'tags']

    def test_func(self):
        if not self.request.user.is_authenticated:
            return False
        try:
            profile = Profile.objects.get(user=self.request.user)
        except Profile.DoesNotExist:
            profile = Profile.objects.create(user=self.request.user)
        return profile.has_passed_exam

        profile = Profile.objects.get(user=self.request.user)
        return profile.has_passed_exam

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('account_login')
        return render(self.request, 'blog/custom_403.html', status=403)
        return render(self.request, 'blog/custom_403.html', status=403)
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'text', 'tags']
    def form_valid(self, form):
        
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



from django.views import View
from django.shortcuts import render
from .models import Post

class SearchResultsView(View):
    def post(self, request):
        query = request.POST.get('query')
        results = Post.objects.filter(title__icontains=query)
        return render(request, 'blog/search_results.html', {'results': results})

def profile_view(request):
    return render(request, 'blog/profile.html', {})

@login_required(login_url='login-redirect')
def exam(request):
    questions = ExamQuestion.objects.order_by('?')[:10]
    
    if request.method == "POST":
        user_answers = {int(k): int(v) for k, v in request.POST.items() if k != "csrfmiddlewaretoken"}
        score = sum(1 for q_id, answer in user_answers.items() if ExamQuestion.objects.get(id=q_id).correct_answer == answer)
        if score >= 5:
            profile, created = Profile.objects.get_or_create(user=request.user)
            profile.has_passed_exam = True
            profile.save()
        return render(request, 'blog/exam_result.html', {'score': score, 'total_questions': 10})

    return render(request, 'blog/exam.html', {'questions': questions})


def account_info(request):

    if request.method == 'POST':
        display_name = request.POST.get('display_name')
        profile, created = Profile.objects.get_or_create(user=request.user)
        profile.display_name = display_name
        profile.save()
    return render(request, 'blog/account_info.html')
