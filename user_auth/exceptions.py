from rest_framework.exceptions import APIException

class ValidationError(APIException):
    status_code = 422


# EMAIL EXCEPTIONS
class EmailAlreadyExists(APIException):
    status_code = 409
    default_detail = 'Error! A user with that email address already exists.'
    default_code = 'Email Already Exists.'

# DATE-OF-BIRTH ERRO
class InvalidDateOfBirth(ValidationError):
    default_detail = 'Invalid date_of_birth!'
    default_code = 'Invalid dob.'

# PASSWORD EXCEPTIONS
class PasswordTooShort(ValidationError):
    default_detail = 'Password is too short!'
    default_code = 'Short Password.'
