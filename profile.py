#!/usr/bin/env python
# coding:utf-8

__author__ = 'joe'

import uuid

class Profile():
    def __init__(self,
                 # basic information
                 id = str(uuid.uuid4()), title='default',

                 # settings for the URL generation
                 url_protocol = False, url_subdomain = False, url_domain = True, url_path = False,

                 # use this value instead of domain if not null
                 use_text = '',

                 # settings for the key generation
                 hash_algorithm = 'sha256', username = '', modifier = '', password_length = 8,
                 selected_charset = 'utf8',
                 password_prefix = '', password_suffix = '', where_to_use_l33t = 'off', l33t_level = 0
                 ):
        self.id = id
        self.title = title
        self.url_protocol = url_protocol
        self.url_subdomain = url_subdomain
        self.url_domain = url_domain
        self.url_path = url_path
        self.use_text = use_text
        self.hash_algorithm = hash_algorithm
        self.username = username
        self.modifier = modifier
        self.password_length = password_length
        self.selected_charset = selected_charset
        self.password_prefix = password_prefix
        self.password_suffix = password_suffix
        self.where_to_use_l33t = where_to_use_l33t
        self.l33t_level = l33t_level


    @staticmethod
    def all_profiles():
        pass