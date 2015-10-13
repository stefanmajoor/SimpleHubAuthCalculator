from Tkinter import *
import numpy as np
import math

class App:
    def __init__(self, master):
        self.rows = 4
        self.master = master
        self.update()
        self.matrixlabels = []
 
    '''
    Display all items 
    '''
    def update(self):
        self.frame = Frame(self.master)
        ## How many values
        Label(self.master, text="Amount of nodes:").grid(row=0, column=0, columnspan=3)
        
        ## No idea why this works. But it does
        var = StringVar(root)
        var.set(str(self.rows))
        self.rowBox = Spinbox(self.master, from_=1, to=10, textvariable=str(var))
        self.rowBox.grid(row=0, column=3, columnspan=3)
        Button(self.master, text="Update", command=self.setRows).grid(row=0, column=6)


        ## From and to indications
        Label(self.master, text="To").grid(column=3, row=1)
        Label(self.master, text="From").grid(row=3, column=0)

        self.labels = []

        ## Letters at top
        for i in range(0, self.rows):
            label = Label(self.master, text=unichr(ord("A")+i))
            label.grid(row=2, column=i+2)
            self.labels.append(label)

        ## Letters at the left
        for i in range(0, self.rows):
            label = Label(self.master, text=unichr(ord("A")+i))
            label.grid(row=i+3, column=1)
            self.labels.append(label)

        ## Create all entry fields
        self.entries = [[0. for i in range(self.rows)] for j in range(self.rows)]
        for i in range(0,self.rows):
            for j in range(0,self.rows):
                self.entries[i][j] = Spinbox(self.master, from_=0, to=10, width=3)
                self.entries[i][j].grid(row=i+3, column = j+2)

        ## calculate the different values
        values = []
        for i in range(0, self.rows):
            values.append(unichr(ord("A")+i))


        ## Run button
        Button(self.master, text="Run", command=self.calculate).grid(row=15, column=6)

    '''
    Set the amount of rows
    '''
    def setRows(self):
        self.rows = int(self.rowBox.get())
        self.frame.grid_remove()
        for i in range(0,len(self.entries)):
            for j in range(0, len(self.entries[i])):
                self.entries[i][j].destroy()

        for label in self.labels:
            label.destroy()

        for label in self.matrixlabels:
            label.destroy()
        self.update()

    '''
    Calculate the Pagerank
    '''
    def calculate(self):
        values = np.empty([self.rows, self.rows])
        for i in range(0,self.rows):
            for j in range(0,self.rows):
                values[i][j] = self.entries[i][j].get()


        label = Label(self.master, text="==HUBS==")
        label.grid(row=39, column=1)
        self.matrixlabels.append(label)

        label = Label(self.master, text="=========")
        label.grid(row=39, column=self.rows+1)
        self.matrixlabels.append(label)

        label = Label(self.master, text="==AUTHS==")
        label.grid(row=39, column=self.rows+2)
        self.matrixlabels.append(label)


        label = Label(self.master, text="Iteratie")
        label.grid(row=40, column=0)
        self.matrixlabels.append(label)

        ## Letters at top
        for j in range(0, 2):
            for i in range(0, self.rows):
                label = Label(self.master, text=unichr(ord("A")+i))
                label.grid(row=40, column=(i+1 + (1+self.rows)*j))
                self.matrixlabels.append(label)

        ## Assign hubs and auth scores
        hubs = np.ones(self.rows)
        auth = np.ones(self.rows)


        for i in range(0, 20):
            ## print the values
            label = Label(self.master, text=str(i))
            label.grid(row=41+i, column=0)
            self.matrixlabels.append(label)
            for j in range(0, self.rows):
                label = Label(self.master, text=str(round(hubs[j], 3)))
                label.grid(row=41+i, column=j+1)
                self.matrixlabels.append(label)

                label = Label(self.master, text=str(round(auth[j], 3)))
                label.grid(row=41+i, column=j+2+self.rows)
                self.matrixlabels.append(label)

            ## Now update hubs and auths
            sumNewHubs = 0
            newHubs = np.zeros(self.rows)

            for i in range(0, self.rows):
                for j in range(0, self.rows):
                    newHubs[i] += float(auth[j]) * values[i][j]
                    sumNewHubs += float(auth[j]) * values[i][j]

            newHubs /= sumNewHubs

            sumNewAuths = 0
            newAuths = np.zeros(self.rows)

            for i in range(0, self.rows):
                for j in range(0, self.rows):
                    newAuths[i] += float(hubs[j]) * values[j][i]
                    sumNewAuths += float(hubs[j]) * values[j][i]

            newAuths /= sumNewAuths

            auth = newAuths
            hubs = newHubs

root = Tk()

app = App(root)

root.mainloop()
root.destroy() # optional; see description below