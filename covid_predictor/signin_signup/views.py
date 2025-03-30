import logging
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from .models import CustomUser

logger = logging.getLogger(__name__)

def auth_page(request):
    """Render authentication page"""
    return render(request, 'auth.html')

@csrf_exempt
def api_signup(request):
    """Handle user registration"""
    if request.method == 'POST':
        try:
            # Get form data
            full_name = request.POST.get('full_name', '').strip()
            email = request.POST.get('email', '').strip().lower()
            password = request.POST.get('password', '').strip()
            profile_image = request.FILES.get('profile_image')

            # Validation
            if not all([full_name, email, password]):
                return JsonResponse({
                    'success': False,
                    'message': 'All fields are required'
                }, status=400)

            if CustomUser.objects.filter(email=email).exists():
                return JsonResponse({
                    'success': False,
                    'message': 'Email already exists'
                }, status=400)

            if len(password) < 6:
                return JsonResponse({
                    'success': False,
                    'message': 'Password must be at least 6 characters'
                }, status=400)

            # Create user
            user = CustomUser.objects.create_user(
                email=email,
                full_name=full_name,
                password=password
            )

            # Handle profile image
            if profile_image:
                fs = FileSystemStorage()
                filename = fs.save(f'profile_images/user_{user.id}_{profile_image.name}', profile_image)
                user.profile_image = filename
                user.save()

            # Authenticate and login
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({
                    'success': True,
                    'message': 'Registration successful',
                    'redirect': '/'
                })
            else:
                return JsonResponse({
                    'success': False,
                    'message': 'Authentication failed after registration'
                }, status=400)

        except Exception as e:
            logger.error(f"Signup error: {str(e)}")
            return JsonResponse({
                'success': False,
                'message': 'Server error during registration'
            }, status=500)

    return JsonResponse({
        'success': False,
        'message': 'Invalid request method'
    }, status=405)

@csrf_exempt
def api_login(request):
    """Handle user login"""
    if request.method == 'POST':
        try:
            email = request.POST.get('email', '').strip().lower()
            password = request.POST.get('password', '').strip()

            # Validation
            if not email or not password:
                return JsonResponse({
                    'success': False,
                    'message': 'Email and password are required'
                }, status=400)

            # Authenticate user
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({
                    'success': True,
                    'message': 'Login successful',
                    'redirect': '/'
                })
            else:
                return JsonResponse({
                    'success': False,
                    'message': 'Invalid email or password'
                }, status=400)

        except Exception as e:
            logger.error(f"Login error: {str(e)}")
            return JsonResponse({
                'success': False,
                'message': 'Server error during login'
            }, status=500)

    return JsonResponse({
        'success': False,
        'message': 'Invalid request method'
    }, status=405)

def api_logout(request):
    """Handle user logout"""
    logout(request)
    return JsonResponse({
        'success': True,
        'message': 'Logout successful',
        'redirect': '/auth/'
    })