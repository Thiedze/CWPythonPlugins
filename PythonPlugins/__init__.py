import os
import sys

from PythonPlugins import Plugin, PluginHandler


class Master:
        
    def __init__(self):
        self.path = "/home/thiems/Programming/workspace/CWPythonPlugins/PythonPlugins"
        self.plugins = {}
        self.PluginHandler = PluginHandler.PluginHandler()

        self.loadPlugins()

    def loadPlugins(self):
        files = os.listdir(self.path)
        for f in files:
            fname, ext = os.path.splitext(f)
            if ext == ".py" and fname != '__init__' and fname != 'Plugin':
                mod = __import__(fname)
                if fname == 'FirstPlugin':
                    self.plugins[fname] = self.PluginHandler.GetFirstPlugin(mod);
                    
    def runPluginTest(self):
        for plugin in self.plugins.values():
                plugin.prepare('Test')
                plugin.setCallback(self.pluginCallback)
                
    def pluginCallback(self, Text):
        print(Text)
        
Master = Master()
Master.runPluginTest()