import time
import serial
from matplotlib import pyplot
import matplotlib.pyplot as plt

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=115200,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)

plt.ion()
class DynamicUpdate():
    #Suppose we know the x range
    #min_x = 0
    #max_x = 500

    def on_launch(self):
        #Set up plot
        self.figure, self.ax = plt.subplots()
        self.lines, = self.ax.plot([],[])
        #Autoscale on unknown axis and known lims on the other
        self.ax.set_autoscaley_on(True)
        self.ax.set_autoscalex_on(True)

        #self.ax.set_xlim(self.min_x, self.max_x)
        #Other stuff
        self.ax.grid()
        ...

    def on_running(self, xdata, ydata):
        #Update data (with the new _and_ the old points)
        self.lines.set_xdata(xdata)
        self.lines.set_ydata(ydata)
        #Need both of these in order to rescale
        self.ax.relim()
        self.ax.autoscale_view()
        #We need to draw *and* flush
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()

    #Example
    def __call__(self):
        import numpy as np
        import time
        global time_zero
        self.on_launch()
        
        time.sleep(0.05)
    
d = DynamicUpdate()
time_zero = time.time()
xdata = []
ydata = []
d()
while 1 :
    
    raw=ser.readline().decode()
    pos=int(raw[9:17])
    diff=int(raw[24:-2])
    print(pos, ",",diff)
    xdata.append(time.time()-time_zero)
    ydata.append(pos)
    d.on_running(xdata, ydata)




