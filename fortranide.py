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
from pygments.lexers.fortran import FortranLexer
from pygments.token import Token

a=Tk()
k=""
s2=""
lexer=FortranLexer()
a.title("Fortran ide")	
a.option_add("*tearOff", False)
e=Text(width=120,height=180)
e.tag_config("keyword", foreground='green')
e.tag_config("string_literal", foreground='blue')
e.tag_config("comment", foreground='red')
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
    text_file=e.get('1.0',END)
    c.write(text_file)
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
 c=open(k,"w")
 text_file=e.get('1.0',END)
 c.write(text_file)
def delete():
    e.delete('1.0',END)
def new_temp():
     words="Hello Fortran"
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

token_type_to_tag = {
    Token.Keyword: "keyword",
    Token.Operator.Word: "keyword",
    Token.Name.Builtin: "keyword",
    Token.Literal.String.Single: "string_literal",
    Token.Literal.String.Double: "string_literal",
    Token.Comment.Single: "comment",
    Token.Comment.Double: "comment"
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
m20.add_command(label="new template Hello Fortran",command=new_temp)
m20.add_command(label="new template read",command=new_temp1)
m20.add_command(label="new template array",command=new_temp2)
m20.add_command(label="new template empty",command=new_temp3)
m2.add_command(label="Run",command=run_file)
m2.add_command(label="Compile",command=compile_file)
m2.add_command(label="Compile this file",command=compile_file1)
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
def new_file1(event):
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
def save_file1(event):
 global k
 a=filedialog.asksaveasfilename(title="Save fortran file",filetypes=[("fortran file",("*.for","*.f","*.f90","*.f95","*.f08"))])
 if a!="":
  k=a
  c=open(a,"w")
  text_file=e.get('1.0',END)
  c.write(text_file)
def open_file1(event):
    global k
    a=filedialog.askopenfilename(title="Open fortran file",filetypes=[("fortran file",("*.for","*.f","*.f90","*.f95","*.f08"))])
    k=a
    if a!="":
     c=open(a,"r") 
     text=c.read()
     e.delete("1.0",END)
     e.insert("1.0",text)
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
 c=open(k,"w")
 text_file=e.get('1.0',END)
 c.write(text_file)
e.bind("<Control-n>",new_file1)
e.bind("<Control-s>",save_file1)
e.bind("<Control-o>",open_file1)
e.bind("<Control-r>",run_file1)
e.bind("<Alt-g>",compile_file2)
e.bind("<Control-g>",compile_file3)
e.bind("<Control-e>",save_edit1)
a.config(menu=m)
a.mainloop()