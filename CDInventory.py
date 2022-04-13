#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# KBloodsworth, 2022-Mar-20, Completed TODO's 
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    # TODone Add Code to the CD class
    
    # --Fields-- #
    # --Constructor-- #
    def __init__(self, ID, Title, Artist):
        self.__ID = int(ID)
        self.__Title = str(Title)
        self.__Artist = str(Artist)
        
    # --Properties-- #
    @property
    def ID(self):
        return self.__ID
    
    @ID.setter
    def ID(self, value):
        self.__ID = int(value)
        
    @property
    def Title(self):
        return self.__Title
    
    @Title.setter
    def Title(self, value):
        self.__Title = str(value)
        
    @property
    def Artist(self):
        return self.__Artist
    
    @Artist.setter
    def Artist(self, value):
        self.__Artist = str(value)
    
    

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    
    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        # TODone Add code to process data from a file
        #Lets the user know that the file is missing
        try:
            table.clear()  # this clears existing data and allows to load data from file
            objFile = open(file_name, 'r')
            for line in objFile:
                data = line.strip().split(',')
                dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
                table.append(dicRow)
            objFile.close()
        except FileNotFoundError:
            print('\nFile not found!\n')
        except EOFError:
            print('\nFile is empty!\n')
            
    @staticmethod
    # TODone Add code to process data to a file
    def write_file(file_name, table):
        """Function to write the table to file. 
        
        Writes the 2D data structure table consisting of list of dicts to file 
        
        Args:
            file_name (string): name of file used to write the 2D data structure to, from table: list of dicts
            written to file
            
        Returns:
            None
        """
        #Lets the user know that the file is missing
        try:
            objFile = open(strFileName, 'w')
            for row in table:
                lstValues = list(row.values())
                lstValues[0] = str(lstValues[0])
                objFile.write(','.join(lstValues) + '\n')
            objFile.close()
        except FileNotFoundError:
            print('\nFile not found!\n')
        

# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output"""

    @staticmethod
    # TODone add code to show menu to user
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    # TODone add code to captures user's choice
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    # TODone add code to display the current data on screen
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')

    @staticmethod 
    # TODone add code to get CD data from user
    def add_input():
        """Function asks user to input new ID, Title, and Artist
                
        Args:
            None.
            
        Returns:
            strID(string): CD ID, input from user
            strTitle(string): CD title, input from user 
            strArtist(string): artist name, input from user
        
        """
        strID = input('Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        return strID, strTitle, strArtist
    
   
class DataProcessor:
    # TODone add functions for processing here
    @staticmethod 
    def add_item(strID, strTitle, strArtist):
        """Function to add item to lstOfCDObjects
    
        Args:
            strID(string): CD ID, input from user to add to table
            strTitle(string): CD title, input from user to add to table
            strArtist(string): artist name, input from user to add to table
            
        Returns:
            None. 
        """
        #Tell user the value must be an integer
        try:
            intID = int(strID)
            dicRow = {'ID': intID, 'Title': strTitle, 'Artist': strArtist}
            print('ID must be an integer')
            lstOfCDObjects.append(dicRow)
            IO.show_inventory(lstOfCDObjects)
        except ValueError:
            print('\nMust be an integer!\n')
            
    @staticmethod 
    def del_CD(ntIDDel):
        """Function to delete CD entry from the lstOfCDObjects
        
        Allows the user to choose to delete a CD entry from the lstOfCDObjects
        
        Args:
            None
            
        Returns:
            None
            
        """
        intRowNr = -1
        blnCDRemoved = False
        for row in lstOfCDObjects:
            intRowNr += 1
            if row['ID'] == intIDDel:
                del lstOfCDObjects[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')
              
    # TODone add docstring
    

# -- Main Body of Script -- #
# TODone Add Code to the main body

# 1. When program starts, read in the currently saved Inventory
FileIO.read_file(strFileName, lstOfCDObjects)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileIO.read_file(strFileName, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        strID, strTitle, strArtist = IO.add_input()

        # 3.3.2 Add item to the table
        DataProcessor.add_item(strID, strTitle, strArtist)
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        try:
            IO.show_inventory(lstOfCDObjects)
            # 3.5.1.2 ask user which ID to remove
            intIDDel = int(input('Which ID would you like to delete? ').strip())
            # 3.5.2 search thru table and delete CD
            DataProcessor.del_CD(intIDDel)
            IO.show_inventory(lstOfCDObjects)
            continue  # start loop back at top.
        except ValueError:
            print('\nMust be an integer!\n')
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileIO.write_file(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')



