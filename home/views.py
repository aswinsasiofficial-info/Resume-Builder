from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def landing(request):
    """Render the landing page."""
    return render(request, 'landing.html')


@login_required
def home(request):
    """Render the home page with template selection."""
    template = request.GET.get('template', 'classic')
    return render(request, 'home.html', {'selected_template': template})


@login_required
def builder(request):
    """Render the resume builder form."""
    return render(request, 'index.html')


@login_required
def builder_fullstack(request):
    """Render the resume builder form tailored for Full Stack Developers."""
    context = {
        'profession': 'Full Stack Developer',
        'suggested_skills': [
            'JavaScript', 'Python', 'React', 'Node.js', 'Django', 'MongoDB',
            'PostgreSQL', 'Docker', 'AWS', 'Git', 'REST APIs', 'GraphQL'
        ],
        'suggested_projects': [
            'E-commerce Platform', 'Social Media Dashboard', 'Task Management App',
            'Real-time Chat Application', 'API Gateway Service'
        ],
        'template_type': 'modern',
        'form_title': 'Full Stack Developer Resume Builder'
    }
    return render(request, 'builder_fullstack.html', context)


@login_required
def builder_3d_generalist(request):
    """Render the resume builder form tailored for 3D Generalists."""
    context = {
        'profession': '3D Generalist',
        'suggested_skills': [
            'Maya', 'Blender', 'ZBrush', 'Substance Painter', 'Houdini',
            'Arnold', 'V-Ray', 'Unity', 'Unreal Engine', 'Marvelous Designer',
            'Rigging', 'Motion Capture'
        ],
        'suggested_projects': [
            'Character Modeling Portfolio', 'Environment Design', 'Product Visualization',
            'Animation Reel', 'VFX Simulation'
        ],
        'template_type': 'creative',
        'form_title': '3D Generalist Resume Builder'
    }
    return render(request, 'builder_3d.html', context)


@login_required
def builder_data_scientist(request):
    """Render the resume builder form tailored for Data Scientists."""
    context = {
        'profession': 'Data Scientist',
        'suggested_skills': [
            'Python', 'R', 'SQL', 'TensorFlow', 'PyTorch', 'Scikit-learn',
            'Pandas', 'NumPy', 'Tableau', 'Power BI', 'Spark', 'Hadoop',
            'Machine Learning', 'Deep Learning', 'Statistical Analysis'
        ],
        'suggested_projects': [
            'Predictive Analytics Model', 'NLP Sentiment Analysis', 'Recommendation System',
            'Computer Vision Project', 'Time Series Forecasting'
        ],
        'template_type': 'classic',
        'form_title': 'Data Scientist Resume Builder'
    }
    return render(request, 'builder_data.html', context)


@login_required
def builder_ux_designer(request):
    """Render the resume builder form tailored for UX/UI Designers."""
    context = {
        'profession': 'UX/UI Designer',
        'suggested_skills': [
            'Figma', 'Adobe XD', 'Sketch', 'InVision', 'Prototyping',
            'User Research', 'Wireframing', 'Design Systems', 'HTML/CSS',
            'Interaction Design', 'Usability Testing', 'Visual Design'
        ],
        'suggested_projects': [
            'Mobile App Redesign', 'Design System Creation', 'E-commerce UX Overhaul',
            'Dashboard Interface Design', 'User Research Study'
        ],
        'template_type': 'minimalist',
        'form_title': 'UX/UI Designer Resume Builder'
    }
    return render(request, 'builder_ux.html', context)


@login_required
def builder_executive(request):
    """Render the resume builder form tailored for Executives."""
    context = {
        'profession': 'Executive',
        'suggested_skills': [
            'Strategic Planning', 'Team Leadership', 'P&L Management',
            'Business Development', 'Stakeholder Management', 'Change Management',
            'M&A', 'Board Governance', 'Crisis Management', 'Investor Relations'
        ],
        'suggested_projects': [
            'Company Turnaround', 'IPO Launch', 'Merger Integration',
            'Digital Transformation', 'Market Expansion'
        ],
        'template_type': 'executive',
        'form_title': 'Executive Resume Builder'
    }
    return render(request, 'builder_executive.html', context)


@login_required
def gen_resume(request):
    """Generate and display the resume page."""
    if request.method == 'POST':
        template_type = request.POST.get('template_type', 'classic')

        context = {
            # Template type
            'template_type': template_type,
            # Profile
            'name': request.POST.get('name', ''),
            'title': request.POST.get('title', ''),
            'email': request.POST.get('email', ''),
            'phone': request.POST.get('phone', ''),
            'about': request.POST.get('about', ''),
            # Contact extras
            'location': request.POST.get('location', ''),
            'linkedin': request.POST.get('linkedin', ''),
            'github': request.POST.get('github', ''),
            'portfolio': request.POST.get('portfolio', ''),
            # Skills
            'prog_langs': request.POST.get('prog_langs', ''),
            'frameworks': request.POST.get('frameworks', ''),
            'databases': request.POST.get('databases', ''),
            'dev_tools': request.POST.get('dev_tools', ''),
            'web_tech': request.POST.get('web_tech', ''),
            # Experience 1
            'company1': request.POST.get('company1', ''),
            'post1': request.POST.get('post1', ''),
            'duration1': request.POST.get('duration1', ''),
            'location1': request.POST.get('location1', ''),
            'lin11': request.POST.get('lin11', ''),
            'achievements1': request.POST.get('achievements1', ''),
            # Experience 2
            'company2': request.POST.get('company2', ''),
            'post2': request.POST.get('post2', ''),
            'duration2': request.POST.get('duration2', ''),
            'location2': request.POST.get('location2', ''),
            'lin21': request.POST.get('lin21', ''),
            'achievements2': request.POST.get('achievements2', ''),
            # Experience 3
            'company3': request.POST.get('company3', ''),
            'post3': request.POST.get('post3', ''),
            'duration3': request.POST.get('duration3', ''),
            'location3': request.POST.get('location3', ''),
            'lin31': request.POST.get('lin31', ''),
            # Project 1
            'project1': request.POST.get('project1', ''),
            'durat1': request.POST.get('durat1', ''),
            'desc1': request.POST.get('desc1', ''),
            'project_tech1': request.POST.get('project_tech1', ''),
            'project_url1': request.POST.get('project_url1', ''),
            # Project 2
            'project2': request.POST.get('project2', ''),
            'durat2': request.POST.get('durat2', ''),
            'desc2': request.POST.get('desc2', ''),
            'project_tech2': request.POST.get('project_tech2', ''),
            'project_url2': request.POST.get('project_url2', ''),
            # Education 1
            'degree1': request.POST.get('degree1', ''),
            'college1': request.POST.get('college1', ''),
            'year1': request.POST.get('year1', ''),
            'gpa1': request.POST.get('gpa1', ''),
            'honors1': request.POST.get('honors1', ''),
            # Education 2
            'degree2': request.POST.get('degree2', ''),
            'college2': request.POST.get('college2', ''),
            'year2': request.POST.get('year2', ''),
            'gpa2': request.POST.get('gpa2', ''),
            'honors2': request.POST.get('honors2', ''),
            # Additional fields
            'languages': request.POST.get('languages', ''),
            'certifications': request.POST.get('certifications', ''),
            'interests': request.POST.get('interests', ''),
            # References
            'reference_name1': request.POST.get('reference_name1', ''),
            'reference_title1': request.POST.get('reference_title1', ''),
            'reference_contact1': request.POST.get('reference_contact1', ''),
            'reference_name2': request.POST.get('reference_name2', ''),
            'reference_title2': request.POST.get('reference_title2', ''),
            'reference_contact2': request.POST.get('reference_contact2', ''),
            # Board positions
            'board1': request.POST.get('board1', ''),
            'board_role1': request.POST.get('board_role1', ''),
            'board_year1': request.POST.get('board_year1', ''),
            'board2': request.POST.get('board2', ''),
            'board_role2': request.POST.get('board_role2', ''),
            'board_year2': request.POST.get('board_year2', ''),
            # Awards
            'award1': request.POST.get('award1', ''),
            'award_year1': request.POST.get('award_year1', ''),
            'award2': request.POST.get('award2', ''),
            'award_year2': request.POST.get('award_year2', ''),
        }

        # Select template based on type
        template_map = {
            'classic': 'resume.html',
            'modern': 'resume_modern.html',
            'minimalist': 'resume_minimalist.html',
            'creative': 'resume_creative.html',
            'executive': 'resume_executive.html',
        }

        template_name = template_map.get(template_type, 'resume.html')
        return render(request, template_name, context)
    return render(request, 'index.html')


def login_view(request):
    """Handle user login."""
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid password.')
        except User.DoesNotExist:
            messages.error(request, 'No account found with this email.')

    return render(request, 'login.html')


def signup_view(request):
    """Handle user registration."""
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'An account with this email already exists.')
            return render(request, 'signup.html')

        username = email.split('@')[0]
        base_username = username
        counter = 1
        while User.objects.filter(username=username).exists():
            username = f"{base_username}{counter}"
            counter += 1

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        messages.success(request, 'Account created successfully! Please sign in.')
        return redirect('login')

    return render(request, 'signup.html')


def logout_view(request):
    """Handle user logout."""
    logout(request)
    return redirect('login')


@login_required
def profile(request):
    """Handle user profile dashboard."""
    # Get or create user profile for mobile number
    mobile = request.session.get('mobile', '')

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'update_profile':
            # Update personal information
            request.user.first_name = request.POST.get('first_name', '')
            request.user.last_name = request.POST.get('last_name', '')
            request.user.save()

            # Store mobile in session (since we're using default User model)
            mobile = request.POST.get('mobile', '')
            request.session['mobile'] = mobile

            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')

        elif action == 'change_password':
            # Change password
            current_password = request.POST.get('current_password')
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')

            if not request.user.check_password(current_password):
                messages.error(request, 'Current password is incorrect.')
                return redirect('profile')

            if new_password != confirm_password:
                messages.error(request, 'New passwords do not match.')
                return redirect('profile')

            request.user.set_password(new_password)
            request.user.save()

            # Re-authenticate user after password change
            user = authenticate(request, username=request.user.username, password=new_password)
            if user:
                login(request, user)

            messages.success(request, 'Password changed successfully!')
            return redirect('profile')

        elif action == 'delete_account':
            # Delete account
            password = request.POST.get('password')

            if not request.user.check_password(password):
                messages.error(request, 'Password is incorrect.')
                return redirect('profile')

            request.user.delete()
            messages.success(request, 'Your account has been deleted.')
            return redirect('landing')

    return render(request, 'profile.html', {'mobile': mobile})