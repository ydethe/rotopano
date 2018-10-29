from singleton3 import Singleton

from RPFirmware.actions.PanoramaAction import PanoramaAction


class ActionManager (object, metaclass=Singleton):
    def __init__(self):
        self.handlers = {}
        self.handlers[PanoramaAction.getName()] = PanoramaAction()

    def getAction(self, name):
        return self.handlers[name]
        
    def handleRequest(self, args):
        act_name = args.pop('action')
        act = self.getAction(act_name)
        
        if 'cmd' in args.keys():
            cmd = args.pop('cmd')
        else:
            cmd = ''
        
        # import code
        # code.interact(local=locals())
        
        if cmd == 'start':
            act.start(**args)
        elif cmd == 'stop':
            act.stop()
        elif cmd == 'pause':
            act.pause()
        elif cmd == 'resume':
            act.resume()
        elif cmd == '':
            pass
        else:
            raise KeyError
            
        dat = act.getState()
        
        return dat
        
        
# if __name__ == '__main__':
    # a = ActionManager()
    # a.handleRequest({'action':'panorama','cmd':'start','pano_mode':'Photo','pano_interval':1.})
    