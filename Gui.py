# GUI 
import tkinter as tk
import one_time_pad
import caesar
import transpos
import affine
import vign
import time
#import tk
all_ciphers = [caesar,transpos,affine,vign,one_time_pad]

class Window(tk.Frame):
    def __init__(self,master,*args,**kwargs):
        tk.Frame.__init__(self,master,*args,**kwargs)
        self.pack(fill = 'both',expand = 1)
        self.top = master
        self.ciphers = {"Caesar Cipher":0,"Transposition Cipher":1,"Affine Cipher":2,"Vigneire Cipher":3,"One-Time Pad":4}
        self.modes = {1:"encrypted",0:"decrypted"}
        self.choice = tk.StringVar()
        self.choice.set('Caesar Cipher')
        self.output = tk.StringVar()
        self.output.set(self.choice.get())
        self.output.set("Using Cipher "+self.output.get())
        self.gen_key_mode = tk.BooleanVar()
        self.gen_key_mode.set(0)
        self.info = tk.StringVar()
        self.info.set("Select Cipher")
        
        
        self.logo_frame = tk.Frame(self, bg = "white",bd = 2)
        self.logo_frame.grid(row = 0, column = 0, columnspan = 2,sticky = tk.W+tk.S+tk.N+tk.E )
        self.logo_label = tk.Label(self.logo_frame,text = "KRYPTO",font = ('REMPONK',30),height = 5,width = 50)
        self.logo_label.pack(fill=tk.X, expand = 1)
        self.logo_frame.grid(row = 0, column = 0, columnspan = 2)
        
        self.selection_frame = tk.Frame(self,height = 50, width = 350,  bg = "white", relief = tk.SUNKEN, bd = 2)
        self.selection_frame.grid (row = 1, column = 0,sticky = tk.W)
        self.selection_label = tk.Label(self.selection_frame,text = "Select a \ncipher", bg = 'white',fg = 'black',bd = 3,width = 30)
        self.selection_label.pack(side = tk.LEFT)
        self.selection_scrollbar = tk.Scrollbar(self.selection_frame, orient = 'vertical')
        self.selection_list = tk.Listbox(self.selection_frame,width = 30,yscrollcommand = self.selection_scrollbar.set, relief = tk.GROOVE, selectbackground = 'purple', highlightcolor = 'purple', height = 2)
        for i in self.ciphers:
            if i in ["One-Time Pad","Simple RSA encryption"]:
                self.selection_list.insert(self.ciphers[i],tk.Radiobutton(self.selection_list,justify = tk.LEFT,command = self.set_gen_key,text = i,variable = self.choice,selectcolor = 'purple',value = i).pack())
            else:
                self.selection_list.insert(self.ciphers[i],tk.Radiobutton(self.selection_list,justify = tk.LEFT,command = self.set_gen_key,text = i,selectcolor = 'purple',variable =self.choice, value = i).pack())
            
                
        self.selection_scrollbar.config(command = self.selection_list.yview)
        self.selection_scrollbar.pack(side = tk.RIGHT, fill = "y")
        self.selection_list.pack(fill = 'y', expand = 1)
        
        
        self.process_sel_frame = tk.Frame(self,height = 100, width = 300, bg = "green", relief = tk.RAISED, bd = 5)
        self.process_sel_frame.grid(row = 2, column = 0,sticky = tk.W)
        '''IM'''
        self.mode = tk.IntVar()
        self.encrypt_radio = tk.Radiobutton(self.process_sel_frame,value = 1,selectcolor = "blue",variable = self.mode,text = "Encrypt",padx = 150,command = self.set_input_label)
        self.encrypt_radio.pack()
        self.decrypt_radio = tk.Radiobutton(self.process_sel_frame,value = 0,selectcolor = "red",variable = self.mode,text = "Decrypt",padx = 150, command = self.set_input_label)
        self.decrypt_radio.pack()
        
#        self.input_frame_2 = tk.Frame(self,height =100, width = 550, bg = "red", relief = tk.GROOVE, bd = 5)
#        self.input_frame_2.grid(row = 1, column = 1,sticky = tk.N+tk.W+tk.E)
        self.info_frame = self.process_sel_frame = tk.Frame(self,height = 100, width = 300, bg = "black", relief = tk.RAISED, bd = 5)
        self.info_frame.grid(row = 3, column = 0)
        self.info_label = tk.Label(self.info_frame, textvariable = self.info,fg = "cyan",bg = "black",height = 10, width = 50)
        self.info_label.pack(fill = 'both')
        
        
        
        
        
        
        self.input_frame = tk.Frame(self, height =100, width = 550, bg = "red", relief = tk.GROOVE, bd = 5)
        self.input_frame.grid(row = 1, column = 1,sticky = tk.N+tk.W+tk.E)
        self.inp_var = tk.StringVar()
        self.input_display = tk.Label(self.input_frame,text = "Enter text to be decrypted:",width = 40 )
        self.input_display.grid(row = 0, column = 0)
        self.input_entry = tk.Entry(self.input_frame, bd = 3)
        self.input_entry.grid(row = 0, column = 1,sticky = tk.E+tk.W)
        self.input_key_label = tk.Label(self.input_frame, text = "Enter Key: ")
        self.input_key_label.grid(row = 1,column = 0)
        self.key_entry = tk.Entry(self.input_frame,bd = 3)
        self.key_entry.grid(row =1,column = 1,sticky = tk.W+tk.E)
        self.gen_key_button = tk.Button(self.input_frame,state = "normal", text = "Generate Key",relief = tk.GROOVE,command = self.gen_key, bg = "purple")
        self.gen_key_button.grid(row = 3,column = 1)
        self.gen_key_label = tk.Label(self.input_frame,text = "Option not available for this cipher",bg = "black",fg ="yellow")
        self.gen_key_label.grid(row = 3, column = 0, sticky = tk.E+tk.W)
        
        self.button_frame = tk.Frame(self, height = 100, width = 250, bg = "purple", relief = tk.GROOVE, bd = 5)
        self.button_frame.grid(row = 2, column = 1)
        self.submit_button = tk.Button(self.button_frame, text = 'SUBMIT', relief = tk.GROOVE, bd = 3, bg = 'white', fg = 'black', command = self.submit_press)
        self.submit_button.pack(side = tk.LEFT)
        self.quit_button = tk.Button(self.button_frame,text = "QUIT",command = self.top.destroy)
        self.quit_button.pack(side =tk.RIGHT)
        
        self.output_frame = tk.Frame(self,height = 200, bg = 'black', relief = tk.RAISED, bd = 3)
        self.output_frame.grid(row = 3, column = 1)
        self.output_display = tk.Entry(self.output_frame,exportselection = 1,textvariable = self.output,fg = 'black',bg = 'black',state='readonly')
        self.output_display.pack()
        
    
    def get_choice(self):
        print(self.choice.get())
        print(int(self.mode.get()))
        print(self.output.get())
        #print((one_time_pad.encrypt(self.input_entry.get(),self.key_entry.get())))
    def set_input_label(self):
        self.input_display.config(text = "Enter Text to be "+self.modes[self.mode.get()]+":")

    def gen_key(self):
        if (self.choice.get()=="Simple RSA encryption"):
            pass
        elif(self.choice.get()=="One-Time Pad"):
            k = one_time_pad.generate_key(self.input_entry.get())
            tp = tk.Tk()
            tp.title('KEY')
            tp1 = tk.Text(tp)
            tp1.insert(tk.INSERT,k)
            tp1.pack()
            tk.Button(tp,text = 'OK',command = tp.destroy).pack()
    def key_check(self):
        pass
            
    def set_gen_key(self):
        if(self.choice.get() in ["One-Time Pad","Simple RSA encryption"]) and self.mode.get()==1:
            self.gen_key_button.config(state="normal")
            self.gen_key_label.config(text = "Press to generate random key")
        else:
            self.gen_key_button.config(state="disabled")
            self.gen_key_label.config(text ="Option not available for this cipher")
    def do_process(self):
        
        mode = int(self.mode.get())
        print(type(mode))
        cipher = self.choice.get()
        a = all_ciphers[self.ciphers[cipher]]
        if(mode==1):
            
            self.output.set(a.encrypt(self.input_entry.get(),(self.key_entry.get())))
        else:
            self.output.set(a.decrypt(self.input_entry.get(),(self.key_entry.get())))
        self.get_choice()
    def submit_press(self):
        if self.key_check():
            pass
        else:
            l = []
            l.append("Using cipher "+self.choice.get())
            self.info.set('...\n'.join(l))
            #time.sleep(2)
            l.append("Using key "+self.key_entry.get())
            self.info.set('...\n'.join(l))
            #time.sleep(2)
            l.append("Processing..")
            self.info.set('...\n'.join(l))
            #time.sleep(2)
            l.append("@")
            for i in range(10):
                l[3]="$"
                self.info.set('...\n'.join(l))
                #time.sleep(1)
                l[3]="@"
                self.info.set('...\n'.join(l))
            self.do_process()
            l.append("OUTPUT is :"+self.output.get())
            l.append("To copy output, please use the adjacent cell")
            self.info.set('...\n'.join(l))
            
            
            
            
            
        
            
        
        

root = tk.Tk()
app = Window(root, bg= "gray")
root.mainloop()
