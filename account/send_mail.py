# from django.core.mail import send_mail
#
#
# def send_activation_code(email, activation_code):
#     activation_url = f'http://localhost:8000/api/v1/accounts/activate/{activation_code}'
#     message = f"""
#         Thank you for signing up.
#         Please activate your account.
#         Activation link: {activation_url}
#     """
#     send_mail(
#         'Activate your account',
#         message,
#         'test@test.com',
#         [email, ],
#         fail_silently=False
#     )
#
# # from django.core.mail import send_mail
#
# #
# # def send_activation_code(email,activation_code):
# #     code = user.activation_code
# #     full_link = f'http://localhost:8000/api/v1/accounts/activate/{code}'
# #     to_email = user.email
# #     send_mail(
# #         'Your activation code',
# #         full_link,
# #         'from@example.com',
# #         [to_email],
# #         fail_silently=False,
# #     )


from django.core.mail import send_mail


def send_confirmation_email(user):
    code = user.activation_code
    full_link = f'Ваш код: http://localhost:8000/api/v1/accounts/activate/{code}'
    to_email = user.email
    send_mail(
        'Ваш активационный код!',
        full_link,
        'from@example.com',
        [to_email],
        fail_silently=False,
    )


def send_reset_password(user):
    code = user.activation_code
    full_link = f'Ваш код: http://localhost:8000/api/v1/accounts/activate/{code}'
    to_email = user.email
    send_mail(
        'Активируйте ваш новый код!',
        full_link,
        'from@example.com',
        [to_email],
        fail_silently=False,
    )