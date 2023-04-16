from django.core.mail import send_mail

def send_activation_code(email, code):
    send_mail(
        'FIlm_hackathon',
        f'http://localhost:8000/api/v1/account/activate/{code}/', #body
        'ajnarg523@gmail.com', #from
        [email]   # to
    )


def send_reset_password_code(email, code):
    send_mail(
        'Film_hackathon',
        f'Чтоб сбросить пароль вам нужно  = {code}',
        'ajnarg523@gmail.com',
        [email]
    )    