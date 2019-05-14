import json
import base64
import qrcode
with open('C:\……\gui-config.json','r') as load_f: #路径
    load_dict = json.load(load_f)
    for a in load_dict["configs"]:
        s =a['method']+':'+a['password']+'@'+a['server']+':'+str(a['server_port'])
        remarks='/#'+base64.b64encode(a['remarks'])
        s='ss://'+base64.b64encode(s+remarks)
        img=qrcode.make(s)
        img.show()
