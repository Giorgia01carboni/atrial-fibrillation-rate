import numpy as np
import matplotlib.pyplot as plt

y = np.loadtxt('ecg_af.csv', delimiter=',')
Rpeaks = np.loadtxt('ecg_peaks.csv', delimiter=',')

plt.figure(figsize=(12, 7))
plt.plot(y, label='ECG Atrial Fibrillation')
plt.scatter(Rpeaks, y[Rpeaks.astype(int)], color='red', label='R-peaks')
plt.legend()
plt.title('ECG Atrial Fibrillation')
plt.show()

Rpeaks_length = len(Rpeaks)
row = Rpeaks_length
col = 360
qrst = np.zeros((row, col))
i = 0 #row index

for peak in Rpeaks:
    if peak >= 60 and peak < len(y) - 300:
      start = int(peak - 60)
      end = int(peak + 300)
      qrst[i, :] = y[start:end]
      i += 1

avg_qrst = np.mean(qrst, axis=0)
#print(len(avg_qrst))

plt.figure(figsize=(12, 7))
plt.plot(avg_qrst)
plt.title('Average QRS complex')
plt.show()