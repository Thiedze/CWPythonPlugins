from PythonPlugins import Plugin

class FirstPlugin(Plugin.Plugin):

    def __init__(self):
        print "plugin Test: constructor"

    def setCallback(self, callbackFunction):
        callbackFunction(self.Text)
        
    def prepare(self, Text):
        self.Text = Text