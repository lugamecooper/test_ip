import tkinter
import main
class main_client:
    def __init__(self) -> None:
        self.fen = tkinter.Tk("client ip",className="client ip")
        self.fen.geometry(f"{self.fen.winfo_screenwidth()}x{self.fen.winfo_screenheight()}")
        
        self.div_input = tkinter.Frame(self.fen)
        self.div_input_2 = tkinter.Frame(self.div_input)

        self.label_input = tkinter.Label(self.div_input_2,text="enter une ip :").pack(anchor="n")
        self.input = tkinter.Entry(self.div_input_2)
        self.input.pack(side="left")
        self.div_input_2.pack(side="top")
        self.button = tkinter.Button(master=self.div_input_2,text="validez",command=self.ip)
        self.button.pack(side="bottom")

        self.label_input_describe = tkinter.Label(self.div_input,text="ex : 192.168.0.1\nex : 192.168.0.1/24").pack()
        self.label_error = tkinter.Label(text="",master=self.div_input)
        self.label_error.pack(side="bottom")
        self.div_input.pack(anchor="n",side="left")


        self.div_affichage = tkinter.Frame(self.fen)
        
        self.affichage_sortie = tkinter.Listbox(self.fen,width=100,height=10)

        self.affichage_sortie.insert(1,f"mask_cidr          :: {None}")
        self.affichage_sortie.insert(2,f"mask_bin           :: {None}")
        self.affichage_sortie.insert(3,f"adress_class       :: {None}")
        self.affichage_sortie.insert(4,f"ipv4               :: {None}")
        self.affichage_sortie.insert(5,f"ipv4_bin           :: {None}")
        self.affichage_sortie.insert(6,f"ipv4_network       :: {None}")
        self.affichage_sortie.insert(7,f"ipv4_network_bin   :: {None}")
        self.affichage_sortie.insert(8,f"type_adress        :: {None}")
        self.affichage_sortie.insert(9,f"wilcard_mask       :: {None}")

        self.affichage_sortie.pack()
        self.div_affichage.pack(side="top",anchor="w")

        self.fen.mainloop()

    def ip(self):
        try:
            ip = main.IP(self.input.get())
            self.label_error.config(text="",fg="red")
            self.div_input.update()
            self.affichage_sortie.destroy()
            self.affichage_sortie = tkinter.Listbox(self.fen,width=100,height=10)
            self.affichage_sortie.insert(1,f"mask_cidr          :: {ip.mask_cidr}")
            self.affichage_sortie.insert(2,f"mask_bin           :: {ip.mask_bin}")
            self.affichage_sortie.insert(3,f"adress_class       :: {ip.adress_class}")
            self.affichage_sortie.insert(4,f"ipv4               :: {ip.ipv4}")
            self.affichage_sortie.insert(5,f"ipv4_bin           :: {ip.ipv4_bin}")
            self.affichage_sortie.insert(6,f"ipv4_network       :: {ip.ipv4_network}")
            self.affichage_sortie.insert(7,f"ipv4_network_bin   :: {ip.ipv4_network_bin}")
            self.affichage_sortie.insert(8,f"type_adress        :: {ip.type_adress}")
            self.affichage_sortie.insert(9,f"wilcard_mask       :: {ip.wilcard_mask}")
            self.affichage_sortie.pack()
            self.div_affichage.update()
        except Exception as er:
            self.label_error.config(text=er,fg="red")
            self.div_input.update()

main_client()