#Lab 2 (part 2)
# student name:   Seiya Nozawa-Temchenko
# student number: 34838482

from __future__ import annotations  #helps with type hints
from tkinter import *
#do not import any more modules

#do not change the skeleton of the program. Only add code where it is requested. 
class Complex:
    """ 
        this class implements the complex number type 
        it stores the complex number in its lowest from
        two data fields: 
            real and imaginary
            (real stores the sign of the complex)
        Operation: 
            add, subtract, multiply and divide
            toString
    """
    def __init__(self, real: float, imaginary: float) -> None:
        """ initializer stores the complex number """ 
        self.real = real #Re(C)
        self.imaginary = imaginary #Im(C)
    
    def add(self, secondComplex: Complex) -> Complex:
        """
           adds 'this' complex to secondComplex
           returns the result as a complex number (type Complex)
        """    
        #(a+c) + j(b+d)
        re = self.real + secondComplex.real
        im = self.imaginary + secondComplex.imaginary

        return Complex(re, im)
    
    def subtract(self, secondComplex: Complex) -> Complex:
        """
           subtracts secondComplex from 'this' complex to 
           returns the result as a complex number (type Complex)
        """ 
        #(a-c) + j(b-d)
        re = self.real - secondComplex.real
        im = self.imaginary - secondComplex.imaginary

        return Complex(re, im)

    def multiply(self, secondComplex: Complex) -> Complex:
        """
           multiplies 'this' complex to secondComplex
           returns the result as a complex number (type Complex)
        """ 
        #(ac-bd) + j(ad+bc)
        re = self.real * secondComplex.real - self.imaginary * secondComplex.imaginary
        im = self.imaginary * secondComplex.real + self.real * secondComplex.imaginary

        return Complex(re, im)

    def divide(self, secondComplex: Complex) -> Complex:
        """
           divides 'this' complex by secondComplex
           returns the result as a complex number (type Complex)
        """ 
        #[(ac+bd) + j(ad-bc)] / (c^2 + d^2)
        divisor = secondComplex.real ** 2 + secondComplex.imaginary ** 2

        if divisor == 0: #divide by 0 error
            return Complex(float('nan'), float('nan'))
        
        if ((self.real * secondComplex.real + self.imaginary * secondComplex.imaginary) / divisor).is_integer: #avoid unneccessary decimals (1.0 -> 1)
            re = int((self.real * secondComplex.real + self.imaginary * secondComplex.imaginary) / divisor)
        else: 
            re = (self.real * secondComplex.real + self.imaginary * secondComplex.imaginary) / divisor
        
        if ((self.imaginary * secondComplex.real + self.real * secondComplex.imaginary) / divisor).is_integer:
            im = int((self.imaginary * secondComplex.real + self.real * secondComplex.imaginary) / divisor)
        else: 
            im = (self.imaginary * secondComplex.real + self.real * secondComplex.imaginary) / divisor

        return Complex(re, im)

    def toString(self) -> str:
        """             
            returns a string representation of 'this' complex
            the general output format is: real + imaginary i
            especial cases:
                if 'this' imaginary is 0, it must not show any imaginary
                if 'this' real is 0, it must not show any real 
                if imaginary is 1 or -1, it must show +i or -i
                if real or the imaginary is NaN, it returns "NaN"
        """ 
        if any([
            isinstance(self.real, float) and self.real != self.real, #check nan for real
            isinstance(self.imaginary, float) and self.imaginary != self.imaginary, #check nan for imaginary
        ]):
            return "NaN"
        
        output = "" #initialize empty string
            
        if self.real != 0:
            output += f"{self.real}" #real calculation
        if self.imaginary != 0:
            if self.imaginary > 0 and self.real != 0:
                output += " + " #positive imaginary and real is nonzero
            elif self.imaginary < 0 and self.real != 0:
                output += " - "  #negative imaginary and real is nonzero
            elif self.imaginary < 0 and self.real == 0:
                output += "-"  #negative imaginary and real is 0 (erase empty spaces)
            
            abs_im = abs(self.imaginary) #take absolute value as "-" is already appended
            
            if abs_im == 1:
                output += "i" #don't do 1i
            else:
                output += f"{abs_im}i" #don't do -1i
        
        if self.real == 0 and self.imaginary == 0:
            return "0" #return 0 for 0 real and 0 imaginary
        
        return output

class GUI:
    """ 
        this class implements the GUI for our program
        use as is.
        The add, subtract, multiply and divide methods invoke the corresponding
        methods from the Complex class to calculate the result to display.
    """
    def __init__(self):
        """ 
            The initializer creates the main window, label and entry widgets,
            and starts the GUI mainloop.
        """
        window = Tk()
        window.title("Complex Numbers")
        window.geometry("190x180")
       
        # Labels and entries for the first complex number
        frame1 = Frame(window)
        frame1.grid(row = 1, column = 1, pady = 10)
        Label(frame1, text = "Complex 1:").pack(side = LEFT)
        self.complex1Real = StringVar()
        Entry(frame1, width = 5, textvariable = self.complex1Real, 
              justify = RIGHT, font=('Calibri 13')).pack(side = LEFT)
        Label(frame1, text = "+").pack(side = LEFT)
        self.complex1Imaginary = StringVar()
        Entry(frame1, width = 5, textvariable = self.complex1Imaginary, 
              justify = RIGHT, font=('Calibri 13')).pack(side = LEFT)
        Label(frame1, text = "i").pack(side = LEFT)
        
        # Labels and entries for the second complex number
        frame2 = Frame(window)
        frame2.grid(row = 3, column = 1, pady = 10)
        Label(frame2, text = "Complex 2:").pack(side = LEFT)
        self.complex2Real = StringVar()
        Entry(frame2, width = 5, textvariable = self.complex2Real, 
              justify = RIGHT, font=('Calibri 13')).pack(side = LEFT)
        Label(frame2, text = "+").pack(side = LEFT)
        self.complex2Imaginary = StringVar()
        Entry(frame2, width = 5, textvariable = self.complex2Imaginary, 
              justify = RIGHT, font=('Calibri 13')).pack(side = LEFT)
        Label(frame2, text = "i").pack(side = LEFT)
        
        # Labels and entries for the result complex number
        # an entry widget is used as the output here
        frame3 = Frame(window)
        frame3.grid(row = 4, column = 1, pady = 10)
        Label(frame3, text = "Result:     ").pack(side = LEFT)
        self.result = StringVar()
        Entry(frame3, width = 10, textvariable = self.result, 
              justify = RIGHT, font=('Calibri 13')).pack(side = LEFT)

        # Buttons for add, subtract, multiply and divide
        frame4 = Frame(window) # Create and add a frame to window
        frame4.grid(row = 5, column = 1, pady = 5, sticky = E)
        Button(frame4, text = "Add", command = self.add).pack(
            side = LEFT)
        Button(frame4, text = "Subtract", 
               command = self.subtract).pack(side = LEFT)
        Button(frame4, text = "Multiply", 
               command = self.multiply).pack(side = LEFT)
        Button(frame4, text = "Divide", 
               command = self.divide).pack(side = LEFT)
               
        mainloop()
        
    def add(self): 
        (complex1, complex2) = self.getBothComplex()
        result = complex1.add(complex2)
        self.result.set(result.toString())
    
    def subtract(self):
        (complex1, complex2) = self.getBothComplex()
        result = complex1.subtract(complex2)
        self.result.set(result.toString())
    
    def multiply(self):
        (complex1, complex2) = self.getBothComplex()
        result = complex1.multiply(complex2)
        self.result.set(result.toString())
    
    def divide(self):
        (complex1, complex2) = self.getBothComplex()
        result = complex1.divide(complex2)
        self.result.set(result.toString())

    def getBothComplex(self):
        """ Helper method used by add, subtract, multiply and divide methods """
        try:
            real1 = eval(self.complex1Real.get())
            imaginary1 = eval(self.complex1Imaginary.get())
            complex1 = Complex(real1, imaginary1)

            real2 = eval(self.complex2Real.get())
            imaginary2 = eval(self.complex2Imaginary.get())
            complex2 = Complex(real2, imaginary2)
            return (complex1, complex2)
        except:
            return(Complex(float('nan'), float('nan')), Complex(float('nan'), float('nan'))) #if an entry value is missing, cause NaN

if __name__ == "__main__": GUI()