#!/usr/bin/env python
# coding:utf-8

__author__ = 'joe'

import ConfigParser

class Config():
    def __init__(self, env='development'):
        self.configParser = ConfigParser.ConfigParser()
        self.configParser.read('./config/' + env + '.ini')
        print self.configParser.sections()

    def get(self, field, key):
        return self.configParser.get(field, key)