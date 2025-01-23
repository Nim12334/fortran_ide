from tkinter import*
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
import os
import time
import pathlib
import shutil
from tkinter import colorchooser
import selenium
from selenium import webdriver
from tkinter import messagebox
from pygments.lexers.fortran import FortranLexer
from pygments.token import Token
import subprocess
import sys
import threading
a=Tk()
k=""
s2=""
fjic=0
progress=0
lexer=FortranLexer()
a.title("Fortran ide")  
a.option_add("*tearOff", False)
e=Text(width=180,height=180)

def on_update(event):
    number.config(state=NORMAL)
    number.delete(1.0, "end")
    lines = e.get(1.0, "end").split("\n")
    for i, lines in enumerate(lines, 1):
        number.insert("end", str(i) + "\n")
    number.config(state=DISABLED)
e.bind("<KeyRelease>",on_update)
number=Text(width=4,height=4,wrap='word')
number.config(state=DISABLED)
e.tag_config("keyword", foreground='green')
e.tag_config("string_literal", foreground='red')
m=Menu()
m1=Menu()
def save_file():
 try:
  global k
  a=filedialog.asksaveasfilename(title="Save fortran file",filetypes=[("fortran file",("*.for","*.f","*.f90","*.f95","*.f08"))])
  if a!="":
   k=a
   c=open(a,"w")
   text_file=e.get('1.0',END)
   c.write(text_file)
 except:
    print("")
def open_file():
 try:
  global k
  a=filedialog.askopenfilename(title="Open fortran file",filetypes=[("fortran file",("*.for","*.f","*.f90","*.f95","*.f08"))])
  k=a
  if a!="":
    c=open(a,"r") 
    text=c.read()
    e.delete("1.0",END)
    e.insert("1.0",text)
 except:
    print("")
def new_file():
 try:
    global k
    words="Hello Fortran"
    j=f"program hello\n!create:{time.asctime()}\nimplicit none\nwrite(*,*) '{words}'\nend program"
    e.delete("1.0",END)
    e.insert("1.0",j)
    a=filedialog.asksaveasfilename(title="New fortran file",filetypes=[("fortran file",("*.for","*.f","*.f90","*.f95","*.f08"))])
    k=a
    c=open(a,"w")
    text_file=e.get('1.0',END)
    c.write(text_file)
 except:
    print("")
def run_file():

    program="file"
    os.system(f"gfortran {k} -o {program}")
    os.system(f"{program}.exe")
    os.remove(f"{program}.exe")
 



def compile_file():
 s1=filedialog.askopenfilename(title="Compile fortran file",filetypes=[("fortran file",("*.for","*.f","*.f90","*.f95","*.f08"))])
 try:
  global s2
  s2+=s1
  one=pathlib.Path(s1).name
  two=one.replace(".","")
  words=f"{two}"
  os.system(f"gfortran {s1} -o {words}")
  path=os.path.realpath("fortranide.exe")
  three="\e"
  throo=three.replace("e","")
  path1=os.path.dirname(path)+f"{throo}"+f"{words}.exe"
  s4=pathlib.Path(s1).name
  s5=s1.replace(s4,"")
  shutil.move(path1,s5)
  print("Compile end")
 except:
  s2+=s1
  one=pathlib.Path(s1).name
  two=one.replace(".","")
  words=f"{two}"
  os.system(f"gfortran {s1} -o {words}")
  path=os.path.realpath("fortranide.exe")
  three="\e"
  throo=three.replace("e","")
  path1=os.path.dirname(path)+f"{throo}"+f"{words}.exe"
  s4=pathlib.Path(s1).name
  s5=s1.replace(s4,"")
  os.remove(s5+f"{words}.exe")
  shutil.move(path1,s5)
  print("Compile  end")
  
def save_edit():
 try:
  c=open(k,"w")
  text_file=e.get('1.0',END)
  c.write(text_file)
 except:
  print("")
def delete():
    e.delete('1.0',END)
def new_temp():
     words="Hello Fortran"
     j=f"program hello\n!create:{time.asctime()}\nimplicit none\nwrite(*,*) '{words}'\nend program"
     e.delete('1.0',END)
     e.insert('1.0',j)


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
def new_temp1():
     words="Hello"
     j=f"program read1\n!create:{time.asctime()}\nimplicit none\nreal::x\nwrite(*,*) 'Please write value:'\nread(*,*) x\nprint*, x\nend program"
     e.delete('1.0',END)
     e.insert('1.0',j)
def new_temp2():
     j=f"program array1\n!create:{time.asctime()}\nimplicit none\ninteger::x(10)\nx=[1,2,3,4,5,6,7,8,9,10]\nprint*,x\nend program"
     e.delete('1.0',END)
     e.insert('1.0',j)
def new_temp3():
    j=f"program empty\n!Empty file create:{time.asctime()}\nend program"
    e.delete('1.0',END)
    e.insert('1.0',j)
def compile_file1():
 try:
  global s2
  global k
  s1=k
  s2+=s1
  one=pathlib.Path(s1).name
  two=one.replace(".","")
  words=f"{two}"
  os.system(f"gfortran {s1} -o {words}")
  path=os.path.realpath("fortranide.exe")
  three="\e"
  throo=three.replace("e","")
  path1=os.path.dirname(path)+f"{throo}"+f"{words}.exe"
  s4=pathlib.Path(s1).name
  s5=s1.replace(s4,"")
  shutil.move(path1,s5)
  print("Compile end")
 except:
  s1=k
  s2+=s1
  one=pathlib.Path(s1).name
  two=one.replace(".","")
  words=f"{two}"
  os.system(f"gfortran {s1} -o {words}")
  path=os.path.realpath("fortranide.exe")
  three="\e"
  throo=three.replace("e","")
  path1=os.path.dirname(path)+f"{throo}"+f"{words}.exe"
  s4=pathlib.Path(s1).name
  s5=s1.replace(s4,"")
  os.remove(s5+f"{words}.exe")
  shutil.move(path1,s5)
  print("Compile end")
number.pack(side="left",fill="y")
token_type_to_tag = {
  
     
    Token.Keyword: "keyword",
    Token.Operator.Word: "keyword",
    Token.Name.Builtin: "keyword",
    Token.Literal.String.Single: "string_literal",
    Token.Literal.String.Double: "string_literal",
    
   
}

def get_text_coord(s: str, i: int):
   
    for row_number, line in enumerate(s.splitlines(keepends=True), 1):
        if i < len(line):
            return f'{row_number}.{i}'
        
        i -= len(line)


def on_edit(event):
 
    for tag in e.tag_names():
        e.tag_remove(tag, 1.0, END)
    

    s = e.get(1.0, END)
    tokens = lexer.get_tokens_unprocessed(s)
    
    for i, token_type, token in tokens:
        j = i + len(token)
        if token_type in token_type_to_tag:
            e.tag_add(token_type_to_tag[token_type], get_text_coord(s, i), get_text_coord(s, j))

  
    e.edit_modified(0)
e.bind('<<Modified>>', on_edit)
def new_temp4():
 j=f"program if\n!if file create:{time.asctime()}\ninteger::n=12\nif (n<13) then\nprint *, 'n less than 13'\nelse\nprint *,'n more than 13'\nend if\nend program"
 e.delete('1.0',END)
 e.insert('1.0',j)
def dark_them():
    e["foreground"]="white"
    e["background"]="#1e1e1e"
    e["insertbackground"]="white"
    number["background"]="#1e1e1e"
    number["foreground"]="white"
    m["foreground"]="#1e1e1e"
def light_them():
    e["foreground"]="black"
    e["background"]="#fafafa"
    e["insertbackground"]="black"
    number["background"]="#fafafa"
    number["foreground"]="black"
def new_temp5():
  j=f"program while\n!File create:{time.asctime()}\ndo i=1,10\nprint*,i\nend do\nend program"
  e.delete('1.0',END)
  e.insert('1.0',j)
def f1_file():
 global progress
 if progress==0:
  m1=messagebox.askokcancel("new_template is responsible for","creating new ones templates")
 if m1:
  m2=messagebox.askokcancel("There are 6 of them ","in the current version")
 if m2:
  m3=messagebox.askokcancel("The File tab is responsible for","saving create new or open files")
 if m3:
  m4=messagebox.askokcancel("The Edit tab is responsible for","saving changed files")
 if m4:
  m5=messagebox.askokcancel("The Compile or run tab is responsible for","Compiling or running or debug files")
 if m5:
  m5=messagebox.askokcancel("Important to note","Compile needs to select a file")
  m5=messagebox.askokcancel("And in the Compile this file section","select file no need")
 if m5:
    m6=messagebox.askokcancel("Excellent well done","we looked at the main functions of ide")


def blue_them():
    e["foreground"]="white"
    e["background"]="#152238"
    e["insertbackground"]="white"
    number["background"]="#152238"
    number["foreground"]="white"
def green_them():
    e["foreground"]="white"
    e["background"]="#062315"
    e["insertbackground"]="white"
    number["background"]="#062315"
    number["foreground"]="white"
  




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
m32=Menu()
m33=Menu()
def debug_file1():

    subprocess.run(f"gfortran {k} -g")
    subprocess.run(f"gdb {k}.exe")
    threading.Thread(target=debug_file1)._stop()

def debug_file():
    threading.Thread(target=debug_file1).start()
def files_file1():
 try:
  global s2
  global k
  global fjic
  s1=k
  s2+=s1
  one=pathlib.Path(s1).name
  two=one.replace(".","")
  words=f"{two}"
  os.system(f"gfortran {s1} -o {words}")
  path=os.path.realpath("fortranide.exe")
  three="\e"
  throo=three.replace("e","")
  path1=os.path.dirname(path)+f"{throo}"+f"{words}.exe"
  s4=pathlib.Path(s1).name
  s5=s1.replace(s4,"")
  shutil.move(path1,s5)
  l=k.replace(one,f'{words}.exe')
 except:
  s1=k
  s2+=s1
  one=pathlib.Path(s1).name
  two=one.replace(".","")
  words=f"{two}"
  os.system(f"gfortran {s1} -o {words}")
  path=os.path.realpath("fortranide.exe")
  three="\e"
  throo=three.replace("e","")
  path1=os.path.dirname(path)+f"{throo}"+f"{words}.exe"
  s4=pathlib.Path(s1).name
  s5=s1.replace(s4,"")
  os.remove(s5+f"{words}.exe")
  shutil.move(path1,s5)
  l=k.replace(one,f'{words}.exe')
 os.system(f"{l}")
m30.add_command(label="Dark",command=dark_them)
m30.add_command(label="Light",command=light_them)
m30.add_command(label="Blue",command=blue_them)
m30.add_command(label="Green",command=green_them)
m33.add_command(label="info program",command=info)
m32.add_command(label="check of. documentation gfortran",command=f_file)
m32.add_command(label="help ide",command=f1_file)
m20.add_command(label="new template Hello Fortran",command=new_temp)
m20.add_command(label="new template read",command=new_temp1)
m20.add_command(label="new template array",command=new_temp2)
m20.add_command(label="new template empty",command=new_temp3)
m20.add_command(label="new template if",command=new_temp4)
m20.add_command(label="new template while",command=new_temp5)
m2.add_command(label="Run",command=run_file)
m2.add_command(label="Compile",command=compile_file)
m2.add_command(label="Compile this file",command=compile_file1)
m2.add_command(label="Debug",command=debug_file1)
m2.add_command(label="Compile & Run",command=files_file1)
m.add_cascade(label="File",menu=m1)
m.add_cascade(label="Compile or Run",menu=m2)
m.add_cascade(label="Edit",menu=m18)
m.add_cascade(label="delete",menu=m19)
m.add_cascade(label="new template",menu=m20)
m.add_cascade(label="themes",menu=m30)

m.add_cascade(label="help ",menu=m32)
m.add_cascade(label="info",menu=m33)

l=Scrollbar(orient="vertical",command=lambda *args:[e.yview(*args),number.yview(*args)])

l.pack(side=RIGHT,fill=Y)
e.pack(fill=BOTH)
number.config(yscrollcommand=l.set)
e.config(yscrollcommand=l.set)

def new_file1(event):
 try:
  global k
  words="Hello Fortran"
  j=f"program hello\n!create:{time.asctime()}\nimplicit none\nwrite(*,*) '{words}'\nend program"
  e.delete("1.0",END)
  e.insert("1.0",j)
  a=filedialog.asksaveasfilename(title="New fortran file",filetypes=[("fortran file",("*.for","*.f","*.f90","*.f95","*.f08"))])
  k=a
  c=open(a,"w")
  text_file=e.get('1.0',END)
  c.write(text_file)
 except:
    print("")
def save_file1(event):
 try:
  global k
  a=filedialog.asksaveasfilename(title="Save fortran file",filetypes=[("fortran file",("*.for","*.f","*.f90","*.f95","*.f08"))])
  if a!="":
   k=a
   c=open(a,"w")
   text_file=e.get('1.0',END)
   c.write(text_file)
 except:
    print("")
def open_file1(event):
 try:
  global k
  a=filedialog.askopenfilename(title="Open fortran file",filetypes=[("fortran file",("*.for","*.f","*.f90","*.f95","*.f08"))])
  k=a
  if a!="":
   c=open(a,"r") 
   text=c.read()
   e.delete("1.0",END)
   e.insert("1.0",text)
 except:
    print("")
def run_file1(event):
    program="file"
    os.system(f"gfortran {k} -o {program}")
    os.system(f"{program}.exe")
    os.remove(f"{program}.exe")
def compile_file2(event):
 s1=filedialog.askopenfilename(title="Compile fortran file",filetypes=[("fortran file",("*.for","*.f","*.f90","*.f95","*.f08"))])
 try:
  global s2
  s2+=s1
  one=pathlib.Path(s1).name
  two=one.replace(".","")
  words=f"{two}"
  os.system(f"gfortran {s1} -o {words}")
  path=os.path.realpath("fortranide.exe")
  three="\e"
  throo=three.replace("e","")
  path1=os.path.dirname(path)+f"{throo}"+f"{words}.exe"
  s4=pathlib.Path(s1).name
  s5=s1.replace(s4,"")
  shutil.move(path1,s5)
  print("Compile end")
 except:
  s2+=s1
  one=pathlib.Path(s1).name
  two=one.replace(".","")
  words=f"{two}"
  os.system(f"gfortran {s1} -o {words}")
  path=os.path.realpath("fortranide.exe")
  three="\e"
  throo=three.replace("e","")
  path1=os.path.dirname(path)+f"{throo}"+f"{words}.exe"
  s4=pathlib.Path(s1).name
  s5=s1.replace(s4,"")
  os.remove(s5+f"{words}.exe")
  shutil.move(path1,s5)
  print("Compile end")
def compile_file3(event):
 try:
  global s2
  global k
  s1=k
  s2+=s1
  one=pathlib.Path(s1).name
  two=one.replace(".","")
  words=f"{two}"
  os.system(f"gfortran {s1} -o {words}")
  path=os.path.realpath("fortranide.exe")
  three="\e"
  throo=three.replace("e","")
  path1=os.path.dirname(path)+f"{throo}"+f"{words}.exe"
  s4=pathlib.Path(s1).name
  s5=s1.replace(s4,"")
  os.remove(s5+f"{words}.exe")
  shutil.move(path1,s5)
  print("Compile end")
 except:
  s1=k
  s2+=s1
  one=pathlib.Path(s1).name
  two=one.replace(".","")
  words=f"{two}"
  os.system(f"gfortran {s1} -o {words}")
  path=os.path.realpath("fortranide.exe")
  three="\e"
  throo=three.replace("e","")
  path1=os.path.dirname(path)+f"{throo}"+f"{words}.exe"
  s4=pathlib.Path(s1).name
  s5=s1.replace(s4,"")
  shutil.move(path1,s5)
  print("Compile end")
def save_edit1(event):
 try:
  c=open(k,"w")
  text_file=e.get('1.0',END)
  c.write(text_file)
 except:
    print("")
def alt_new(event):
 words="Hello Fortran"
 j=f"program hello\n!create:{time.asctime()}\nimplicit none\nwrite(*,*) '{words}'\nend program"
 e.delete('1.0',END)
 e.insert('1.0',j)
def alt_new1(event):
 words="Hello"
 j=f"program read1\n!create:{time.asctime()}\nimplicit none\nreal::x\nwrite(*,*) 'Please write value:'\nread(*,*) x\nprint*, x\nend program"
 e.delete('1.0',END)
 e.insert('1.0',j)
def alt_new2(event):
 j=f"program array1\n!create:{time.asctime()}\nimplicit none\ninteger::x(10)\nx=[1,2,3,4,5,6,7,8,9,10]\nprint*,x\nend program"
 e.delete('1.0',END)
 e.insert('1.0',j)
def alt_new3(event):
 j=f"program empty\n!Empty file create:{time.asctime()}\nend program"
 e.delete('1.0',END)
 e.insert('1.0',j)
def alt_new4(event):
 j=f"program if\n!if file create:{time.asctime()}\ninteger::n=12\nif (n<13) then\nprint *, 'n less than 13'\nelse\nprint *,'n more than 13'\nend if\nend program"
 e.delete('1.0',END)
 e.insert('1.0',j)
def alt_new5(event):
  j=f"program while\n!File create:{time.asctime()}\ndo i=1,10\nprint*,i\nend do\nend program"
  e.delete('1.0',END)
  e.insert('1.0',j)
e.bind("<Control-n>",new_file1)
e.bind("<Control-s>",save_file1)
e.bind("<Control-o>",open_file1)
e.bind("<Control-r>",run_file1)
e.bind("<Alt-g>",compile_file2)
e.bind("<Control-g>",compile_file3)
e.bind("<Control-e>",save_edit1)
e.bind("<Control-l>",alt_new)
e.bind("<Control-m>",alt_new1)
e.bind("<Control-d>",alt_new2)
e.bind("<Control-f>",alt_new3)
e.bind("<Control-h>",alt_new4)
e.bind("<Control-j>",alt_new5)
a.config(menu=m)


a.mainloop()