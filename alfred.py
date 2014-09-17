#!/usr/bin/env python

from passwordmaker import PasswordMaker
from profile import Profile
from hasher import HashUtils
import settings

profile = Profile(title='test', selected_charset=settings.CHARSET_OPTIONS[0], password_length=12, hash_algorithm='sha256')
hashUtil = HashUtils()

pwm = PasswordMaker(profile=profile, hashUtil=hashUtil)

