from django.core.mail import send_mail
from imooc.settings import EMAIL_FROM,ACTIVATE_URL
import string,random
from users.models import EmailVerifyRecord

def send_email(email,type_name):
    subject = "账号激活"
    code = random_code(length=20)
    record = EmailVerifyRecord(code=code,email=email,send_type=type_name)
    record.save()
    path = type_name+'/'+code
    body = "请点击以下链接用于激活你的账号:{}".format(ACTIVATE_URL+path)
    send_mail(subject=subject,
                message=body,
                from_email=EMAIL_FROM,
                recipient_list=[email])



def random_code(length=8):
    """
    whitespace -- a string containing all ASCII whitespace
    ascii_lowercase -- a string containing all ASCII lowercase letters
    ascii_uppercase -- a string containing all ASCII uppercase letters
    ascii_letters -- a string containing all ASCII letters
    digits -- a string containing all ASCII decimal digits
    hexdigits -- a string containing all ASCII hexadecimal digits
    octdigits -- a string containing all ASCII octal digits
    punctuation -- a string containing all ASCII punctuation characters
    printable -- a string containing all ASCII characters considered printable
    """
    random_str = string.ascii_letters+string.digits
    return ''.join(random.choices(random_str,k=length))
