import datetime as dt
from matplotlib import pyplot as plt
from matplotlib import animation as animation
from MCP3008 import MCP3008
import csv

#Cofigure three MCP3008 ADCs, two to be used with two chip select pins of the first Hardware SPI bus, and the third to be used with the first chip select pin of the second Hardware SPI bus.
adc1 = MCP3008(bus=0, device=0)#1st MCP3008
adc2 = MCP3008(bus=0,device=1)#2nd MCP3008
adc3 = MCP3008(bus=1,device=0)#3rd MCP3008

#Initialise a dictionary for taking values from the MCP3008 boards and converting them into temperatures
tdict = {}

#define a list of abscissas and ordinatesto be used as formal parameters for the animate_{i} function
xs = []
ys = []

#input voltage
vin = 5

#input resistance
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
    

for i in range(21):
    
    #creating 20 lists each for temperature values from 20 refrigerators
    globals()[f"y{i}"] = []
    
    #creating 20 lists each for timestamp values corresponding to the temperature values
    globals()[f"x{i}"] = []

#define animate function separately for each live plot
def animate_0(i,xs,ys):
    tdict[0] = (((r1*(1/((vin/(((adc1.read(channel = 0))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[0])
    with open('temp_log_0.csv', mode='w') as csv_file:
        fieldnames = ['Time', 'Temperature']
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        
        writer.writeheader()
        writer.writerow({'Time': xs, 'Temperature': ys})
    xs[-20:]
    ys[-20:]
    a0.clear()
    a0.plot(xs,ys)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature of Refrigerator 1 over Time')
    plt.ylabel('Temperature(deg C)')
    plt.xlabel('Time')

def animate_1(i,xs,ys):
    tdict[1] = (((r1*(1/((vin/(((adc1.read(channel = 1))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[1])
    with open('temp_log_1.csv', mode='w') as csv_file:
        fieldnames = ['Time', 'Temperature']
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        
        writer.writeheader()
        writer.writerow({'Time': xs, 'Temperature': ys})
    xs[-20:]
    ys[-20:]
    a1.clear()
    a1.plot(xs,ys)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature of Refrigerator 2 over Time')
    plt.ylabel('Temperature(deg C)')
    plt.xlabel('Time')

def animate_2(i,xs,ys):
    tdict[2] = (((r1*(1/((vin/(((adc1.read(channel = 2))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[2])
    with open('temp_log_2.csv', mode='w') as csv_file:
        fieldnames = ['Time', 'Temperature']
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        
        writer.writeheader()
        writer.writerow({'Time': xs, 'Temperature': ys})
    xs[-20:]
    ys[-20:]
    a2.clear()
    a2.plot(xs,ys)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature of Refrigerator 3 over Time')
    plt.ylabel('Temperature(deg C)')
    plt.xlabel('Time')
    
def animate_3(i,xs,ys):
    tdict[3] = (((r1*(1/((vin/(((adc1.read(channel = 3))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[3])
    with open('temp_log_3.csv', mode='w') as csv_file:
        fieldnames = ['Time', 'Temperature']
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        
        writer.writeheader()
        writer.writerow({'Time': xs, 'Temperature': ys})
    xs[-20:]
    ys[-20:]
    a3.clear()
    a3.plot(xs,ys)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature of Refrigerator 4 over Time')
    plt.ylabel('Temperature(deg C)')
    plt.xlabel('Time')
   
def animate_4(i,xs,ys):
    tdict[4] = (((r1*(1/((vin/(((adc1.read(channel = 4))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[4])
    with open('temp_log_4.csv', mode='w') as csv_file:
        fieldnames = ['Time', 'Temperature']
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        
        writer.writeheader()
        writer.writerow({'Time': xs, 'Temperature': ys})
    xs[-20:]
    ys[-20:]
    a4.clear()
    a4.plot(xs,ys)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature of Refrigerator 5 over Time')
    plt.ylabel('Temperature(deg C)')
    plt.xlabel('Time')
    
def animate_5(i,xs,ys):
    tdict[5] = (((r1*(1/((vin/(((adc1.read(channel = 5))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[5])
    with open('temp_log_5.csv', mode='w') as csv_file:
        fieldnames = ['Time', 'Temperature']
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        
        writer.writeheader()
        writer.writerow({'Time': xs, 'Temperature': ys})
    xs[-20:]
    ys[-20:]
    a5.clear()
    a5.plot(xs,ys)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature of Refrigerator 6 over Time')
    plt.ylabel('Temperature(deg C)')
    plt.xlabel('Time')
    
def animate_6(i,xs,ys):
    tdict[6] = (((r1*(1/((vin/(((adc1.read(channel = 6))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[6])
    with open('temp_log_6.csv', mode='w') as csv_file:
        fieldnames = ['Time', 'Temperature']
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        
        writer.writeheader()
        writer.writerow({'Time': xs, 'Temperature': ys})
    xs[-20:]
    ys[-20:]
    a6.clear()
    a6.plot(xs,ys)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature of Refrigerator 7 over Time')
    plt.ylabel('Temperature(deg C)')
    plt.xlabel('Time')
    
def animate_7(i,xs,ys):
    tdict[7] = (((r1*(1/((vin/(((adc1.read(channel = 7))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[7])
    with open('temp_log_7.csv', mode='w') as csv_file:
        fieldnames = ['Time', 'Temperature']
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        
        writer.writeheader()
        writer.writerow({'Time': xs, 'Temperature': ys})
    xs[-20:]
    ys[-20:]
    a7.clear()
    a7.plot(xs,ys)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature of Refrigerator 8 over Time')
    plt.ylabel('Temperature(deg C)')
    plt.xlabel('Time')
    
def animate_8(i,xs,ys):
    tdict[8] = (((r1*(1/((vin/(((adc2.read(channel = 0))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[8])
    with open('temp_log_8.csv', mode='w') as csv_file:
        fieldnames = ['Time', 'Temperature']
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        
        writer.writeheader()
        writer.writerow({'Time': xs, 'Temperature': ys})
    xs[-20:]
    ys[-20:]
    a8.clear()
    a8.plot(xs,ys)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature of Refrigerator 9 over Time')
    plt.ylabel('Temperature(deg C)')
    plt.xlabel('Time')
    
def animate_9(i,xs,ys):
    tdict[9] = (((r1*(1/((vin/(((adc2.read(channel = 1))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[9])
    with open('temp_log_9.csv', mode='w') as csv_file:
        fieldnames = ['Time', 'Temperature']
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        
        writer.writeheader()
        writer.writerow({'Time': xs, 'Temperature': ys})
    xs[-20:]
    ys[-20:]
    a9.clear()
    a9.plot(xs,ys)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature of Refrigerator 10 over Time')
    plt.ylabel('Temperature(deg C)')
    plt.xlabel('Time')
    
def animate_10(i,xs,ys):
    tdict[10] = (((r1*(1/((vin/(((adc2.read(channel = 2))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[10])
    with open('temp_log_10.csv', mode='w') as csv_file:
        fieldnames = ['Time', 'Temperature']
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        
        writer.writeheader()
        writer.writerow({'Time': xs, 'Temperature': ys}) 
    xs[-20:]
    ys[-20:]
    a10.clear()
    a10.plot(xs,ys)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature of Refrigerator 11 over Time')
    plt.ylabel('Temperature(deg C)')
    plt.xlabel('Time')
    
def animate_11(i,xs,ys):
    tdict[11] = (((r1*(1/((vin/(((adc2.read(channel = 3))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[11])
    with open('temp_log_11.csv', mode='w') as csv_file:
        fieldnames = ['Time', 'Temperature']
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        
        writer.writeheader()
        writer.writerow({'Time': xs, 'Temperature': ys})
    xs[-20:]
    ys[-20:]
    a11.clear()
    a11.plot(xs,ys)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature of Refrigerator 12 over Time')
    plt.ylabel('Temperature(deg C)')
    plt.xlabel('Time')
    
def animate_12(i,xs,ys):
    tdict[12] = (((r1*(1/((vin/(((adc2.read(channel = 4))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[12])
    with open('temp_log_12.csv', mode='w') as csv_file:
        fieldnames = ['Time', 'Temperature']
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        
        writer.writeheader()
        writer.writerow({'Time': xs, 'Temperature': ys})
    xs[-20:]
    ys[-20:]
    a12.clear()
    a12.plot(xs,ys)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature of Refrigerator 13 over Time')
    plt.ylabel('Temperature(deg C)')
    plt.xlabel('Time')
    
def animate_13(i,xs,ys):
    tdict[13] = (((r1*(1/((vin/(((adc2.read(channel = 5))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[13])
    with open('temp_log_13.csv', mode='w') as csv_file:
        fieldnames = ['Time', 'Temperature']
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        
        writer.writeheader()
        writer.writerow({'Time': xs, 'Temperature': ys})
    xs[-20:]
    ys[-20:]
    a13.clear()
    a13.plot(xs,ys)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature of Refrigerator 14 over Time')
    plt.ylabel('Temperature(deg C)')
    plt.xlabel('Time')
    
def animate_14(i,xs,ys):
    tdict[14] = (((r1*(1/((vin/(((adc2.read(channel = 6))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[14])
    with open('temp_log_14.csv', mode='w') as csv_file:
        fieldnames = ['Time', 'Temperature']
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        
        writer.writeheader()
        writer.writerow({'Time': xs, 'Temperature': ys})
    xs[-20:]
    ys[-20:]
    a14.clear()
    a14.plot(xs,ys)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature of Refrigerator 15 over Time')
    plt.ylabel('Temperature(deg C)')
    plt.xlabel('Time')
    
def animate_15(i,xs,ys):
    tdict[15] = (((r1*(1/((vin/(((adc2.read(channel = 7))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[15])
    with open('temp_log_15.csv', mode='w') as csv_file:
        fieldnames = ['Time', 'Temperature']
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        
        writer.writeheader()
        writer.writerow({'Time': xs, 'Temperature': ys})
    xs[-20:]
    ys[-20:]
    a15.clear()
    a15.plot(xs,ys)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature of Refrigerator 16 over Time')
    plt.ylabel('Temperature(deg C)')
    plt.xlabel('Time')
    
def animate_16(i,xs,ys):
    tdict[16] = (((r1*(1/((vin/(((adc3.read(channel = 0))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[16])
    with open('temp_log_16.csv', mode='w') as csv_file:
        fieldnames = ['Time', 'Temperature']
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        
        writer.writeheader()
        writer.writerow({'Time': xs, 'Temperature': ys})
    xs[-20:]
    ys[-20:]
    a16.clear()
    a16.plot(xs,ys)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature of Refrigerator 17 over Time')
    plt.ylabel('Temperature(deg C)')
    plt.xlabel('Time')
    
def animate_17(i,xs,ys):
    tdict[17] = (((r1*(1/((vin/(((adc3.read(channel = 1))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[17])
    with open('temp_log_17.csv', mode='w') as csv_file:
        fieldnames = ['Time', 'Temperature']
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        
        writer.writeheader()
        writer.writerow({'Time': xs, 'Temperature': ys})
    xs[-20:]
    ys[-20:]
    a17.clear()
    a17.plot(xs,ys)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature of Refrigerator 18 over Time')
    plt.ylabel('Temperature(deg C)')
    plt.xlabel('Time')
    
def animate_18(i,xs,ys):
    tdict[18] = (((r1*(1/((vin/(((adc3.read(channel = 2))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[18])
    with open('temp_log_18.csv', mode='w') as csv_file:
        fieldnames = ['Time', 'Temperature']
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        
        writer.writeheader()
        writer.writerow({'Time': xs, 'Temperature': ys})
    xs[-20:]
    ys[-20:]
    a18.clear()
    a18.plot(xs,ys)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature of Refrigerator 19 over Time')
    plt.ylabel('Temperature(deg C)')
    plt.xlabel('Time')
    
def animate_19(i,xs,ys):
    tdict[19] = (((r1*(1/((vin/(((adc3.read(channel = 3))/1023)*3.3)) - 1))) + r0*((alpha*t0)-1))/(r0*alpha))
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(tdict[19])
    with open('temp_log_19.csv', mode='w') as csv_file:
        fieldnames = ['Time', 'Temperature']
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        
        writer.writeheader()
        writer.writerow({'Time': xs, 'Temperature': ys})
    xs[-20:]
    ys[-20:]
    a19.clear()
    a19.plot(xs,ys)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature of Refrigerator 20 over Time')
    plt.ylabel('Temperature(deg C)')
    plt.xlabel('Time')
    
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
