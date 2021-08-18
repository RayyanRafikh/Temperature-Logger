import datetime as dt
from matplotlib import pyplot as plt
from matplotlib import animation as animation
from MCP3008 import MCP3008
import csv
from csv import reader

#Configure three MCP3008 ADCs, two to be used with two chip select pins of the first Hardware SPI bus, and the third to be used with the first chip select pin of the second Hardware SPI bus.
adc1 = MCP3008(bus=0, device=0)#1st MCP3008
adc2 = MCP3008(bus=0,device=1)#2nd MCP3008
adc3 = MCP3008(bus=1,device=0)#3rd MCP3008

#Initialise a dictionary for taking values from the MCP3008 boards, then converting them into temperatures, and saving them again into the same dictionary
tdict = {}

#define a list of abscissas and ordinatesto be used as formal parameters for the animate_{i} function
xs = []
ys = []

#input voltage
vin = 5

#known input resistance for voltage divider
r1 = 3300

#Parameters of the PT100 sensor used
r0 = 100
t0 = 0
alpha = 0.003851

#Initialise 5 figures(windows) each for displaying live plots(animation) of temperatures of 4 different refrigerators
for i in range(5):
    globals()[f"fig_{i}"] = plt.figure()

#Set each figure to display live plots of 4 refrigerators each
a0 = fig_0.add_subplot(2,2,1)
a1 = fig_0.add_subplot(2,2,2)
a2 = fig_0.add_subplot(2,2,3)
a3 = fig_0.add_subplot(2,2,4)
a4 = fig_1.add_subplot(2,2,1)
a5 = fig_1.add_subplot(2,2,2)
a6 = fig_1.add_subplot(2,2,3)
a7 = fig_1.add_subplot(2,2,4)
a8 = fig_2.add_subplot(2,2,1)
a9 = fig_2.add_subplot(2,2,2)
a10 = fig_2.add_subplot(2,2,3)
a11 = fig_2.add_subplot(2,2,4)
a12 = fig_3.add_subplot(2,2,1)
a13 = fig_3.add_subplot(2,2,2)
a14 = fig_3.add_subplot(2,2,3)
a15 = fig_3.add_subplot(2,2,4)
a16 = fig_4.add_subplot(2,2,1)
a17 = fig_4.add_subplot(2,2,2)
a18 = fig_4.add_subplot(2,2,3)
a19 = fig_4.add_subplot(2,2,4)


for i in range(20):

    #creating 20 lists each for temperature values from 20 refrigerators
    globals()[f"y{i}"] = []

    #creating 20 lists each for timestamp values corresponding to the temperature values
    globals()[f"x{i}"] = []
    


#define animate function separately for each live plot which will be called continuously for each animation
def animate_0(i,xs,ys):
    
    #formula for computing the temperature value from the sensor ADC value
    tdict[0] = (((r1*(1/((vin/(((adc1.read(channel = 0))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    
    #Adding the latest temperature values and corresponding time stamps to separate lists xs and ys respectively
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[0])
    
    #define the fieldnames for values to be entered in csv file
    fieldnames = ['Time', 'Temperature']
    
    #try to open and read the csv file if it exists
    try :
        with open('fridge_1.csv', mode = 'r') as read_obj :
            csv_reader = reader(read_obj)
            
            # if the first row, i.e. the fieldnames are not present in the csv file, lower the flag, otherwise raise it
            if fieldnames not in csv_reader :
                k = 0
            else :
                k = 1
    #if the csv file doesnt exist, make one and append the first row as fieldnames and raise the flag            
    except :
        with open('fridge_1.csv', mode='w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(fieldnames)
            k = 1
    
    #open the csv file in writing mode
    with open('fridge_1.csv', mode='a') as csv_file: 
        writer = csv.writer(csv_file)
        
        #append the fieldnames in the first row only if the flag is not raised
        if k == 0:
            writer.writerow(fieldnames)
        
        #append the temperature values row by row after the fieldnames
        writer.writerow([dt.datetime.now().strftime('%H:%M:%S.%f'),tdict[0]])
        
    #maintains only the last 3 values in the lists            
    xs = xs[-3:]
    ys = ys[-3:]
    
    #refresh the plot
    a0.clear()
    
    #plot the animation in the figure
    a0.plot(xs,ys)
    
    #adjust the padding of the subplots
    plt.subplots_adjust(bottom=0.30)
    
    #Set the title, xlabel and ylabel for each subplot
    a0.set_title('Refrigerator 1')
    a0.set_ylabel('Temperature(deg C)')

def animate_1(i,xs,ys):
    tdict[1] = (((r1*(1/((vin/(((adc1.read(channel = 1))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[1])
    fieldnames = ['Time', 'Temperature']
    try :
        with open('fridge_2.csv', mode = 'r') as read_obj :
            csv_reader = reader(read_obj)
            if fieldnames not in csv_reader :
                k = 0
            else :
                k = 1                  
    except :
        with open('fridge_2.csv', mode='w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(fieldnames)
            k = 1
    with open('fridge_2.csv', mode='a') as csv_file:
        writer = csv.writer(csv_file)
        if k == 0:
            writer.writerow(fieldnames)
        writer.writerow([dt.datetime.now().strftime('%H:%M:%S.%f'),tdict[1]])   
    xs = xs[-3:]
    ys = ys[-3:]
    a1.clear()
    a1.plot(xs,ys)
    plt.subplots_adjust(bottom=0.30)
    a1.set_title('Refrigerator 2')

def animate_2(i,xs,ys):
    tdict[2] = (((r1*(1/((vin/(((adc1.read(channel = 2))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[2])
    fieldnames = ['Time', 'Temperature']
    try :
        with open('fridge_3.csv', mode = 'r') as read_obj :
            csv_reader = reader(read_obj)
            if fieldnames not in csv_reader :
                k = 0
            else :
                k = 1                  
    except :
        with open('fridge_3.csv', mode='w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(fieldnames)
            k = 1     
    with open('fridge_3.csv', mode='a') as csv_file: 
        writer = csv.writer(csv_file)
        if k == 0:
            writer.writerow(fieldnames)
        writer.writerow([dt.datetime.now().strftime('%H:%M:%S.%f'),tdict[2]])
    xs = xs[-3:]
    ys = ys[-3:]
    a2.clear()
    a2.plot(xs,ys)
    plt.subplots_adjust(bottom = 0.30)
    a2.set_title('Refrigerator 3')
    a2.set_ylabel('Temperature(deg C)')
    a2.set_xlabel('Time')

def animate_3(i,xs,ys):
    tdict[3] = (((r1*(1/((vin/(((adc1.read(channel = 3))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[3])
    fieldnames = ['Time', 'Temperature']
    try :
        with open('fridge_4.csv', mode = 'r') as read_obj :
            csv_reader = reader(read_obj)
            if fieldnames not in csv_reader :
                k = 0
            else :
                k = 1                  
    except :
        with open('fridge_4.csv', mode='w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(fieldnames)
            k = 1
    with open('fridge_4.csv', mode='a') as csv_file: 
        writer = csv.writer(csv_file)
        if k == 0:
            writer.writerow(fieldnames)
        writer.writerow([dt.datetime.now().strftime('%H:%M:%S.%f'),tdict[3]])
    xs = xs[-3:]
    ys = ys[-3:]
    a3.clear()
    a3.plot(xs,ys)
    plt.subplots_adjust(bottom=0.30)
    a3.set_title('Refrigerator 4')
    a3.set_xlabel('Time')

def animate_4(i,xs,ys):
    tdict[4] = (((r1*(1/((vin/(((adc1.read(channel = 4))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[4])
    fieldnames = ['Time', 'Temperature']
    try :
        with open('fridge_5.csv', mode = 'r') as read_obj :
            csv_reader = reader(read_obj)
            if fieldnames not in csv_reader :
                k = 0
            else :
                k = 1                  
    except :
        with open('fridge_5.csv', mode='w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(fieldnames)
            k = 1   
    with open('fridge_5.csv', mode='a') as csv_file: 
        writer = csv.writer(csv_file)
        if k == 0:
            writer.writerow(fieldnames)
        writer.writerow([dt.datetime.now().strftime('%H:%M:%S.%f'),tdict[4]])
    xs = xs[-3:]
    ys = ys[-3:]
    a4.clear()
    a4.plot(xs,ys)
    plt.subplots_adjust(bottom=0.30)
    a4.set_title('Refrigerator 5')
    a4.set_ylabel('Temperature(deg C)')

def animate_5(i,xs,ys):
    tdict[5] = (((r1*(1/((vin/(((adc1.read(channel = 5))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[5])
    fieldnames = ['Time', 'Temperature']
    try :
        with open('fridge_6.csv', mode = 'r') as read_obj :
            csv_reader = reader(read_obj)
            if fieldnames not in csv_reader :
                k = 0
            else :
                k = 1                  
    except :
        with open('fridge_6.csv', mode='w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(fieldnames)
            k = 1      
    with open('fridge_6.csv', mode='a') as csv_file: 
        writer = csv.writer(csv_file)
        if k == 0:
            writer.writerow(fieldnames)
        writer.writerow([dt.datetime.now().strftime('%H:%M:%S.%f'),tdict[5]])   
    xs = xs[-3:]
    ys = ys[-3:]
    a5.clear()
    a5.plot(xs,ys)
    plt.subplots_adjust(bottom=0.30)
    a5.set_title('Refrigerator 6')

def animate_6(i,xs,ys):
    tdict[6] = (((r1*(1/((vin/(((adc1.read(channel = 6))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[6])
    fieldnames = ['Time', 'Temperature']
    try :
        with open('fridge_7.csv', mode = 'r') as read_obj :
            csv_reader = reader(read_obj)
            if fieldnames not in csv_reader :
                k = 0
            else :
                k = 1                  
    except :
        with open('fridge_7.csv', mode='w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(fieldnames)
            k = 1      
    with open('fridge_7.csv', mode='a') as csv_file: 
        writer = csv.writer(csv_file)
        if k == 0:
            writer.writerow(fieldnames)
        writer.writerow([dt.datetime.now().strftime('%H:%M:%S.%f'),tdict[6]])
    xs = xs[-3:]
    ys = ys[-3:]
    a6.clear()
    a6.plot(xs,ys)
    plt.subplots_adjust(bottom=0.30)
    a6.set_title('Refrigerator 7')
    a6.set_ylabel('Temperature(deg C)')
    a6.set_xlabel('Time')

def animate_7(i,xs,ys):
    tdict[7] = (((r1*(1/((vin/(((adc1.read(channel = 7))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[7])
    fieldnames = ['Time', 'Temperature']
    try :
        with open('fridge_8.csv', mode = 'r') as read_obj :
            csv_reader = reader(read_obj)
            if fieldnames not in csv_reader :
                k = 0
            else :
                k = 1                  
    except :
        with open('fridge_8.csv', mode='w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(fieldnames)
            k = 1    
    with open('fridge_8.csv', mode='a') as csv_file: 
        writer = csv.writer(csv_file)
        if k == 0:
            writer.writerow(fieldnames)
        writer.writerow([dt.datetime.now().strftime('%H:%M:%S.%f'),tdict[7]])
    xs = xs[-3:]
    ys = ys[-3:]
    a7.clear()
    a7.plot(xs,ys)
    plt.subplots_adjust(bottom=0.30)
    a7.set_title('Refrigerator 8')
    a7.set_xlabel('Time')

def animate_8(i,xs,ys):
    tdict[8] = (((r1*(1/((vin/(((adc2.read(channel = 0))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[8])
    fieldnames = ['Time', 'Temperature']
    try :
        with open('fridge_9.csv', mode = 'r') as read_obj :
            csv_reader = reader(read_obj)
            if fieldnames not in csv_reader :
                k = 0
            else :
                k = 1                  
    except :
        with open('fridge_9.csv', mode='w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(fieldnames)
            k = 1       
    with open('fridge_9.csv', mode='a') as csv_file:
        writer = csv.writer(csv_file)
        if k == 0:
            writer.writerow(fieldnames)
        writer.writerow([dt.datetime.now().strftime('%H:%M:%S.%f'),tdict[8]])  
    xs = xs[-3:]
    ys = ys[-3:]
    a8.clear()
    a8.plot(xs,ys)
    plt.subplots_adjust(bottom=0.30)
    a8.set_title('Refrigerator 9')
    a8.set_ylabel('Temperature(deg C)')

def animate_9(i,xs,ys):
    tdict[9] = (((r1*(1/((vin/(((adc2.read(channel = 1))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[9])
    fieldnames = ['Time', 'Temperature']
    try :
        with open('fridge_10.csv', mode = 'r') as read_obj :
            csv_reader = reader(read_obj)
            if fieldnames not in csv_reader :
                k = 0
            else :
                k = 1                  
    except :
        with open('fridge_10.csv', mode='w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(fieldnames)
            k = 1       
    with open('fridge_10.csv', mode='a') as csv_file:
        writer = csv.writer(csv_file)
        if k == 0:
            writer.writerow(fieldnames)
        writer.writerow([dt.datetime.now().strftime('%H:%M:%S.%f'),tdict[9]])  
    xs = xs[-3:]
    ys = ys[-3:]
    a9.clear()
    a9.plot(xs,ys)
    plt.subplots_adjust(bottom=0.30)
    a9.set_title('Refrigerator 10')

def animate_10(i,xs,ys):
    tdict[10] = (((r1*(1/((vin/(((adc2.read(channel = 2))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[10])
    fieldnames = ['Time', 'Temperature']
    try :
        with open('fridge_11.csv', mode = 'r') as read_obj :
            csv_reader = reader(read_obj)
            if fieldnames not in csv_reader :
                k = 0
            else :
                k = 1                  
    except :
        with open('fridge_11.csv', mode='w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(fieldnames)
            k = 1   
    with open('fridge_11.csv', mode='a') as csv_file:
        writer = csv.writer(csv_file)
        if k == 0:
            writer.writerow(fieldnames)
        writer.writerow([dt.datetime.now().strftime('%H:%M:%S.%f'),tdict[10]])    
    xs = xs[-3:]
    ys = ys[-3:]
    a10.clear()
    a10.plot(xs,ys)
    plt.subplots_adjust(bottom=0.30)
    a10.set_title('Refrigerator 11')
    a10.set_ylabel('Temperature(deg C)')
    a10.set_xlabel('Time')

def animate_11(i,xs,ys):
    tdict[11] = (((r1*(1/((vin/(((adc2.read(channel = 3))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[11])
    fieldnames = ['Time', 'Temperature']
    try :
        with open('fridge_12.csv', mode = 'r') as read_obj :
            csv_reader = reader(read_obj)
            if fieldnames not in csv_reader :
                k = 0
            else :
                k = 1                  
    except :
        with open('fridge_12.csv', mode='w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(fieldnames)
            k = 1       
    with open('fridge_12.csv', mode='a') as csv_file:
        writer = csv.writer(csv_file)
        if k == 0:
            writer.writerow(fieldnames)
        writer.writerow([dt.datetime.now().strftime('%H:%M:%S.%f'),tdict[11]])
    xs = xs[-3:]
    ys = ys[-3:]
    a11.clear()
    a11.plot(xs,ys)
    plt.subplots_adjust(bottom=0.30)
    a11.set_title('Refrigerator 12')
    a11.set_xlabel('Time')

def animate_12(i,xs,ys):
    tdict[12] = (((r1*(1/((vin/(((adc2.read(channel = 4))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[12])
    fieldnames = ['Time', 'Temperature']
    try :
        with open('fridge_13.csv', mode = 'r') as read_obj :
            csv_reader = reader(read_obj)
            if fieldnames not in csv_reader :
                k = 0
            else :
                k = 1                  
    except :
        with open('fridge_13.csv', mode='w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(fieldnames)
            k = 1       
    with open('fridge_13.csv', mode='a') as csv_file:
        writer = csv.writer(csv_file)
        if k == 0:
            writer.writerow(fieldnames)
        writer.writerow([dt.datetime.now().strftime('%H:%M:%S.%f'),tdict[12]])  
    xs = xs[-3:]
    ys = ys[-3:]
    a12.clear()
    a12.plot(xs,ys)
    plt.subplots_adjust(bottom=0.30)
    a12.set_title('Refrigerator 13')
    a12.set_ylabel('Temperature(deg C)')

def animate_13(i,xs,ys):
    tdict[13] = (((r1*(1/((vin/(((adc2.read(channel = 5))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[13])
    fieldnames = ['Time', 'Temperature']
    try :
        with open('fridge_14.csv', mode = 'r') as read_obj :
            csv_reader = reader(read_obj)
            if fieldnames not in csv_reader :
                k = 0
            else :
                k = 1                  
    except :
        with open('fridge_14.csv', mode='w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(fieldnames)
            k = 1    
    with open('fridge_14.csv', mode='a') as csv_file:
        writer = csv.writer(csv_file)
        if k == 0:
            writer.writerow(fieldnames)
        writer.writerow([dt.datetime.now().strftime('%H:%M:%S.%f'),tdict[13]])  
    xs = xs[-3:]
    ys = ys[-3:]
    a13.clear()
    a13.plot(xs,ys)
    plt.subplots_adjust(bottom=0.30)
    a13.set_title('Refrigerator 14')

def animate_14(i,xs,ys):
    tdict[14] = (((r1*(1/((vin/(((adc2.read(channel = 6))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[14])
    fieldnames = ['Time', 'Temperature']
    try :
        with open('fridge_15.csv', mode = 'r') as read_obj :
            csv_reader = reader(read_obj)
            if fieldnames not in csv_reader :
                k = 0
            else :
                k = 1                  
    except :
        with open('fridge_15.csv', mode='w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(fieldnames)
            k = 1    
    with open('fridge_15.csv', mode='a') as csv_file:
        writer = csv.writer(csv_file)
        if k == 0:
            writer.writerow(fieldnames)
        writer.writerow([dt.datetime.now().strftime('%H:%M:%S.%f'),tdict[14]])  
    xs = xs[-3:]
    ys = ys[-3:]
    a14.clear()
    a14.plot(xs,ys)
    plt.subplots_adjust(bottom=0.30)
    a14.set_title('Refrigerator 15')
    a14.set_ylabel('Temperature(deg C)')
    a14.set_xlabel('Time')

def animate_15(i,xs,ys):
    tdict[15] = (((r1*(1/((vin/(((adc2.read(channel = 7))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[15])
    fieldnames = ['Time', 'Temperature']
    try :
        with open('fridge_16.csv', mode = 'r') as read_obj :
            csv_reader = reader(read_obj)
            if fieldnames not in csv_reader :
                k = 0
            else :
                k = 1                  
    except :
        with open('fridge_16.csv', mode='w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(fieldnames)
            k = 1     
    with open('fridge_16.csv', mode='a') as csv_file:
        writer = csv.writer(csv_file)
        if k == 0:
            writer.writerow(fieldnames)
        writer.writerow([dt.datetime.now().strftime('%H:%M:%S.%f'),tdict[15]])
    xs = xs[-3:]
    ys = ys[-3:]
    a15.clear()
    a15.plot(xs,ys)
    plt.subplots_adjust(bottom=0.30)
    a15.set_title('Refrigerator 16')
    a15.set_xlabel('Time')

def animate_16(i,xs,ys):
    tdict[16] = (((r1*(1/((vin/(((adc3.read(channel = 0))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[16])
    fieldnames = ['Time', 'Temperature']
    try :
        with open('fridge_17.csv', mode = 'r') as read_obj :
            csv_reader = reader(read_obj)
            if fieldnames not in csv_reader :
                k = 0
            else :
                k = 1                  
    except :
        with open('fridge_17.csv', mode='w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(fieldnames)
            k = 1     
    with open('fridge_17.csv', mode='a') as csv_file:
        writer = csv.writer(csv_file)
        if k == 0:
            writer.writerow(fieldnames)
        writer.writerow([dt.datetime.now().strftime('%H:%M:%S.%f'),tdict[16]])   
    xs = xs[-3:]
    ys = ys[-3:]
    a16.clear()
    a16.plot(xs,ys)
    plt.subplots_adjust(bottom=0.30)
    a16.set_title('Refrigerator 17')
    a16.set_ylabel('Temperature(deg C)')

def animate_17(i,xs,ys):
    tdict[17] = (((r1*(1/((vin/(((adc3.read(channel = 1))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[17])
    fieldnames = ['Time', 'Temperature']
    try :
        with open('fridge_18.csv', mode = 'r') as read_obj :
            csv_reader = reader(read_obj)
            if fieldnames not in csv_reader :
                k = 0
            else :
                k = 1                  
    except :
        with open('fridge_18.csv', mode='w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(fieldnames)
            k = 1      
    with open('fridge_18.csv', mode='a') as csv_file:
        writer = csv.writer(csv_file)
        if k == 0:
            writer.writerow(fieldnames)
        writer.writerow([dt.datetime.now().strftime('%H:%M:%S.%f'),tdict[17]]) 
    xs = xs[-3:]
    ys = ys[-3:]
    a17.clear()
    a17.plot(xs,ys)
    plt.subplots_adjust(bottom=0.30)
    a17.set_title('Refrigerator 18')

def animate_18(i,xs,ys):
    tdict[18] = (((r1*(1/((vin/(((adc3.read(channel = 2))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[18])
    fieldnames = ['Time', 'Temperature']
    try :
        with open('fridge_19.csv', mode = 'r') as read_obj :
            csv_reader = reader(read_obj)
            if fieldnames not in csv_reader :
                k = 0
            else :
                k = 1                  
    except :
        with open('fridge_19.csv', mode='w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(fieldnames)
            k = 1   
    with open('fridge_19.csv', mode='a') as csv_file:
        writer = csv.writer(csv_file)
        if k == 0:
            writer.writerow(fieldnames)
        writer.writerow([dt.datetime.now().strftime('%H:%M:%S.%f'),tdict[18]])   
    xs = xs[-3:]
    ys = ys[-3:]
    a18.clear()
    a18.plot(xs,ys)
    plt.subplots_adjust(bottom=0.30)
    a18.set_title('Refrigerator 19')
    a18.set_ylabel('Temperature(deg C)')
    a18.set_xlabel('Time')

def animate_19(i,xs,ys):
    tdict[19] = (((r1*(1/((vin/(((adc3.read(channel = 3))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[19])
    fieldnames = ['Time', 'Temperature']
    try :
        with open('fridge_20.csv', mode = 'r') as read_obj :
            csv_reader = reader(read_obj)
            if fieldnames not in csv_reader :
                k = 0
            else :
                k = 1                  
    except :
        with open('fridge_20.csv', mode='w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(fieldnames)
            k = 1      
    with open('fridge_20.csv', mode='a') as csv_file:
        writer = csv.writer(csv_file)
        if k == 0:
            writer.writerow(fieldnames)
        writer.writerow([dt.datetime.now().strftime('%H:%M:%S.%f'),tdict[19]])  
    xs = xs[-3:]
    ys = ys[-3:]
    a19.clear()
    a19.plot(xs,ys)
    plt.subplots_adjust(bottom=0.30)
    a19.set_title('Refrigerator 20')
    a19.set_xlabel('Time')

#Setup live plots(animation) for each of the 20 plots in 5 different figures(windows)
ani_0 = animation.FuncAnimation(fig_0, animate_0, fargs=(x0,y0), interval=1000)
ani_1 = animation.FuncAnimation(fig_0, animate_1, fargs=(x1,y1), interval=1000)
ani_2 = animation.FuncAnimation(fig_0, animate_2, fargs=(x2,y2), interval=1000)
ani_3 = animation.FuncAnimation(fig_0, animate_3, fargs=(x3,y3), interval=1000)
ani_4 = animation.FuncAnimation(fig_1, animate_4, fargs=(x4,y4), interval=1000)
ani_5 = animation.FuncAnimation(fig_1, animate_5, fargs=(x5,y5), interval=1000)
ani_6 = animation.FuncAnimation(fig_1, animate_6, fargs=(x6,y6), interval=1000)
ani_7 = animation.FuncAnimation(fig_1, animate_7, fargs=(x7,y7), interval=1000)
ani_8 = animation.FuncAnimation(fig_2, animate_8, fargs=(x8,y8), interval=1000)
ani_9 = animation.FuncAnimation(fig_2, animate_9, fargs=(x9,y9), interval=1000)
ani_10 = animation.FuncAnimation(fig_2, animate_10, fargs=(x10,y10), interval=1000)
ani_11 = animation.FuncAnimation(fig_2, animate_11, fargs=(x11,y11), interval=1000)
ani_12 = animation.FuncAnimation(fig_3, animate_12, fargs=(x12,y12), interval=1000)
ani_13 = animation.FuncAnimation(fig_3, animate_13, fargs=(x13,y13), interval=1000)
ani_14 = animation.FuncAnimation(fig_3, animate_14, fargs=(x14,y14), interval=1000)
ani_15 = animation.FuncAnimation(fig_3, animate_15, fargs=(x15,y15), interval=1000)
ani_16 = animation.FuncAnimation(fig_4, animate_16, fargs=(x16,y16), interval=1000)
ani_17 = animation.FuncAnimation(fig_4, animate_17, fargs=(x17,y17), interval=1000)
ani_18 = animation.FuncAnimation(fig_4, animate_18, fargs=(x18,y18), interval=1000)
ani_19 = animation.FuncAnimation(fig_4, animate_19, fargs=(x19,y19), interval=1000)

#Initiate the live plot(animations)
plt.show()
