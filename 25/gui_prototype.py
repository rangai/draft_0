from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Button, Style

class PrimitiveBC_Gui(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.protocol('WM_DELETE_WINDOW', self.quit)
        self.coin_balance = StringVar(self.parent, '0')
        self.status_message = StringVar(self.parent, 'No coin to be sent')
        self.initApp()
        self.setupGUI()

    def quit(self, event=None):
        self.parent.destroy()

    def initApp(self):
        print('SimpleBitcoin is now activating ...: ')
      

    def display_info(self, info):
        pass

    def update_status(self, info):
        self.status_message.set(info)

    def update_balance(self):
        pass

    def create_menu(self):
        top = self.winfo_toplevel()
        self.menuBar = Menu(top)
        top['menu'] = self.menuBar

        self.subMenu = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label='Menu', menu=self.subMenu)
        self.subMenu.add_command(label='Show My Address', command=self.show_my_address)
        self.subMenu.add_command(label='Load my Keys', command=self.load_my_keys)
        self.subMenu.add_command(label='Update Blockchain', command=self.update_block_chain)
        self.subMenu.add_separator()
        self.subMenu.add_command(label='Quit', command=self.quit)

        self.subMenu2 = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label='Settings', menu=self.subMenu2)
        self.subMenu2.add_command(label='Renew my Keys', command=self.renew_my_keypairs)
        self.subMenu2.add_command(label='Connection Info', command=self.edit_conn_info)

        self.subMenu3 = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label='Advance', menu=self.subMenu3)
        self.subMenu3.add_command(label='Show logs', command=self.open_log_window)
        self.subMenu3.add_command(label='Show Blockchain', command=self.show_my_block_chain)

    
    def show_my_address(self):
        pass
    
    def load_my_keys(self):
        pass    

    def update_block_chain(self):
        pass
        
    def renew_my_keypairs(self):
        pass
        
    def edit_conn_info(self):
        pass

    def open_log_window(self):
        pass
        
    def show_my_block_chain(self):
        pass
  
    def setupGUI(self):
        self.parent.bind('<Control-q>', self.quit)
        self.parent.title("PrimitiveBC GUI")
        self.pack(fill=BOTH, expand=1)

        self.create_menu()

        lf = LabelFrame(self, text='Current Balance')
        lf.pack(side=TOP, fill='both', expand='yes', padx=7, pady=7)

        lf2 = LabelFrame(self, text='')
        lf2.pack(side=BOTTOM, fill='both', expand='yes', padx=7, pady=7)
    
        self.balance = Label(lf, textvariable=self.coin_balance, font='Helvetica 20')
        self.balance.pack()

        # Recipient Address
        self.label = Label(lf2, text='Recipient Address:')
        self.label.grid(row=0, pady=5)

        self.recipient_pubkey = Entry(lf2, bd=2)
        self.recipient_pubkey.grid(row=0, column=1, pady=5)

        # Amount to pay
        self.label2 = Label(lf2, text='Amount to pay :')
        self.label2.grid(row=1, pady=5)
    
        self.amountBox = Entry(lf2, bd=2)
        self.amountBox.grid(row=1, column=1, pady=5, sticky='NSEW')

        # Fee
        self.label3 = Label(lf2, text='Fee (Optional) :')
        self.label3.grid(row=2, pady=5)
    
        self.amountBox2 = Entry(lf2, bd=2)
        self.amountBox2.grid(row=2, column=1, pady=5, sticky='NSEW')

        self.label4 = Label(lf2, text='')
        self.label4.grid(row=3, pady=5)

        # Send Coin(s)
        self.sendBtn = Button(lf2, text='\nSend Coin(s)\n', command=self.sendCoins)
        self.sendBtn.grid(row=4, column=1, sticky='NSEW')

        stbar = Label(self.winfo_toplevel(), textvariable=self.status_message, bd=1, relief=SUNKEN, anchor=W)
        stbar.pack(side=BOTTOM, fill=X)
  
    def sendCoins(self):
        pass
 
def main():
    root = Tk()
    app = PrimitiveBC_Gui(root)
    root.mainloop()

if __name__ == '__main__':
    main()