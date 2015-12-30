import lcm
from mvec_pk import mvec
import numpy as np

data_dict={}

def process_msg(title, contents):
    print "----------------------------------------------------------------------------------"
    print "Message title: ", title
    print "----------------------------------------------------------------------------------"
    t=title.split('_')
    df = np.array(contents[0]) - np.array(contents[1])
    if(len(t)==1 or t[1]=='d'):
        print df
        print np.mean(df)
    elif(t[1] == 'm'):
        print np.mean(df)
    print "----------------------------------------------------------------------------------"
    

def my_handler_test(channel, data):
    msg = mvec.decode(data)

    if(data_dict.has_key(msg.title)==False):
        data_dict[msg.title] = [msg.vec]
    else:
        if(len(data_dict[msg.title]) < 2):
            data_dict[msg.title].append(msg.vec)
            process_msg(msg.title, data_dict[msg.title])



lc = lcm.LCM()
subscription = lc.subscribe("TEST", my_handler_test)

try: 
    while True:
        lc.handle()
except KeyboardInterrupt:
    pass
