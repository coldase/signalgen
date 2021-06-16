import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from tkinter import *

class App:
	def __init__(self):
		self.root = Tk()
		self.root.geometry("350x300")
		self.root.title("WaveGenerator")
		self.freq_scale = Scale(self.root, orient=VERTICAL)
		self.amp_scale = Scale(self.root, orient=VERTICAL)
		self.seconds_scale = Scale(self.root, orient=VERTICAL, from_=0, to=10)
		self.samples_scale = Scale(self.root, orient=VERTICAL, from_=0, to=1000)

	def run(self):
		self.content()
		self.root.mainloop()

	def handle_click(self, case):
		freq = self.freq_scale.get()
		amp = self.amp_scale.get()
		seconds = self.seconds_scale.get()
		samples = self.samples_scale.get()
		self.make_plot(freq, amp, case, seconds, samples)

	def content(self):
		
		freg_lb = Label(self.root, text="Freq").place(x=39, y=25)
		amp_lb = Label(self.root, text="Amp").place(x=119, y=25)
		sec_lb = Label(self.root, text="Sec").place(x=200, y=25)
		Samples_lb = Label(self.root, text="Samples").place(x=269, y=25)

		self.freq_scale.place(x=20, y=50)
		self.amp_scale.place(x=100, y=50)
		self.seconds_scale.place(x=180, y=50)
		self.samples_scale.place(x=260, y=50)

		sine_btn = Button(self.root, text="Sine Wave", command=lambda: self.handle_click(1)).place(x=60, y=200, width=90)
		square_btn = Button(self.root, text="Square Wave", command=lambda: self.handle_click(2)).place(x=200, y=200, width=90)
	
	def make_plot(self, freq, amp, case, seconds, samples):
		time = np.linspace(0, seconds, samples)
		sine_wave = amp*np.sin(2*np.pi*freq*time)
		square_wave = amp*signal.square(2*np.pi*freq*time, duty=0.3)
		if case == 1:
			plt.plot(time, sine_wave)
		if case == 2:
			plt.plot(time, square_wave)
		plt.xlabel('Time (s)')
		plt.ylabel('Amplitude')
		plt.show()

generator = App()

if __name__ == "__main__":
	generator.run()