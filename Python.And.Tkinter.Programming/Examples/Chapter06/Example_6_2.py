from tkinter import *
import Pmw

eventList = { '2': 'KeyPress', '3': 'KeyRelease', '4': 'ButtonPress',
              '5': 'ButtonRelease', '6': 'Motion', '7': 'Enter',
              '8': 'Leave', '9': 'FocusIn', '10': 'FocusOut',
              '12': 'Expose', '15': 'Visibility', '17': 'Destroy',
              '18': 'Unmap', '19': 'Map', '21': 'Reparent',
              '22': 'Configure', '24': 'Gravity', '26': 'Circulate',
              '28': 'Property',  '32': 'Colormap','36': 'Activate',
              '37': 'Deactivate' }

root = Tk()
Pmw.initialise()

def reportEvent(event):
    rpt = ''
    rpt += '\n\n{}'.format(80*'=')
    rpt += '\nEvent: type={} ({})'.format(event.type, eventList.get(event.type, 'Unknown'))
    rpt += '\ntime={}'.format(event.time)
    rpt += '  widget={}'.format(event.widget)
    rpt += '  x={}, y={}'.format(event.x, event.y)
    rpt += '  x_root={}, y_root={}'.format(event.x_root, event.y_root)
    rpt += '  y_root={}'.format(event.y_root)
    rpt += '\nserial={}'.format(event.serial)
    rpt += '  num={}'.format(event.num)
    rpt += '  height={}'.format(event.height)
    rpt += '  width={}'.format(event.width)
    rpt += '  keysym={}'.format(event.keysym)
    rpt += '  ksNum={}'.format(event.keysym_num)

    #### some event types don't have these attributes 
    try:
        rpt += '  focus={}'.format(event.focus)
    except:
        pass

    try:
        rpt += '  send={}'.format(event.send_event)
    except:
        pass
    
    if event.type == '17':  # '17' 是 Destroy 事件的类型编号
        print(rpt)
        return  # 直接返回，不处理 Destroy 事件

    text2.yview(END)
    text2.insert(END, rpt)
    
frame = Frame(root, takefocus=1, highlightthickness=2)
text  = Entry(frame, width=10, takefocus=1, highlightthickness=2)
text2 = Pmw.ScrolledText(frame)

for event in eventList.values():
    frame.bind('<{}>'.format(event), reportEvent)
    text.bind('<{}>'.format(event), reportEvent)

text.pack()
text2.pack(fill=BOTH, expand=YES)
frame.pack()

text.focus_set()
root.mainloop()
