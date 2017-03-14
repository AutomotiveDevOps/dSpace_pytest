"""
Dummy library for dSpace pytest demo
"""
import os

class Appl(object):
    def __init__(self, *args, **kwargs):
        self.app = args[0]
        self.platform = args[1]
        
    def __repr__(self):
        return "dSpace({}, {})".format(self.app, self.platform)