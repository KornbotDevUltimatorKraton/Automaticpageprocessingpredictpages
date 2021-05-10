import re # Regular expression word 
import os #Operating system onboard 
import subprocess #Subprocess for processing the command and extract string from the terminal
import camelot # Extract the data table from the pdf file
from PyPDF2 import PdfFileWriter, PdfFileReader
import wordninja
import json
import pandas as pd
os.system("echo 'Rkj3548123' | sudo -S mkdir ComponentDoc") # Get the documentation of the components 
os.system("echo 'Rkj3548123' | sudo -S mkdir tempolarydocextract") #Get the data extract from the table of the pdf part specification
os.system("echo 'Rkj3548123' | sudo -S mkdir Configuresearch") #Create the configure file for the search in json 
os.system("echo 'Rkj3548123' | sudo -S chmod -R 777 ComponentDoc") # Activate the permission 
os.system("echo 'Rkj3548123' | sudo -S chmod -R 777 tempolarydocextract") # Activate the permission
os.system("echo 'Rkj3548123' | sudo -S chmod -R 777 Configuresearch") # Activate the permission
username = str(subprocess.check_output("uname -a",shell=True)) # Get the the username of the computer reading from the client computer 
Getusername = username.split("-")[0].split(" ")[1]  #Get the username
PATHMAIN = "/home/"+str(Getusername)+"/Automaticsoftware/ComponentDoc"
HOME = "/home/"+str(Getusername)+"/Automaticsoftware/"
EXTRACT  = "/home/"+str(Getusername)+"/Automaticsoftware/tempolarydocextract" #Tempolary read the file extraction from the pdf specification function
CONFIG   = "/home/"+str(Getusername)+"/Automaticsoftware/Configuresearch" # Config file
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# List file in the path directory on each 
listMainpath = os.listdir(PATHMAIN)  #Get the main path of the directory 
listExtract = os.listdir(EXTRACT)    #Get the extraction of the data tables in the component information pins configurection 
listConfig = os.listdir(CONFIG) #Get the list config file from the system 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
output = PdfFileWriter()
input1 = PdfFileReader(open(PATHMAIN+"/"+"drv8320.pdf", "rb"))
inputcomp = "drv8320" # Get the component input data 
# Pins search continued function for long range pins configurection 
searchpinsconfiguretion = "Pin Configuration and Functions"
searchConfigcontinued = "Pin Functions (continued)"
specificationExtract = ""
# print how many pages input1 has:
print("document1.pdf has %d pages." % input1.getNumPages())
#for page in input1.pages:
         
#            print(page,page.extractText())
#first_page = input1.getPage(3)
#print(first_page.extractText())
#print(wordninja.split(str(first_page.extractText())))
listConfig = os.listdir(CONFIG) #Get the config file 
Pageclassification = [] # Save the page classification for predeict the next page output from the boundary configuretion on the json file
Packagecheck = []  # Checking the len of the list package 
Pinsquantity = []  # Get the quantity of the pins on the ic 
Currentpage =  []  #Current page found on the data 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
        #list devices bugget and combine for the table data type page processing
Devicesbucket = [] # Device bucket for the page processing 
Packagetypebucket = [] #Package type for the page processing 
Pinsbucket = [] # Getting the pins bucket data for the value of each package type data combination dictionary
reftabledetect = [] # Get the table detector referent inside the array 
refpins = [] #Get the reference pins 
refpagecal = [] # Get the referent page from the page classification algorithm
nextpage = [] #Get the prediction page 
combinedictdata = {}  # Get the dictionarylist of the data output for page processingfunction 
Pinsextract = {} # Generate the dictionary for the page reference and the next page prediction 

Packageslist  = open(CONFIG+"/"+listConfig[0],'r')# Reading the configfile 
Packagedatalist = Packageslist.readline()
PackagesLoad = json.loads(Packagedatalist)
print(PackagesLoad.get('package').get('packagesdrawing')) #Get the package of the ic for adding into the list detected 
def Pagecalculation(outputinterger): 
   if int(outputinterger) <= 144:
          print("In the range of package pins=",outputinterger)
          #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
               # Put the page calculation here for the 
def Configure(configfile): 
     try: 
       data = open(CONFIG+"/"+str(configfile),'r') #Open the configuretion file for the path 
       datas = data.readline()
       transfer = json.loads(datas)
       return transfer
     except:
        print("Not found the configure file please check again")
def Modeextractnotable(datapins,df,listdata,q): 

                  if str(listdata[q]).split(" ")[0] in datapins:
                          print("Found the header",listdata[q],"Begin extraction....") # Activate actraction begin 
                          for i in range(1,len(df[listdata[q]])):
                              print(i,df[listdata[q]].values[i])

                  if listdata[q] in datapins: 
                       print("Found the header",listdata[q],"Begin extraction....") # Activate actraction begin 
                       for i in range(1,len(df[listdata[q]])):
                              print(i,df[listdata[q]].values[i])
                              print(Pinsquantity.append(str(df[listdata[q]].values[i])))
def Modeextracttion(datapins,transfer,df,listdata,q):
               # TI pattern pinconfigureation table 
               # Pins configure 

                 
                  devicename = transfer.get("Device").get("devices") #Extracting the pins name from the TI 
                  packagedevice = transfer.get("Device").get("packagedata") # Get the Description text 
                  pinsnumber = transfer.get("Device").get("pins") #Get the pins number from the device package from the pdf file
                  Devices = ['Device']
                  Package = ['Package\nType']
                  Pinsnumber = ['Pins']
                  if datapins[0] == "Device":
                    print("Get the Device  name")  
                    if listdata[q] in datapins: 
                       print("Found the header",listdata[q],"Begin extraction string....") # Activate actraction begin 
                       for i in range(1,len(df[listdata[q]])):
                              print(i,df[listdata[q]].values[i])
                              print(Devicesbucket.append(str(df[listdata[q]].values[i])))
                  if datapins[0] == "Package\nType":
                    print("Get the Device  name")  
                    if listdata[q] in datapins: 
                       print("Found the header",listdata[q],"Begin extraction string....") # Activate actraction begin 
                       for i in range(1,len(df[listdata[q]])):
                              print(i,df[listdata[q]].values[i])
                              print(Packagetypebucket.append(str(df[listdata[q]].values[i]))) 
                  if datapins[0] == "Pins":
                    print("Get the Device  name")  
                    if listdata[q] in datapins: 
                       print("Found the header",listdata[q],"Begin extraction string....") # Activate actraction begin 
                       for i in range(1,len(df[listdata[q]])):
                              print(i,df[listdata[q]].values[i])
                              print(Pinsbucket.append(str(df[listdata[q]].values[i]))) 
#Bit bucket for the combine                                                      
def Bucketcombinefunc(devicesinput,Packagetypebucket,Pinsbucket): # Get the list from each package input  
       print("Combine each package datainto the dict") # The function to combine the dictionary file into the dictionary 
       for qw in range(0,len(devicesinput)):  # using qw to get the value in the list array 
                   print("Begin creating the dictionary data function") 
                   combinedictdata[str(devicesinput[qw])] = str(Packagetypebucket[qw])+","+str(Pinsbucket[qw])  #Get the list variable to generate the json and dictionary data structure                  
                   
def extractionalgorithm(df,listdata,configfile):
          # In the case not detected table running this function 
          try: 
              print(configfile)
              data = open(CONFIG+"/"+str(configfile),'r') #Open the configuretion file for the path 
              datas = data.readline()
              transfer = json.loads(datas)
              print(transfer)
          except:
              print("Not found the configure file please check again")

          #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
          # TI pattern for the extraction

          datapins = transfer.get("Unnamed").get("Unnamed") #Extracting the pins name from the TI 
          description = transfer.get("Description").get("description") # Get the Description text 
          inputoutput = transfer.get("IO").get("io") #IO get the input output pins function matching pins
          print(inputoutput)
          print(description)
          #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
               # Pins configure 
          for q in range(0,len(listdata)): 
                  
                  Modeextractnotable(datapins, df, listdata, q),Modeextractnotable(description, df, listdata, q),Modeextractnotable(datapins, df, listdata, q) 
def extractpinspackage(df,listdata,configfile): 
           print("Begin extraction the pins and package from the package information page")
           try: 
              print(configfile)
              data = open(CONFIG+"/"+str(configfile),'r') #Open the configuretion file for the path 
              datas = data.readline()
              transfer = json.loads(datas)
              print(transfer)
           except:
              print("Not found the configure file please check again")

          #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
          # TI pattern for the extraction

           devicename = transfer.get("Device").get("devices") #Extracting the pins name from the TI 
           packagedevice = transfer.get("Device").get("packagedata") # Get the Description text 
           pinsnumber = transfer.get("Device").get("pins") #Get the pins number from the device package from the pdf file
           print(devicename)  # Using the first one as the key 
           print(packagedevice) # First value 
           print(pinsnumber) # Second value 
          #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
               # Pins configure 
           listMode = [['Device'],['Package\nType'],['Pins']]            
           for q in range(0,len(listdata)):     
                  print(Modeextracttion(listMode[0],transfer,df,listdata,q))
           for q in range(0,len(listdata)): 
                  print(Modeextracttion(listMode[1], transfer, df, listdata, q))
           for q in range(0,len(listdata)): 
                  print(Modeextracttion(listMode[2], transfer, df, listdata, q))
def Tabledetector(intput1,inputcomp,Pinsquantity): 
        for i in reversed(range(0,input1.getNumPages())):  # Running the page for the back checking 
         first_page = input1.getPage(i)
         print(first_page.extractText())
         print(wordninja.split(str(first_page.extractText())))
         outputdat = str(first_page.extractText())
         Extracteddata = wordninja.split(str(first_page.extractText())) # Get the list to searching the pattern of the product type
         if 'PACKAGING'in Extracteddata: 
                   print("Found package")
                   if 'INFORMATION' in Extracteddata: 
                                  print("Found information break....")
                                  print("".join(Extracteddata))
                                  packlist = PackagesLoad.get('package').get('rootpackages')
                                  packdrawing = PackagesLoad.get('package').get('packagesdrawing')
                                  print("Case 1")  
                                  tables = camelot.read_pdf(PATHMAIN +"/"+str(inputcomp)+".pdf",pages=str(i))
                                  if len(tables) == 0: 
                                         print("Not Found the data table",len(tables))
                                         for i in range(0,len(packlist)):
                                          check = any(item in wordninja.split(str(packlist[i])) for item in Extracteddata)
                                          print(check)
                                          try:
                                             if check == True: 
                                                   print(Extracteddata[Extracteddata.index(packlist[i])])
                                                   print(wordninja.split(str(packlist[i])),len(wordninja.split(str(packlist[i]))))
                                                   outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(wordninja.split(str(packlist[i])))]
                                                   check2 = any(item in wordninja.split(str(outputinterger)) for item in Extracteddata)
                                                   if outputinterger.strip().isdigit():
                                                         print("Output is Number")
                                                         print(outputinterger) #Get tge output here to calculate the page output data 
                                                   else:
                                                      print("Output is string")
                                                      if check2 == True:
                                                         print("Check loop 2")
                                                         if len(outputinterger) >1:
                                                              outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(wordninja.split(str(outputinterger)))+len(wordninja.split(str(packlist[i])))]
                                                              print(outputinterger)
                                                              print(Pinsquantity.append(str(outputinterger)))

                                                         if len(outputinterger) == 1: 
                                                              print("detected len integer")
                                                              outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(outputinterger)+len(wordninja.split(str(outputinterger)))+len(wordninja.split(str(packlist[i])))]
                                                              print(outputinterger)   
                                                              print(Pinsquantity.append(str(outputinterger)))
                                                              if int(outputinterger) <= 144:
                                                                      print("In the range of package pins=",outputinterger)

                                                                      #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>        
                                                                                    #Get the page calculation here 
                                                                      #one page output calculation   
                                                          
                                          except:
                                             print("This part is not found in the list package")
                                  if len(tables) >= 1:
                                         #Data table found then classify and extract the pins and packages 
                                         print("Found the data table",len(tables)) 
                                         print(tables[0].df)
                                         print(tables[0].parsing_report)
                                         tables[0].to_csv(EXTRACT +"/"+str(inputcomp)+'.csv') 
                                         #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                         print("Reading pandas....")
                                         df = pd.read_csv (r''+EXTRACT+"/"+str(inputcomp)+'.csv')
                                         print(df)
                                         print(Configure(listConfig[0])) # Get the data from the json file
                                         #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                         # Algorithm for classify the extraction of the text 
                                         index = df.index
                                         number_of_rows = len(index)
                                         print(number_of_rows)
                                         listdata = list(df.columns.values)
                                         print(listdata)
                                         extractpinspackage(df,listdata,listConfig[0])
                                  break
         if 'PACKAGE'in Extracteddata: 
                   print("Found package")
                   if 'MATERIALS' in Extracteddata: 
                           print("Found Material")
                           if 'INFORMATION' in Extracteddata: 
                                  print("Found information break....")
                                  print("".join(Extracteddata))
                                  packlist = PackagesLoad.get('package').get('rootpackages')
                                  packdrawing = PackagesLoad.get('package').get('packagesdrawing')
                                  print("Case 2")
                                  tables = camelot.read_pdf(PATHMAIN +"/"+str(inputcomp)+".pdf",pages=str(i))
                                  if len(tables) == 0: 
                                         print("Not Found the data table",len(tables))
                                         for i in range(0,len(packlist)):
                                          check = any(item in wordninja.split(str(packlist[i])) for item in Extracteddata)
                                          print(check)
                                          try:
                                             if check == True: 
                                                   print(Extracteddata[Extracteddata.index(packlist[i])])
                                                   print(wordninja.split(str(packlist[i])),len(wordninja.split(str(packlist[i]))))
                                                   outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(wordninja.split(str(packlist[i])))]
                                                   check2 = any(item in wordninja.split(str(outputinterger)) for item in Extracteddata)
                                                   print(outputinterger)
                                                   if outputinterger.strip().isdigit():
                                                         print("Output is Number")
                                                         print(wordninja.split(str(outputinterger)))
                                                         print(outputinterger) #Get tge output here to calculate the page output data 
                                                   else:
                                                      print("Output is string")

                                                      if check2 == True:
                                                         print("Check loop 2")
                                                         print(wordninja.split(str(outputinterger)))
                                                         if len(outputinterger) >1:
                                                              outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(wordninja.split(str(outputinterger)))+len(wordninja.split(str(packlist[i])))]
                                                              print(outputinterger)
                                                              print(Pinsquantity.append(str(outputinterger)))

                                                              if outputinterger <=144: 
                                                                     print("In the ranage of the package pins",outputinterger) 
                                                                     #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                                                                    #Get the page calculation here  
                                                         if len(outputinterger) == 1: 
                                                              print("detected len integer")
                                                              outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(outputinterger)+len(wordninja.split(str(outputinterger)))+len(wordninja.split(str(packlist[i])))]
                                                              print(outputinterger)
                                                              print(Pinsquantity.append(str(outputinterger)))

                                                              if outputinterger <= 144:
                                                                      print("In the range of package pins",outputinterger)
                                                                      #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>        
                                                                                    #Get the page calculation here 
                                                   break                                       
                                          except:
                                             print("This part is not found in the list package")  
                                  if len(tables) >= 1:
                                         print("Found the data table",len(tables))
                                         reftabledetect.append(str(len(tables))) # checking the len after fererence if found then equal 1 
                                         print(tables[0].df)
                                         print(tables[0].parsing_report)
                                         tables[0].to_csv(EXTRACT +"/"+str(inputcomp)+'.csv') 
                                         #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                         print("Reading pandas....")
                                         df = pd.read_csv (r''+EXTRACT+"/"+str(inputcomp)+'.csv')
                                         print(df)
                                         print(Configure(listConfig[0])) # Get the data from the json file
                                         #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                         # Algorithm for classify the extraction of the text 
                                         index = df.index
                                         number_of_rows = len(index)
                                         print(number_of_rows)
                                         listdata = list(df.columns.values)
                                         print(listdata)
                                         extractpinspackage(df,listdata,listConfig[0])
                                  break
def CheckingPins(input1):
       for i in reversed(range(0,input1.getNumPages())):  # Running the page for the back checking 
         first_page = input1.getPage(i)
         print(first_page.extractText())
         print(wordninja.split(str(first_page.extractText())))
         outputdat = str(first_page.extractText())
         Extracteddata = wordninja.split(str(first_page.extractText())) # Get the list to searching the pattern of the product type
         if 'PACKAGING'in Extracteddata: 
                   print("Found package")
                   if 'INFORMATION' in Extracteddata: 
                                  print("Found information break....")
                                  print("".join(Extracteddata))
                                  packlist = PackagesLoad.get('package').get('rootpackages')
                                  packdrawing = PackagesLoad.get('package').get('packagesdrawing')
                                  print("Case 1")
                                  for i in range(0,len(packlist)):
                                          check = any(item in wordninja.split(str(packlist[i])) for item in Extracteddata)
                                          print(check)
                                          try:
                                             if check == True: 
                                                   print(Extracteddata[Extracteddata.index(packlist[i])])
                                                   print(wordninja.split(str(packlist[i])),len(wordninja.split(str(packlist[i]))))
                                                   outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(wordninja.split(str(packlist[i])))]
                                                   check2 = any(item in wordninja.split(str(outputinterger)) for item in Extracteddata)
                                                   if outputinterger.strip().isdigit():
                                                         print("Output is Number")
                                                         print(outputinterger) #Get tge output here to calculate the page output data 
                                                   else:
                                                      print("Output is string")
                                                      if check2 == True:
                                                         print("Check loop 2")
                                                         if len(outputinterger) >1:
                                                              outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(wordninja.split(str(outputinterger)))+len(wordninja.split(str(packlist[i])))]
                                                              print(outputinterger)
                                                         if len(outputinterger) == 1: 
                                                              print("detected len integer")
                                                              outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(outputinterger)+len(wordninja.split(str(outputinterger)))+len(wordninja.split(str(packlist[i])))]
                                                              print(outputinterger)   
                                                              if int(outputinterger) <= 144:
                                                                      print("In the range of package pins=",outputinterger)
                                                                      Packagecheck.append(outputinterger)
                                                                      #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>        
                                                                                    #Get the page calculation here 
                                                                      #one page output calculation   
                                                          
                                          except:
                                             print("This part is not found in the list package")
                                  break
         if 'PACKAGE'in Extracteddata: 
                   print("Found package")
                   if 'MATERIALS' in Extracteddata: 
                           print("Found Material")
                           if 'INFORMATION' in Extracteddata: 
                                  print("Found information break....")
                                  print("".join(Extracteddata))
                                  packlist = PackagesLoad.get('package').get('rootpackages')
                                  packdrawing = PackagesLoad.get('package').get('packagesdrawing')
                                  print("Case 2")
                                  for i in range(0,len(packlist)):
                                          check = any(item in wordninja.split(str(packlist[i])) for item in Extracteddata)
                                          print(check)
                                          try:
                                             if check == True: 
                                                   print(Extracteddata[Extracteddata.index(packlist[i])])
                                                   print(wordninja.split(str(packlist[i])),len(wordninja.split(str(packlist[i]))))
                                                   outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(wordninja.split(str(packlist[i])))]
                                                   check2 = any(item in wordninja.split(str(outputinterger)) for item in Extracteddata)
                                                   print(outputinterger)
                                                   if outputinterger.strip().isdigit():
                                                         print("Output is Number")
                                                         print(wordninja.split(str(outputinterger)))
                                                         print(outputinterger) #Get tge output here to calculate the page output data 
                                                   else:
                                                      print("Output is string")

                                                      if check2 == True:
                                                         print("Check loop 2")
                                                         print(wordninja.split(str(outputinterger)))
                                                         if len(outputinterger) >1:
                                                              outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(wordninja.split(str(outputinterger)))+len(wordninja.split(str(packlist[i])))]
                                                              print(outputinterger)
                                                              if outputinterger <=144: 
                                                                     print("In the ranage of the package pins",outputinterger) 
                                                                     #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                                                                    #Get the page calculation here  
                                                         if len(outputinterger) == 1: 
                                                              print("detected len integer")
                                                              outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(outputinterger)+len(wordninja.split(str(outputinterger)))+len(wordninja.split(str(packlist[i])))]
                                                              print(outputinterger)
                                                              if outputinterger <= 144:
                                                                      print("In the range of package pins",outputinterger)
                                                                      Packagecheck.append(outputinterger) #Get the output integer of the pins and save into the package check list to classify the pins 
                                                                      #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>        
                                                                                    #Get the page calculation here 
                                                   break                                       
                                          except:
                                             print("This part is not found in the list package")         
                                  break
def Pinsearchfunction(input1,inputcomp,searchpinsconfiguretion):   
               print("Searching pin configuretion page.....")
               for i in range(0,input1.getNumPages()):  # Running the page for the back checking 
                  first_page = input1.getPage(i)
                  print(first_page.extractText())
                  print(wordninja.split(str(first_page.extractText())))
                  outputdat = str(first_page.extractText())
                  Extracteddata = wordninja.split(str(first_page.extractText())) # Get the list to searching the pattern of the product type
                  datasearch = str(searchpinsconfiguretion).split(" ") 
                  check2 = any(item in datasearch for item in Extracteddata)
                  packlist = PackagesLoad.get('package').get('rootpackages')
                  packdrawing = PackagesLoad.get('package').get('packagesdrawing')
                  boundary = ['0','1','2']
                  check0 = any(item in list(str(i)) for item in boundary) # Setting default check bundary 
                  if check0 == False:
                      print("Check false page")
                      if check2 == True:
                                  print("Found the Pins configuretion","page",str(i))
                                  #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                       #This is the starter page only ignite the starter loop 
                                  Packagecheck.append(str(i)) # Get the current page and detecting the other page in the search 
                                  tables = camelot.read_pdf(PATHMAIN +"/"+str(inputcomp)+".pdf",pages=str(i))
                                  if len(tables) == 0: 
                                         print("Not Found the data table",len(tables))
                                         for i in range(0,len(packlist)):
                                          check = any(item in wordninja.split(str(packlist[i])) for item in Extracteddata)
                                          print(check)
                                          try:
                                             if check == True: 
                                                   print(Extracteddata[Extracteddata.index(packlist[i])])
                                                   print(wordninja.split(str(packlist[i])),len(wordninja.split(str(packlist[i]))))
                                                   outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(wordninja.split(str(packlist[i])))]
                                                   check2 = any(item in wordninja.split(str(outputinterger)) for item in Extracteddata)
                                                   if outputinterger.strip().isdigit():
                                                         print("Output is Number")
                                                         print(outputinterger) #Get tge output here to calculate the page output data 
                                                   else:
                                                      print("Output is string")
                                                      if check2 == True:
                                                         print("Check loop 2")
                                                         if len(outputinterger) >1:
                                                              outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(wordninja.split(str(outputinterger)))+len(wordninja.split(str(packlist[i])))]
                                                              print(outputinterger)
                                                         if len(outputinterger) == 1: 
                                                              print("detected len integer")
                                                              outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(outputinterger)+len(wordninja.split(str(outputinterger)))+len(wordninja.split(str(packlist[i])))]
                                                              print(outputinterger)   
                                                              if int(outputinterger) <= 144:
                                                                      print("In the range of package pins=",outputinterger)

                                                                      #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>        
                                                                                    #Get the page calculation here 
                                                                      #one page output calculation   
                                                          
                                          except:
                                             print("This part is not found in the list package")
                                  if len(tables) >= 1:
                                         print("Found the data table",len(tables))
                                         print(tables[0].df)
                                         print(tables[0].parsing_report)
                                         tables[0].to_csv(EXTRACT +"/"+str(inputcomp)+'.csv') 
                                         #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                         print("Reading pandas....")
                                         df = pd.read_csv (r''+EXTRACT+"/"+str(inputcomp)+'.csv')
                                         print(df)
                                         print(Configure(listConfig[0])) # Get the data from the json file
                                         #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                         # Algorithm for classify the extraction of the text 
                                         index = df.index
                                         number_of_rows = len(index)
                                         print(number_of_rows)
                                         listdata = list(df.columns.values)
                                         print(listdata)
                                         extractionalgorithm(df,listdata,listConfig[0]) #running the function of the configuretion file function 

                                  break


                      break  
def Classifypagematch(input1,inputcomp,Pinsquantity,Packagecheck):
             print("Begin predict the next page")
             pageclassifylist = PackagesLoad.get("Pageclassify")
             #print(pageclassifylist)
             print(Packagecheck,Pinsquantity) # Show the input page variable and the pins quantity 
             val_list = list(pageclassifylist.values())  # Get the page classify list 
             print(val_list)
             for i in range(0,len(val_list)):
                    try: 
                        if int(val_list[i][0]) <= int(Pinsquantity[0]) <= int(val_list[i][1]): 
                           try:
                                 position = val_list.index(val_list[i])
                                 print("Array position",position)
                                 print(list(pageclassifylist)[position])
                                 if int(list(pageclassifylist)[position]) == 1:
                                         savenextpage = int(Packagecheck[0])+int(list(pageclassifylist)[position])-1
                                         Packagecheck.append(str(savenextpage))
                                         print(Packagecheck[0])      
                                         refpagecal.append(Packagecheck[0]) #Get the reference of the page  
                                 if int(list(pageclassifylist)[position]) >= 2:
                                         
                                         refpage =  int(Packagecheck[0])+int(list(pageclassifylist)[position])-1 # ref starter page 
                                         savenextpage = int(Packagecheck[0])+int(list(pageclassifylist)[position])
                                         Packagecheck.clear() # Clear the recent page before append the new page 
                                         Packagecheck.append(str(savenextpage))
                                         print(refpage) # Get the reference starter page 
                                         print(Packagecheck[0])      
                                         refpagecal.append(refpage) #Get the reference of the page 
                                         #Pageclassification.append(refpagecal[0]) # replace the refernce page into the starter page
                                         nextpage.append(Packagecheck[0]) # Next page append 
                                         
                                                                 
                                 break
                           except:
                               print("Not in the list",str(i))
                    except: 
                        print("Not in the list",str(i))       
def Classifyselectionfunction(input1,inputcomp,Pinsquantity,Packagecheck,reftabledetect,combinedictdata): #Get the reftable for setting the condition function and the combination dictionary data for get the key and value of the ic  
                    print("Classify the reference detection",str(reftabledetect))
                    if str(reftabledetect) == '1':
                           print("Detected table in the page")
                           for w in range(0,len(list(combinedictdata))):
                                     print("#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                     print(str(w),list(combinedictdata)[w])
                                     pinsoutput = combinedictdata.get(str(list(combinedictdata)[w])).split(",")[1] # Get the pins out from the string to add the array value into the classification base 
                                     #Reference 
                                     refpins.append(pinsoutput)# add the reference pins and clear after running the new process 
                                     print("Pins number",refpins[0])
                                     Classifypagematch(input1,inputcomp,refpins,Packagecheck) #Get the refpins into the loop and calculate the page from the input estimation 
                                     #after add the estimation page delete the refpins to be ready for adding the new one
                                     refpins.clear() # Clear the refferent pins 

                                     print(refpagecal) # Adding the reference page int the array 
                                     
                                     print("#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                     
                    if str(reftabledetect) == '0': 
                           print("Not detected table in the page") 
                           Classifypagematch(input1,inputcomp,Pinsquantity,Packagecheck) #Get the refpins into the loop and calculate the page from the input estimation 
                            
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                      #Get the data sopecification function for the 
Tabledetector(input1,inputcomp,Pinsquantity) #Get the pins and quantity of the package specificatoin 
Pinsearchfunction(input1,inputcomp,searchpinsconfiguretion) #Get the pins function of the input pdf file 
print(list(Packagecheck))
print(list(Pinsquantity))
print(list(Devicesbucket))
print(list(Packagetypebucket))
print(list(Pinsbucket))
Bucketcombinefunc(Devicesbucket,Packagetypebucket,Pinsbucket) #Processing the json type data 
print(combinedictdata) #Get the combine data from the json file generated function 
print(reftabledetect,len(reftabledetect)) # Get the reference of the data table on the function 
Classifyselectionfunction(input1,inputcomp,Pinsquantity,Packagecheck,len(reftabledetect),combinedictdata)
print("Reference starter page",refpagecal) # Get the reference page 
print("Predict next page",Pageclassification)
