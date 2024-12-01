from django.shortcuts import render

# Simulated user database
users = {}

# HTML form view
def sign_up_by_html(request):
    info = {}  # Initialize the info variable as an empty dictionary

    # Your existing view logic (if any) goes here...

    return render(request, template_name='fifth_task/registration_page.html', context={'info': info})

# Django form view with validation logic
def sign_up_by_django(request):
    info = {}

    if request.method == 'POST':
        # Retrieve form inputs
        login = request.POST.get('login', '').strip()
        password1 = request.POST.get('password1', '').strip()
        password2 = request.POST.get('password2', '').strip()
        age = request.POST.get('age', '').strip()

        # Validation checks
        if not login or not password1 or not password2 or not age:
            info['error'] = 'Все поля должны быть заполнены.'
        elif password1 != password2:
            info['error'] = 'Пароли не совпадают.'
        elif not age.isdigit() or int(age) < 18:
            info['error'] = 'Вы должны быть старше 18.'
        elif login in users:
            info['error'] = f"Пользователь с логином '{login}' уже существует."
        else:
            # Save new user
            users[login] = {'password': password1, 'age': int(age)}
            info['success'] = f"Приветствуем, {login}!"
            # Clear form fields after success
            info['login'] = ''
            info['age'] = ''

    return render(request, template_name='fifth_task/registration_page.html', context={'info': info})
