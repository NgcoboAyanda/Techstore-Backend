from rest_framework.exceptions import APIException

##EXCEPTIONS ARE ORDERED BY STATUS CODES

#2X

#3X

#4X
# Status code 401 (Unauthorized)
# When wrong or no credentials are entered.
class HTTP401(APIException):
    status_code = 401

class WrongPassword(HTTP401):
    default_detail = 'The password you entered is incorrect. Please try again!'
    default_code = 'Wrong password.'

# Status code 404 (Not found)
# When the requested data does not exist
class HTTP404(APIException):
    status_code = 404

class UserDoesNotExist(HTTP404):
    default_detail = 'Error! There is no user associated with the given email address.'
    default_code = 'User Not Found!'


# Status code 409 (Conflict)
#*Mostly validation errors
class HTTP409(APIException):
    status_code = 409

class EmailAlreadyExists(HTTP409):
    status_code = 409
    default_detail = 'A user with that email address already exists.'
    default_code = 'Email Already Exists.'


# Status code 422 (Unprocessable Entity)
class HTTP422(APIException):
    status_code = 422

class InvalidDateOfBirth(HTTP422):
    default_detail = 'Invalid date of birth!'

class InvalidEmail(HTTP422):
    default_detail = 'Invalid email address!'
    default_code = 'Invalid Email!'

class InvalidPassword(HTTP422):
    default_detail = 'Enter a valid password.'
    default_code = 'Invalid Password.'

class PasswordTooShort(HTTP422):
    default_detail = 'Password has less than 6 characters. Password is too short!'
    default_code = 'Password Too Short.'

class InvalidInformation(HTTP422):
    default_detail = 'Required fields have not been submitted!'
    default_code = 'Required Fields Not Submitted.'
