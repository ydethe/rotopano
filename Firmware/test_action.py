from RPFirmware.ActionManager import ActionManager


a = ActionManager()
dat={'pano_mode': 'Photo', 'pano_interval': 1.0,'action':'panorama','cmd':'start'}

a.handleRequest(dat)
