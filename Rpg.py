import tkinter as tk
import random
ordi = (0, 1, 2)
#0=attaque 1=soin 2=defense
fenetre = tk.Tk()
fenetre.title("Rpg")
fenetre.geometry("400x300")

frame_haut = tk.Frame(fenetre)
frame_haut.pack(fill="x")
frame_gauche = tk.Frame(frame_haut)
frame_gauche.pack(side="left", padx=10)
frame_droite = tk.Frame(frame_haut)
frame_droite.pack(side="right", padx=10)
label_titre = tk.Label(frame_haut, text="Rpg")
label_titre.pack(pady=5)
label_pv = tk.Label(frame_gauche, text="")
label_pv.pack(anchor="w")
label_magie = tk.Label(frame_gauche, text="")
label_magie.pack(anchor="w")
label_pv_ordi = tk.Label(frame_droite, text="")
label_pv_ordi.pack(anchor="e")
label_magie_ordi = tk.Label(frame_droite, text="")
label_magie_ordi.pack(anchor="e")
frame_boutons = tk.Frame(fenetre)
frame_boutons.pack(pady=40)   
frame_message = tk.Frame(fenetre)
frame_message.pack()
label_message = tk.Label(frame_message, text="", font=("Arial", 12, "bold"))
label_message.pack(pady=10)
defense_active_uti = False
defense_active_ordi=False
def reset_boutons():
    for widget in frame_boutons.winfo_children():
        widget.destroy()
def perso():
    robu = tk.Button(frame_boutons, text="Robuste", command=affec_robu)
    sorc = tk.Button(frame_boutons, text="Sorcier", command=affec_sorc)
    guer = tk.Button(frame_boutons, text="Guerrier", command=affec_guer)
    robu.pack(side="left", padx=5)
    sorc.pack(side="left", padx=5)
    guer.pack(side="left", padx=5)

def affec_robu():
    global choix
    choix = "Robuste"
    affectation()
def affec_sorc():
    global choix
    choix = "Sorcier"
    affectation()
def affec_guer():
    global choix
    choix = "Guerrier"
    affectation()
def affectation():
    global pv, magie, degat_uti, soin_uti, pv_uti, magie_uti
    if choix == "Robuste":
        pv_uti = 160
        magie_uti = 30
        degat_uti = 10
        soin_uti = 6
        pv = 160
        magie = 30
    elif choix == "Sorcier":
        pv_uti = 110
        magie_uti = 100
        degat_uti = 8
        soin_uti = 25
        pv = 110
        magie = 100
    elif choix == "Guerrier":
        pv_uti = 80
        magie_uti = 40
        degat_uti = 28
        soin_uti = 8
        pv = 80
        magie = 40
    niv()
def niv():
    reset_boutons()
    simp = tk.Button(frame_boutons, text="Niveau simple", command=ordi_simple)
    moy = tk.Button(frame_boutons, text="Niveau Moyen",command=ordi_moyen)
    hard = tk.Button(frame_boutons, text="Niveau Hard")
    simp.pack(side="left", padx=5)
    moy.pack(side="left", padx=5)
    hard.pack(side="left", padx=5)
###SIMPLE###
def ordi_simple():   
    global pv_ordi, magie_ordi, degat_ordi, soin_ordi,pv_or_di,mg_or_di
    pv_ordi = 120
    magie_ordi = 60
    degat_ordi = 15
    soin_ordi = 15
    pv_or_di=120
    mg_or_di=60
    simple()

def simple():
    label_pv.config(text=f"PV Joueur : {pv_uti}/{pv}")
    label_magie.config(text=f"Magie Joueur : {magie_uti}/{magie}")
    label_pv_ordi.config(text=f"PV Ordi : {pv_ordi}/{pv_or_di}")
    label_magie_ordi.config(text=f"Magie Ordi : {magie_ordi}/{mg_or_di}")    

    if pv_ordi>0 and pv_uti>0:
        reset_boutons()
        at = tk.Button(frame_boutons, text="Attaque",command=att_uti)
        mag = tk.Button(frame_boutons, text="Magie (soin)",command=mag_uti)
        defe = tk.Button(frame_boutons, text="Defense",command=def_uti)
        at.pack(side="left", padx=10)
        mag.pack(side="left", padx=10)
        defe.pack(side="left", padx=10)
        
    elif pv_uti<=0:
        reset_boutons()
        label_message.config(text="Perdu")

    elif pv_ordi<=0:
        reset_boutons()
        label_message.config(text="Victoire")    
def att_uti():
    reset_boutons()
    global pv_ordi, defense_active_ordi
    degat_uti_def=degat_uti
    if defense_active_ordi:
        degat_uti_def=degat_uti_def//2
        defense_active_ordi=False
    pv_ordi -= degat_uti_def
    label_message.config(text="Vous avez attaquer")
    confi = tk.Button(frame_boutons, text="Confirmer",command=tour_ordi)
    confi.pack(side="left", padx=10)

def mag_uti():
    reset_boutons()
    global pv_uti,magie_uti
    pv_uti+=soin_uti 
    magie_uti-=soin_uti
    label_message.config(text="Vous vous etes soigné")
    confi = tk.Button(frame_boutons, text="Confirmer",command=tour_ordi)
    confi.pack(side="left", padx=10)    
def def_uti():  
    reset_boutons()
    global defense_active_uti
    defense_active_uti = True
    label_message.config(text="Vous êtes en position de défense")
    confi = tk.Button(frame_boutons, text="Confirmer", command=tour_ordi)
    confi.pack(side="left", padx=10)

def tour_ordi():
    reset_boutons()
    global pv_uti, pv_ordi, magie_ordi
    global defense_active_uti, defense_active_ordi
    ale = random.choice(ordi)
    if ale==0:
        degats=degat_ordi
        if defense_active_uti:
            degats=degats//2
            defense_active_uti= False
    
        pv_uti-=degats
        label_message.config(text="Vous avez subis des degats")
        confi = tk.Button(frame_boutons, text="Confirmer",command=simple)
        confi.pack(side="left", padx=10)

    elif ale==1:
        if magie_ordi>0:
            pv_ordi+=soin_ordi
            magie_ordi-=soin_ordi
            label_message.config(text="L'ordi ce soigne ")
            confi = tk.Button(frame_boutons, text="Confirmer",command=simple)
            confi.pack(side="left", padx=10)
        else :
            label_message.config(text="L'ordi ne peux plus ce soigner ")
            confi = tk.Button(frame_boutons, text="Confirmer",command=simple)
            confi.pack(side="left", padx=10)
    elif ale==2:
        defense_active_ordi=True
        label_message.config(text="L'ordi ce met en position defense ")
        confi = tk.Button(frame_boutons, text="Confirmer",command=simple)
        confi.pack(side="left", padx=10)
    #Simple#



def ordi_moyen():

    global pv_ordi, magie_ordi, degat_ordi, soin_ordi,pv_or_di,mg_or_di
    if choix == "Robuste":
        pv_ordi = 170
        magie_ordi = 40
        degat_ordi = 14
        soin_ordi = 10
        pv_or_di=170
        mg_or_di=40
    elif choix == "Sorcier":
        pv_ordi = 130
        magie_ordi = 70
        degat_ordi = 12
        soin_ordi = 18
        pv_or_di=130
        mg_or_di=70 
    elif choix == "Guerrier":
        pv_ordi = 110
        magie_ordi = 50
        degat_ordi = 20
        soin_ordi = 12
        pv_or_di=110
        mg_or_di=50
    moyen()
def moyen():
    label_pv.config(text=f"PV Joueur : {pv_uti}/{pv}")
    label_magie.config(text=f"Magie Joueur : {magie_uti}/{magie}")
    label_pv_ordi.config(text=f"PV Ordi : {pv_ordi}/{pv_or_di}")
    label_magie_ordi.config(text=f"Magie Ordi : {magie_ordi}/{mg_or_di}")    

    if pv_ordi>0 and pv_uti>0:
        reset_boutons()
        at = tk.Button(frame_boutons, text="Attaque",command=att_moy_uti)
        mag = tk.Button(frame_boutons, text="Magie (soin)")
        defe = tk.Button(frame_boutons, text="Defense")
        at.pack(side="left", padx=10)
        mag.pack(side="left", padx=10)
        defe.pack(side="left", padx=10)
        
    elif pv_uti<=0:
        reset_boutons()
        label_message.config(text="Perdu")

    elif pv_ordi<=0:
        reset_boutons()
        label_message.config(text="Victoire")  
        
def att_moy_uti():
    print
perso()
fenetre.mainloop()