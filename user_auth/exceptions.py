from rest_framework.exceptions import APIException

class ValidationError(APIException):
    status_code = 422


# EMAIL EXCEPTIONS
class EmailAlreadyExists(APIException):
    status_code = 409
    default_detail = 'A user with that email address already exists.'
    default_code = 'Email Already Exists.'

class InvalidEmail(ValidationError):
    default_detail = 'Invalid email address!'
    default_code = 'Invalid Email!'



# DATE-OF-BIRTH EXCEPTIONS
class InvalidDateOfBirth(ValidationError):
    default_detail = 'Invalid Date Of Birth!'
    default_code = 'Invalid dob.'



# PASSWORD EXCEPTIONS
class PasswordTooShort(ValidationError):
    default_detail = 'Password has less than 6 characters. Password is too short!'
    default_code = 'Short Password.'


# OTHER EXCEPTIONS
class InvalidInformation(ValidationError):
    default_detail = 'Required fields have not been submitted!'
    default_code = 'Required Fields Not Submitted.'
