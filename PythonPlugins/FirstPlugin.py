'''
Created on Nov 19, 2014

@author: thiems
'''

class Plugin:
    def __init__(self):
        print "plugin Test: constructor"

    def cb(self):
        print "plugin Test: callback"
        
    def setCallback(self, callbackFunction):
        callbackFunction(self.Text)
        
    def prepare(self, Text):
        self.Text = Text