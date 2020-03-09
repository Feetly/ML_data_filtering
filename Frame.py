from tkinter import *

root = Tk()
root.title('MileCode ') 
root.state('zoomed')
root.bind("<F11>", lambda event: root.attributes("-fullscreen",True))
root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))

L1 = Label(root, text="MileCode :- ", font=("bold", 40, )).grid(row=0,column=0,pady=20)
Label(root, text="\tAvailabe Options :- (Click to Choose)").grid(row=1,column=0,sticky=W,pady=10)
Button(root,text="1) Refresh Code, if you have made any changes to excel").grid(row=2,column=0,sticky=W,pady=5,padx=20)
Button(root,text='2) Get current Price of Product?').grid(row=3,column=0,sticky=W,pady=5,padx=20)
Button(root,text="3) Get Price of Product at particular date?").grid(row=4,column=0,sticky=W,pady=5,padx=20)
Button(root,text='4) Get all price details of Product?').grid(row=5,column=0,sticky=W,pady=5,padx=20)
Button(root,text='5) Get initial price of Product?').grid(row=6,column=0,sticky=W,pady=5,padx=20)
Button(root,text='6) Get current prices of all Product?').grid(row=7,column=0,sticky=W,pady=5,padx=20)
Button(root,text='7) Get prices of all Product at particular date?').grid(row=8,column=0,sticky=W,pady=5,padx=20)
Button(root,text='8) Get initial prices of all Product?').grid(row=9,column=0,sticky=W,pady=5,padx=20)
Button(root,text='9) Get Date at which a particular product price was changed to some new price?').grid(row=10,column=0,sticky=W,pady=5,padx=20)
Button(root,text='10) Exit').grid(row=11,column=0,sticky=W,pady=5,padx=20)

root.mainloop()
