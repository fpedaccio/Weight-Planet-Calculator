# Planet weight calculator by Facundo Pedaccio

#The program is capable of calculating the weight that the user enters on any planet in the solar system and some of its moons.
#We use the weight of the user on the earth (in KGf), which is equal to the mass of that body,
#to calculate gravity based on the formula
#Weight (in Newtons) = mass (in KG) * gravitational acceleration of the chosen planet (in m * s ^ 2).
#All this accompanied by a nice and nerdy user interface,
#which also includes some friendly reminders about physics. Like the meaning of weight and mass.


from tkinter import *
from tkinter import ttk



# User Interface (GUI)
ventana = Tk()
peso = IntVar()
planeta = StringVar()
res = StringVar()
ventana.geometry("1000x700")
ventana.title("How much would I weight in? APP")
ventana.iconbitmap("C:\guiplanetas\planet.ico")
gui = PhotoImage(file="C:\guiplanetas\gui.png")
guiplace = Label(ventana, image=gui)
guiplace.place(x=0, y=0, relwidth=1, relheight=1)


# Calculate weight function: based on W = m*g
# W = Weight, m = Mass, g = gravitational acceleration



#Calculate function
def calculate(selection):
    """Calculates the weight on selected planet where selection refers to the planeta(combobox) selection.
        Conditional at the start of the function catches exceptions on user input.
        g is reference to the g of selected planet which is declared while creating the class"""
    if peso == 0 or selection == -1:
        return 
    else:
        try:
            mass = peso.get()/9.8
            g = (eval(selection)).g
            res.set(str(mass*g))
        except:
            res.set("Invalid input for weight")

#Class body - to create object body(panet/moon) with the English name of the planet, g and a function language
#to add names of the bodies in alternate language
class body:
    bodies_list = []
    
    def __init__(self,name,g):
        self.g = g
        self.bodies_list.append(self)
        self.names = {"English": name}

    def language(self,language,name):
        self.names[language] = name

#Create all bodies here. English name and g are the only mandatory requirements. 
#Names in other languages can be added to the body by using body.language(language,name) function
Moon = body("Moon",1.62)
Mars = body("Mars",3.7)
Jupiter = body("Jupiter",24.79)
Saturan = body("Saturan",10.74)
Mercury = body("Mercury",3.70)
Venus = body("Venus",8.87)
Uranus = body("Uranus",8.87)
Npetune = body("Neptune",11.15)
Europa = body("Europa",1.31)

#Example of adding name to a body in alternate language
Mars.language("Spanish","Marte")

#Function to get bodies' names
def names(language):
    """Use this function to get the names of planets in a specified language that is to be used in the combobox options.
        If the specified language is not found or the name of one/some planets do not exist in that language,
        """
    returnlist = []
    for i in body.bodies_list:
        if language in i.names.keys():
            returnlist.append(i.names.get(language))
        else:
            returnlist.append(i.names.get("English"))
    return tuple(returnlist)
    
# Saving user inputs into variables. Peso = Weight, planeta = planet
peso = IntVar()
planeta = StringVar()

# Result variable
res = StringVar()


# Used fonts
fontentry= ("Montserrat", 15, "bold")
fontbuttom= ("Montserrat", 10, "bold")
fontresult = ("Montserrat", 20, "bold")


# Entry boxes
pesoentry = Entry(ventana, justify="center", font=(fontentry), bd=0,textvariable=peso)
pesoentry.place(x=285,y=253, width=370, height=37)

planeta = ttk.Combobox(ventana,justify="center", font=(fontentry),textvariable=planeta)
planeta.place(x=256,y=352,width=450, height=38)

#Add the list of planets to the options in Combobox
 
planeta['values'] = names("Spanish")


# Result Label
textoR = Label(ventana,textvariable=res,font=(fontresult), bd=0, bg="alice blue", fg="black")
textoR.place(x=650,y=515)

# Calculate button
boton = Button(ventana,text="Calculate",command=lambda: calculate(planeta.get()),bg="white",fg="black", bd=0, font=(fontbuttom))
boton.place(x=433,y=453)
ventana.mainloop()
