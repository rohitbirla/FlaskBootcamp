import bcrypt
from flask_bcrypt import Bcrypt

bcrypt  = Bcrypt()

password = 'supersecretpassword'

hased_password = bcrypt.generate_password_hash(password=password)

# print(hased_password)

check =bcrypt.check_password_hash(hased_password,'supersecretpassword')
print(check)