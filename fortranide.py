from tkinter import*
from tkinter import filedialog
import os
import time
import pathlib
import shutil
from tkinter import colorchooser
import selenium
from selenium import webdriver
from tkinter import messagebox
a=Tk()
k=""
s2=""
a.title("Fortran ide")	
a.option_add("*tearOff", False)
e=Text(width=120,height=180)


m=Menu()
m1=Menu()
def save_file():
 global k
 a=filedialog.asksaveasfilename(title="Save fortran file",filetypes=[("fortran file",("*.for","*.f","*.f90","*.f95","*.f08"))])
 if a!="":
  k=a
  c=open(a,"w")
  text_file=e.get('1.0',END)
  c.write(text_file)
def open_file():
    global k
    a=filedialog.askopenfilename(title="Open fortran file",filetypes=[("fortran file",("*.for","*.f","*.f90","*.f95","*.f08"))])
    k=a
    if a!="":
     c=open(a,"r") 
     text=c.read()
     e.delete("1.0",END)
     e.insert("1.0",text)
def new_file():
    global k
    words="Hello Fortran"
    j=f"program hello\n!create:{time.asctime()}\nimplicit none\nwrite(*,*) '{words}'\nend program"
    e.delete("1.0",END)
    e.insert("1.0",j)
    a=filedialog.asksaveasfilename(title="New fortran file",filetypes=[("fortran file",("*.for","*.f","*.f90","*.f95","*.f08"))])
    k=a
    c=open(a,"w")
    print(k)
    text_file=e.get('1.0',END)
    c.write(text_file)
def run_file():
    program="program"
    a2=filedialog.askopenfilename(title="Run fortran file",filetypes=[("fortran file",("*.for","*.f","*.f90","*.f95","*.f08"))])
    os.system(f"gfortran {a2} -o {program}")
    os.system(f"{program}.exe")
    os.remove(f"{program}.exe")

def compile_file():
    global s2
    words="program"
    s1=filedialog.askopenfilename(title="Compile fortran file",filetypes=[("fortran file",("*.for","*.f","*.f90","*.f95","*.f08"))])
    s2+=s1
    filee = os.path.realpath(__file__)
    direct1 = str(os.path.dirname(filee))+"\program.exe"
    s4=str(pathlib.Path(s1).name)
    direct2=s1.replace(s4,"program.exe")
    os.system(f"gfortran {s1} -o {words}")
    shutil.move(direct1,direct2)
    print("Compile  end")
def save_edit():
 c=open(k,"w")
 text_file=e.get('1.0',END)
 c.write(text_file)
def delete():
    e.delete('1.0',END)
def new_temp():
     words="Hello"
     j=f"program hello\n!create:{time.asctime()}\nimplicit none\nwrite(*,*) '{words}'\nend program"
     e.delete('1.0',END)
     e.insert('1.0',j)
def cursor_file():
 result =colorchooser.askcolor(initialcolor="black",title="color cursor")
 e["insertbackground"] = result[1]
def back_file():
 result =colorchooser.askcolor(initialcolor="black",title="color background")
 e["background"] = result[1]   
def fore_file():
 result =colorchooser.askcolor(initialcolor="black",title="color text")
 e["foreground"] = result[1]   
def font_file1(font):
    e["font"]=font
def font_file():
    a.tk.call("tk", "fontchooser", "configure", "-font", e["font"], "-command", a.register(font_file1))
    a.tk.call("tk", "fontchooser", "show")
def f_file():
    ach=webdriver.Edge()
    ach.get("https://fortran-lang.org/learn/")
def info():
    messagebox.showwarning("Program is not product","offical Fortran")

m18=Menu()
m19=Menu()
m19.add_command(label="delete",command=delete)
m18.add_cascade(label="Save edit",command=save_edit)
m1.add_command(label="Save",command=save_file)
m1.add_command(label="Open",command=open_file)
m1.add_command(label="New",command=new_file)
m2=Menu()
m20=Menu()
m30=Menu()
m31=Menu()
m32=Menu()
m33=Menu()
m33.add_command(label="info program",command=info)
m32.add_command(label="check of. documentation fortran",command=f_file)
m31.add_command(label="font",command=font_file)
m30.add_command(label="cursor",command=cursor_file)
m30.add_command(label="background",command=back_file)
m30.add_command(label="foreground",command=fore_file)
m20.add_command(label="new template",command=new_temp)
m2.add_command(label="Run",command=run_file)
m2.add_command(label="Compile",command=compile_file)
m.add_cascade(label="File",menu=m1)
m.add_cascade(label="Compile or Run",menu=m2)
m.add_cascade(label="Edit",menu=m18)
m.add_cascade(label="delete",menu=m19)
m.add_cascade(label="new template",menu=m20)
m.add_cascade(label="color",menu=m30)
m.add_cascade(label="font",menu=m31)
m.add_cascade(label="help ",menu=m32)
m.add_cascade(label="info",menu=m33)
l=Scrollbar(orient="vertical",command=e.yview)
l.pack(side=RIGHT,fill=Y)
e.pack(fill=BOTH)
e["yscrollcommand"]=l.set
a.config(menu=m)
a.mainloop()