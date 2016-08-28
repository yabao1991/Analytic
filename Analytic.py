from tkinter import *
import tkinter.messagebox as tkMessageBox
import tkinter.filedialog as tkFileDialog

from urllib.request import urlopen
import base64

import matplotlib
matplotlib.use("Agg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


from numpy import mean, median
from scipy.stats import skew, kurtosis
from collections import Counter
from statistics import pstdev

import wbdata
import pandas
from datetime import datetime, date, time

#""""""""""""""""""""""""""""""""""""Lin Zhang_Email Function"""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import webbrowser
#""""""""""""""""""""""""""""""""""""Lin Zhang_Email Function"""""""""""""""""""""""""""""""""""""""""""""""""""""


font_title = ("Avenir Heavy", 20)
#.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+
#.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+

class MenuBar(Menu):
    def __init__(self, parent):
       Menu.__init__(self, parent)
          
       ########## MENUBAR
       # FILE MENU    
       fileMenu = Menu(self, tearoff = 0)     
       fileMenu.add_command(label = "New", accelerator = "Ctrl+N", command = self.new_file)
       fileMenu.add_command(label = "Open", accelerator = "Ctrl+O", command = self.open_file)
       fileMenu.add_command(label = "Save", accelerator = "Ctrl+S", command = self.save)
       fileMenu.add_separator()
       fileMenu.add_command(label = "Exit", underline = 1, command = self.exit)
       self.add_cascade(label = "File", underline = 0, menu = fileMenu)  
       
       # HELP Menu
       helpmenu = Menu(self, tearoff = 0)
       helpmenu.add_command(label = 'About Us', command = self.About)
       self.add_cascade(label = 'Help', menu = helpmenu)
       
       
    ########### FUNCTIONS
    # Function - New File
    def new_file(self):
       if tkMessageBox.askyesno("Save. ","Do you want to save current file"):
          root.title("Untitled")
       global filename
       filename = None
       textPad.delete(1.0, END) # delete(start index,END index)

    # Function - Open File
    def open_file(self):
       myopen = filedialog.askopenfile()
       mlabel4 = Label(root,
                  text = myopen).pack()
       return

    # Function - Save
    def save(self):
       global filename
       try:
          f = open(filename,'w')
          letter = textPad.get(1.0, 'end')
          f.write(letter)
          f.close()
       except:
          save_as()

    # Function - Saveas
    def save_as(self):
       try:
          f = tkFileDialog.asksaveasfilename(**textPad.file_opt)
          fh = open(f, 'w')
          textoutput = textPad.get(1.0, END)
          fh.write(textoutput)
          fh.close()
          app.title(os.path.basename(f))
       except:
          pass
       
    # Function - Exit
    def exit(self):
       mExit = tkMessageBox.askyesno(title = "Quit",
                        message = "Are you sure?")
       if mExit > 0:
          root.destroy()
          return      
    
    # Function - About
    def About(self):
       tkMessageBox.showinfo(title = 'About Us',
                        message = 'Creating Tools for You')   
       
#.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+
#.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+      

class process(object):
    def __init__(self):
       pass    

    def generate(self, app):
       now = datetime.now()
       app.label_date.config(text = "Today is " + now.isoformat())
       x = app.textPad_population.get(1.0, END)
       app.label_output.config(text = x)
       return
#.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+
#.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+      

class page(Frame):
    def __init__(self, *args, **kwargs):
       Frame.__init__(self, *args, **kwargs)
    def show(self):
       self.lift()       

#.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+
#.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+

class page_home(page):
    def __init__(self, *args, **kwargs):
       page.__init__(self, *args, **kwargs)
       
       label = Label(self, text = "Home", font = font_title)
       label.pack(side = "top", fill = "both", expand = FALSE)


       frame_01 = Frame(self, bg = 'white', borderwidth = 2, relief = FLAT)
       frame_01.pack(side = TOP, padx = 2, pady = 2)

       url = "http://surjadjajaf.com/MISC/temp/20160816.MounikaHorse.gif"
       u = urlopen(url)
       raw_data = u.read()
       u.close()

       b64_data = base64.encodestring(raw_data)
       photo = PhotoImage(data = b64_data)

       label_photo = Label(frame_01, image = photo)
       label_photo.image = photo
       label_photo.pack(side = TOP, padx = 1, pady = 80)

       intro = '"The global financial crisis - missed by most analysts - shows that most forecasters are poor at pricing in economic/financial risks, let alone geopolitical ones." \n Nouriel Roubini, American economist'

       label_intro = Label(frame_01, text = intro, wraplength = 500, justify = CENTER)
       label_intro.pack(side = TOP, padx = 1, pady = 1)
       
       
       
#.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+
#.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.Mounika save function+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+      
       
class page_summary(page):
      def __init__(self, *args, **kwargs):
       page.__init__(self, *args, **kwargs)

       label = Label(self, text = "Summary", font = font_title)
       label.pack(side = "top", fill = "both", expand = FALSE)


       frame_01 = Frame(self, bg = 'white', borderwidth = 2, relief = FLAT)
       frame_01.pack(side = TOP, padx = 2, pady = 2)

       textPad_population = Text(frame_01, width = 39, height = 12,  bg = "light yellow", fg = "black", padx = 2, pady = 2)
       textPad_population.pack(side = TOP, fill = BOTH, expand = FALSE)
       x = textPad_population.delete(1.0, 'end')
       f = open('newfile.txt','r')
       for line in iter(f):
            print(line)
            textPad_population.insert(END, line)
       




#.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+
#.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+
class page_analytic_01(page):
    def __init__(self, *args, **kwargs):
       page.__init__(self, *args, **kwargs)
       def send_input():
          message = process()
          message.generate(self)

       def clear_input():
          x = textPad_population.delete(1.0, 'end')
          return
#++++++++++++++++++++++++++++++++++++++++++Mounika save function++++++++++++++++++++++++++++++++++++++++++++++++++++++++
       def saveComment():
          f = open('newfile.txt','a')
          comment = textPad_population.get(1.0, 'end')
          f.write(comment)
          f.close()
          x = textPad_population.delete(1.0, 'end')
          y = textPad_population1.delete(1.0, 'end')
          f = open('newfile.txt','r')
          for line in iter(f):
             textPad_population1.insert(INSERT, line)
#++++++++++++++++++++++++++++++++++++++++Mounika save fucntion+++++++++++++++++++++++++++++++++++++++++++++++++
#""""""""""""""""""""""""""""""""""""Lin Zhang_Email Function"""""""""""""""""""""""""""""""""""""""""""""""""""""
       def sendE():
          url = 'https://gmail.com'
          webbrowser.open(url)
          webbrowser.get()
#""""""""""""""""""""""""""""""""""""Lin Zhang_Email Function"""""""""""""""""""""""""""""""""""""""""""""""""""""

       
       label = Label(self, text = "Analytic 01", font = font_title)
       label.pack(side = "top", fill = "both", expand = FALSE)


       frame_01 = Frame(self, bg = 'white', borderwidth = 2, relief = FLAT)
       frame_01.pack(side = TOP, padx = 2, pady = 2)

       frame_011 = Frame(frame_01, bg = 'white', borderwidth = 2, relief = FLAT)
       frame_011.pack(side = LEFT, padx = 2, pady = 2)

       fig_population = Figure(figsize = (5.5, 3.5), dpi = 100, facecolor = 'white')
       addsubplot_population = fig_population.add_subplot(111)

       list_country = ["USA"]
       period_population = (datetime(1970, 1, 1), datetime(2016, 7, 23))
       indicators_population = {'SP.POP.TOTL': 'population'}

       df_population = wbdata.get_dataframe(indicators_population, country = list_country, data_date = period_population)
          
       df_population.index = df_population.index.astype('datetime64')
       x_population = df_population.index
       y_population = df_population.population
       addsubplot_population.plot(x_population, y_population)
       addsubplot_population.legend(labels = list_country, loc = 'best', fontsize = 8)    
       
       addsubplot_population.set_title('Population')
       addsubplot_population.set_xlabel('Time')
       fig_population.autofmt_xdate()
       addsubplot_population.set_ylabel('#')
       addsubplot_population.set_axis_bgcolor('white')

       frame_0111 = Frame(frame_011, bg = 'white', borderwidth = 2, relief = FLAT)
       frame_0111.pack(side = TOP, padx = 2, pady = 2)

       canvas_population = FigureCanvasTkAgg(fig_population, frame_0111)
       canvas_population.show()
       canvas_population.get_tk_widget().pack(side = TOP,  fill = BOTH,  expand = False)

       toolbar_population = NavigationToolbar2TkAgg(canvas_population, frame_0111)
       toolbar_population.update()
       canvas_population._tkcanvas.pack(side = TOP,  fill = BOTH,  expand = False)


       # Stats
       frame_0112 = Frame(frame_011, bg = 'white', borderwidth = 2, relief = FLAT)
       frame_0112.pack(side = TOP, padx = 2, pady = 2)

       mean_population = mean(df_population.population)
       label_mean = Label(frame_0112, text = 'Mean: %2.0f' %(mean_population))
       label_mean.pack(side = TOP, padx = 2, pady = 0)

       median_population = median(df_population.population)
       label_median = Label(frame_0112, text = 'Median: %2.0f' %(median_population))
       label_median.pack(side = TOP, padx = 2, pady = 0)

       data = Counter(df_population.population)
       mode_population = data.most_common(1)
       label_mode = Label(frame_0112, text = 'Mode:  %s' %(mode_population))
       label_mode.pack(side = TOP, padx = 2, pady = 0)

       sd_population = pstdev(df_population.population)
       label_sd = Label(frame_0112, text = 'Standard Deviation: %2.0f' %(sd_population))
       label_sd.pack(side = TOP, padx = 2, pady = 0)

       skewness_population = skew(df_population.population, axis = 0, bias = False)
       label_skew = Label(frame_0112, text = 'Skew: %2.4f' %(skewness_population))
       label_skew.pack(side = TOP, padx = 2, pady = 0)

       kurtosis_population= kurtosis(df_population.population, axis = 0, bias = False)
       label_kurtosis = Label(frame_0112, text = 'Kurtosis: %2.4f' %(kurtosis_population))
       label_kurtosis.pack(side = TOP, padx = 2, pady = 0)



       # Comment
       frame_012 = Frame(frame_01, bg = 'white', borderwidth = 2, relief = FLAT)
       frame_012.pack(side = LEFT, padx = 10, pady = 1)   

       textPad_population = Text(frame_012, width = 39, height = 30,  bg = "light yellow", fg = "black", padx = 2, pady = 2)
       textPad_population.pack(side = TOP, fill = BOTH, expand = False)

       textPad_population1 = Text(frame_012, width = 39, height = 12,  bg = "light yellow", fg = "black", padx = 2, pady = 2)
       textPad_population1.pack(side = TOP, fill = BOTH, expand = FALSE)
       x = textPad_population1.delete(1.0, 'end')
       f = open('newfile.txt','r')
       for line in iter(f):
            textPad_population1.insert(END, line)

       frame_0121 = Frame(frame_012, bg = 'white', borderwidth = 2, relief = FLAT)
       frame_0121.pack(side = TOP, padx = 1, pady = 1)

       button_population = Button(frame_0121, text = 'Save', fg = 'red', bg = 'blue', command = saveComment).pack(side = LEFT, padx = 2, pady = 2)
       button_population = Button(frame_0121, text = 'Clear', fg = 'red', bg = 'blue',  command = clear_input).pack(side = LEFT, padx = 2, pady = 2, )
       button_population = Button(frame_0121, text = 'Email', fg = 'red', command = sendE, bg = 'blue').pack(side = LEFT, padx = 2, pady = 2)
    

#.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+
#.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+

class page_analytic_02(page):
    def __init__(self, *args, **kwargs):
       page.__init__(self, *args, **kwargs)


       def send_input():
          message = process()
          message.generate(self)

       def clear_input():
          x = textPad_population.delete(1.0, 'end')
          return
#++++++++++++++++++++++++++++++++++++++++++Mounika save function++++++++++++++++++++++++++++++++++++++++++++++++++++++++
       def saveComment():
          f = open('newfile.txt','a')
          comment = textPad_population.get(1.0, 'end')
          f.write(comment)
          f.close()
          x = textPad_population.delete(1.0, 'end')
          y = textPad_population1.delete(1.0, 'end')
          f = open('newfile.txt','r')
          for line in iter(f):
             textPad_population1.insert(INSERT, line)
#++++++++++++++++++++++++++++++++++++++++Mounika save fucntion+++++++++++++++++++++++++++++++++++++++++++++++++

#""""""""""""""""""""""""""""""""""""Lin Zhang_Email Function"""""""""""""""""""""""""""""""""""""""""""""""""""""
       def sendE():
          url = 'https://gmail.com'
          webbrowser.open(url)
          webbrowser.get()
#""""""""""""""""""""""""""""""""""""Lin Zhang_Email Function"""""""""""""""""""""""""""""""""""""""""""""""""""""


       label = Label(self, text = "Analytic 02", font = font_title)
       label.pack(side = "top", fill = "both", expand = FALSE)


       frame_01 = Frame(self, bg = 'white', borderwidth = 2, relief = FLAT)
       frame_01.pack(side = TOP, padx = 2, pady = 2)

       frame_011 = Frame(frame_01, bg = 'white', borderwidth = 2, relief = FLAT)
       frame_011.pack(side = LEFT, padx = 2, pady = 2)

       fig_population = Figure(figsize = (5.5, 3.5), dpi = 100, facecolor = 'white')
       addsubplot_population = fig_population.add_subplot(111)

       list_country = ["GBR"]
       period_population = (datetime(1970, 1, 1), datetime(2016, 7, 23))
       indicators_population = {'SP.POP.TOTL': 'population'}

       df_population = wbdata.get_dataframe(indicators_population, country = list_country, data_date = period_population)
          
       df_population.index = df_population.index.astype('datetime64')
       x_population = df_population.index
       y_population = df_population.population
       addsubplot_population.plot(x_population, y_population)
       addsubplot_population.legend(labels = list_country, loc = 'best', fontsize = 8)    
       
       addsubplot_population.set_title('Population')
       addsubplot_population.set_xlabel('Time')
       fig_population.autofmt_xdate()
       addsubplot_population.set_ylabel('#')
       addsubplot_population.set_axis_bgcolor('white')

       frame_0111 = Frame(frame_011, bg = 'white', borderwidth = 2, relief = FLAT)
       frame_0111.pack(side = TOP, padx = 2, pady = 2)

       canvas_population = FigureCanvasTkAgg(fig_population, frame_0111)
       canvas_population.show()
       canvas_population.get_tk_widget().pack(side = TOP,  fill = BOTH,  expand = False)

       toolbar_population = NavigationToolbar2TkAgg(canvas_population, frame_0111)
       toolbar_population.update()
       canvas_population._tkcanvas.pack(side = TOP,  fill = BOTH,  expand = False)


       # Stats
       frame_0112 = Frame(frame_011, bg = 'white', borderwidth = 2, relief = FLAT)
       frame_0112.pack(side = TOP, padx = 2, pady = 2)

       mean_population = mean(df_population.population)
       label_mean = Label(frame_0112, text = 'Mean: %2.0f' %(mean_population))
       label_mean.pack(side = TOP, padx = 2, pady = 0)

       median_population = median(df_population.population)
       label_median = Label(frame_0112, text = 'Median: %2.0f' %(median_population))
       label_median.pack(side = TOP, padx = 2, pady = 0)

       data = Counter(df_population.population)
       mode_population = data.most_common(1)
       label_mode = Label(frame_0112, text = 'Mode:  %s' %(mode_population))
       label_mode.pack(side = TOP, padx = 2, pady = 0)

       sd_population = pstdev(df_population.population)
       label_sd = Label(frame_0112, text = 'Standard Deviation: %2.0f' %(sd_population))
       label_sd.pack(side = TOP, padx = 2, pady = 0)

       skewness_population = skew(df_population.population, axis = 0, bias = False)
       label_skew = Label(frame_0112, text = 'Skew: %2.4f' %(skewness_population))
       label_skew.pack(side = TOP, padx = 2, pady = 0)

       kurtosis_population= kurtosis(df_population.population, axis = 0, bias = False)
       label_kurtosis = Label(frame_0112, text = 'Kurtosis: %2.4f' %(kurtosis_population))
       label_kurtosis.pack(side = TOP, padx = 2, pady = 0)



       # Comment
       frame_012 = Frame(frame_01, bg = 'white', borderwidth = 2, relief = FLAT)
       frame_012.pack(side = LEFT, padx = 10, pady = 1)   

       textPad_population = Text(frame_012, width = 39, height = 30,  bg = "light yellow", fg = "black", padx = 2, pady = 2)
       textPad_population.pack(side = TOP, fill = BOTH, expand = False)
#++++++++++++++++++++++++++++++++++++++++++++++++++Mounika save function++++++++++++++++++++++++++++++++++++++++++++++++++++       
       textPad_population1 = Text(frame_012, width = 39, height = 12,  bg = "light yellow", fg = "black", padx = 2, pady = 2)
       textPad_population1.pack(side = TOP, fill = BOTH, expand = FALSE)
       x = textPad_population1.delete(1.0, 'end')
       f = open('newfile.txt','r')
       for line in iter(f):
            textPad_population1.insert(END, line)
#+++++++++++++++++++++++++++++++++++++++++++Mounika save function++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
       frame_0121 = Frame(frame_012, bg = 'white', borderwidth = 2, relief = FLAT)
       frame_0121.pack(side = TOP, padx = 1, pady = 1)

       button_population = Button(frame_0121, text = 'Save', fg = 'red', bg = 'blue', command = saveComment).pack(side = LEFT, padx = 2, pady = 2)
       button_population = Button(frame_0121, text = 'Clear', fg = 'red', bg = 'blue',  command = clear_input).pack(side = LEFT, padx = 2, pady = 2, )
       button_population = Button(frame_0121, text = 'Email', fg = 'red', command = sendE, bg = 'blue').pack(side = LEFT, padx = 2, pady = 2)

       # Label
       today = ""
       self.label_date = Label(self, text = today)
       self.label_date.pack(side = TOP)
       x = ""
       self.label_output = Label(self, text = x)
       self.label_output.pack(side = TOP)

       
#.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+
#.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+
       
class MainView(Frame):    
    def __init__(self, *args, **kwargs):
       Frame.__init__(self, *args, **kwargs)
       self.menu()
       
       home = page_home(self)
       summary = page_summary(self)
       analytic_01 = page_analytic_01(self)
       analytic_02 = page_analytic_02(self)
             
       ########## BANNER
       label_top = Label(self,
                  bg = "#89440b",
                  height = 2,
                  width = 1200)
       label_top.pack(side = TOP,
                expand = NO,
                fill = X)      

       label_bottom = Label(self,
                  bg="#eda14b",
                  height = 2,
                  width = 1200)
       label_bottom.pack(side = BOTTOM,
                expand = NO,
                fill = X)

                
       frame_0 = Frame(self, bg = 'white', borderwidth = 2, relief = FLAT)
       frame_0.pack(side = TOP, padx = 10, pady = 1)
          
       buttonframe = Frame(self)
       container = Frame(self)
       buttonframe.pack(side="top", fill="x", expand=False)
       container.pack(side="top", fill="both", expand=True)
       
       home.place(in_ = container, x = 0, y = 0, relwidth = 1, relheight=1)
       summary.place(in_ = container, x = 0, y = 0, relwidth = 1, relheight = 1)
       analytic_01.place(in_ = container, x = 0, y = 0, relwidth=1, relheight = 1)
       analytic_02.place(in_ = container, x = 0, y = 0, relwidth=1, relheight = 1)
       
       button_home = Button(frame_0, text = "Home", command = home.lift)
       button_summary = Button(frame_0, text = "Summary", command = summary.lift)
       button_analytic_01 = Button(frame_0, text = "Analytic 01", command = analytic_01.lift)
       button_analytic_02 = Button(frame_0, text = "Analytic 02", command = analytic_02.lift)

       button_home.grid(row = 0, column = 0, padx = 20, pady = 1)
       button_summary.grid(row = 0, column = 1, padx = 20, pady = 1)
       button_analytic_01.grid(row = 0, column = 2, padx = 20, pady = 1)
       button_analytic_02.grid(row = 0, column = 3, padx = 20, pady = 1)

       home.show()
       
    def menu(self):
       menubar = MenuBar(root)
       root.config(menu = menubar)
       





#.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+
#.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+      

if __name__ == "__main__":
    root = Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.geometry("900x700+51+51") # dimensions of the window
    root.title("Analytic")
    root.mainloop()




