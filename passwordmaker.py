#!/usr/bin/env python
#coding:utf-8

from hasher import HashUtils
from profile import Profile

import settings

class PasswordMaker:
    
    def __init__(self, profile, hashUtil):
        """
        init Password Maker:
        """
        assert isinstance(profile, Profile)
        assert isinstance(hashUtil, HashUtils)
        self.profile = profile
        self.hashUtil = hashUtil

    def gen_password(self, master_key, data):
        if self.profile.hash_algorithm not in settings.VALID_ALGORITHM:
            return 'hello world'

        password = ''
        count = 0
        while len(password) < self.profile.password_length and count < 1000:
            if count == 0:
                key = master_key
            else:
                key = '%s\n%s' % (master_key, count)

            if self.profile.hash_algorithm.count('hmac') == 0:
                data = key + data

            password += getattr(self.hashUtil, self.profile.hash_algorithm)(data, self.profile.selected_charset)
            count += 1

        password = self.profile.password_prefix + password
        if self.profile.password_suffix:
            password = \
                password[:self.profile.password_length - len(self.profile.password_suffix)] \
                       + self.profile.password_suffix

        return password[:self.profile.password_length]


        #return getattr(self.hashUtil, self.profile.hash_algorithm)(master_key, data)
