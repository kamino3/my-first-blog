
from django.shortcuts import redirect
from .models import Profile

class ExamCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if user is trying to access post creation or editing
        if hasattr(request, 'user') and request.user.is_authenticated and ('post/new' in request.path or 'post/edit' in request.path):
            try:
                profile = Profile.objects.get(user=request.user)
                if not profile.has_passed_exam:
                    # Redirect to the exam page
                    return redirect('exam')
            except Profile.DoesNotExist:
                # If the profile does not exist, redirect to the exam page
                return redirect('exam')

        response = self.get_response(request)
        return response
