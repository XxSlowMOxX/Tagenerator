import ts3

CH1 = 14129609
CH2 = 14129610
CH3 = 14129612
CH4 = 14129618

def tagenerator_edit_channel(strong):
    with ts3.query.TS3Connection("62.104.20.98", "10011") as ts3conn:
        try: 
            ts3conn.login(client_login_name="Moritz", client_login_password="qu9mYT9s") 
        except ts3.query.TS3QueryError as err:
            print("Login failed:", err.resp.error["msg"]) 
            exit(1) 
        ts3conn.use(port=9998)
        strong1 = strong[:39]
        strong2 = strong[40:79]
        strong3 = strong[80:119]
        strong4 = strong[120: 159]
        try:
            ts3conn.channeledit(cid=CH1, channel_name=strong1)
        except ts3.query.TS3QueryError:
                print("NO")
        if(strong2 == ""):
            try:
                ts3conn.channeledit(cid=CH2, channel_name="[cspacer"+str(CH2) + "]")
            except ts3.query.TS3QueryError:
                print("NO")
        else:
            ts3conn.channeledit(cid=CH2, channel_name=strong2)
        if(strong3 == ""):
            try:
                ts3conn.channeledit(cid=CH3, channel_name="[cspacer"+str(CH3) + "]")
            except ts3.query.TS3QueryError:
                print("NO")
        else:
            ts3conn.channeledit(cid=CH3, channel_name=strong3)
        if(strong4 == ""):
            try:
                ts3conn.channeledit(cid=CH4, channel_name="[cspacer"+str(CH4) + "]")
            except ts3.query.TS3QueryError:
                print("NO")
        else:
            ts3conn.channeledit(cid=CH4, channel_name=strong4)