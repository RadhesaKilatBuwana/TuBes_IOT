import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt

def Peak_Accel_Treshold(data, timestamps, treshold):
	Last_State = 'below' #Below < treshold, above > treshold
	Crest_Troughs = 0
	Crossings = []
	
	for i, datum in enumerate(data):
		Current_State = Last_State
		if datum < treshold:
			Current_State = 'below'
		elif datum > treshold:
			Current_State = 'above'
		
		if Current_State is not Last_State:
			if Current_State is 'above'
				Crossing = [timestamps[i], treshold]
				Crossings.append(Crossing)
			else
				Crossing = [timestamps[i], treshold]
				Crossings.append(Crossing)
			Crest_Troughs += 1
		Last_State = Current_State
	return np.array(Crossings)

def Butter_Lowpass(Cutoff, FS, order=5):
	NYQ = 0.5 * FS
	Normal_Cutoff = Cutoff/NYQ
	b,a = butter(order, Normal_Cutoff, btype='low', analog=False)
	return b,a
	
def Butter_Lowpass_Filter(Data, Cutoff, FS, order=5):
	b,a = Butter_Lowpass(Cutoff, FS, order=order)
	y = lfilter(b, a, data)
	return y
	
def Show_graphs(Unfiltered, TimeStamps, Cutoff, FS, order=5):
	b, a = Butter_Lowpass(Cutoff, FS, order)
    # Frequency response graph
    w, h = freqz(b, a, worN=8000)
    plt.subplot(2, 1, 1)
    plt.plot(0.5 * FS * w / np.pi, np.abs(h), 'b')
    plt.plot(Cutoff, 0.5 * np.sqrt(2), 'ko')
    plt.axvline(Cutoff, color='k')
    plt.xlim(0, 0.5 * FS)
    plt.title("Lowpass Filter Frequency Response")
    plt.xlabel('Frequency [Hz]')
    plt.grid()
    Filtered = Butter_Lowpass_Filter(Unfiltered, Cutoff, FS, order)
    plt.subplot(2, 1, 2)
    plt.plot(Timestamps, Unfiltered, 'r-', label='unfiltered')
    plt.plot(Timestamps, Filtered, 'g-', linewidth=2, label='filtered')
    plt.xlabel('Time [sec]')
    plt.grid()
    plt.legend()
    plt.subplots_adjust(hspace=0.35)
    plt.show()