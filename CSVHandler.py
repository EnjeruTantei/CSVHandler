'''
Created on Mar 29, 2019

@author: Krystal
'''

class CSVHandler(object):
    '''
    classdocs
    '''
    import csv

    def __init__(self, url=False, newline='', mode = "r"):
        '''
        Constructor
        '''
        self.url = url
        self.newline = newline
        self.bookPress = None
        self.mode = mode
        self.openBook = None
        #print(">",mode)
        if self.url != False:
            self.book = self.OpenNewBook(url, newline, mode)
        else:
            self.book = None
            
        
    def read(self, delimiter=',', quotechar='|'):
        '''
        returns an open book.
        '''
        import csv
        return csv.reader(self.book, delimiter=delimiter, quotechar=quotechar)
    
    def getRows(self, openbook, returnToggle=False, printToggle = True):
        '''
        openbook @ def read:
        '''
        
        
        if returnToggle == False:
            for row in openbook:
                if printToggle == True:
                    print(', '.join(row))
        elif returnToggle == True:
            list = []
            for row in openbook:
                list.append(row)
                #print(', '.join(row))
            return(list)
        
    def getHeader(self, rows, returnToggle=False):
        if returnToggle == True:
            print(rows[0])
        else:
            array = {}
            for row in rows[0]:
                index = rows[0].index(row)
                array[row] = index
                #print(row, rows[0].index(row))
                
            return(array)
    def BuildTableOfContents(self, openbook):
        '''
        openbook @ def read:
        '''
        dict = {}
        
        for row in openbook:
            dict["row_"+str(len(dict))] = row
        
        return dict
        
    def OpenNewBook(self, name, newline="", mode='w'):
        '''
        Creates a new book
        '''
        if ".csv" not in name:
            name = name + ".csv"
            
        #print(">",name, newline, mode)
        self.openBook = open(name, mode=mode, newline=newline)
        return open(name, mode=mode, newline=newline)
        
    def BookPress(self, delimiter=',', quotechar='|'):
        import csv
        return csv.writer(self.book, delimiter=delimiter, quotechar=quotechar)
        
    def writeRow(self, row):
        if self.bookPress == None:
            self.bookPress = self.BookPress();
        
        self.bookPress.writerow(row);
        