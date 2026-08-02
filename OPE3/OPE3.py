import librosa
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

SR = 22050  # common sample rate to resample everything to
 
original, _      = librosa.load("original.mp3", sr=SR, mono=True)
karaoke, _        = librosa.load("karaoke.mp3", sr=SR, mono=True)
different_song, _ = librosa.load("different_song.mp3", sr=SR, mono=True)
 

def match_length(a, b):
    n = min(len(a), len(b))
    return a[:n], b[:n]
 
def normalize(x):
    return x / (np.max(np.abs(x)) + 1e-9)
 
original      = normalize(original)
karaoke       = normalize(karaoke)
different_song = normalize(different_song)
 

def normalized_cross_correlation(x, y):
    x, y = match_length(x, y)
    x = x - np.mean(x)
    y = y - np.mean(y)
    corr = signal.correlate(x, y, mode="full")
    corr /= (np.linalg.norm(x) * np.linalg.norm(y) + 1e-9)
    lag = np.argmax(np.abs(corr)) - (len(x) - 1)
    return corr, lag, np.max(np.abs(corr))
 
corr_orig_karaoke, lag1, peak1 = normalized_cross_correlation(original, karaoke)
corr_orig_diff, lag2, peak2    = normalized_cross_correlation(original, different_song)
corr_karaoke_diff, lag3, peak3 = normalized_cross_correlation(karaoke, different_song)
 
print("=== TIME-DOMAIN CROSS-CORRELATION (peak, aligned lag) ===")
print(f"Original  vs Karaoke        : peak={peak1:.4f}  lag={lag1} samples")
print(f"Original  vs Different Song : peak={peak2:.4f}  lag={lag2} samples")
print(f"Karaoke   vs Different Song : peak={peak3:.4f}  lag={lag3} samples")

def pearson(x, y):
    x, y = match_length(x, y)
    return np.corrcoef(x, y)[0, 1]
 
pearson_ok = pearson(original, karaoke)
pearson_od = pearson(original, different_song)
pearson_kd = pearson(karaoke, different_song)
 
print("\n=== PEARSON CORRELATION COEFFICIENT (raw waveform) ===")
print(f"Original  vs Karaoke        : r = {pearson_ok:.4f}")
print(f"Original  vs Different Song : r = {pearson_od:.4f}")
print(f"Karaoke   vs Different Song : r = {pearson_kd:.4f}")
 

def feature_correlation(x, y, feature="mfcc"):
    x, y = match_length(x, y)
    if feature == "mfcc":
        fx = librosa.feature.mfcc(y=x, sr=SR, n_mfcc=13)
        fy = librosa.feature.mfcc(y=y, sr=SR, n_mfcc=13)
    else:  # chroma
        fx = librosa.feature.chroma_stft(y=x, sr=SR)
        fy = librosa.feature.chroma_stft(y=y, sr=SR)
    n = min(fx.shape[1], fy.shape[1])
    fx, fy = fx[:, :n].flatten(), fy[:, :n].flatten()
    return np.corrcoef(fx, fy)[0, 1]
 
mfcc_ok = feature_correlation(original, karaoke, "mfcc")
mfcc_od = feature_correlation(original, different_song, "mfcc")
mfcc_kd = feature_correlation(karaoke, different_song, "mfcc")
 
chroma_ok = feature_correlation(original, karaoke, "chroma")
chroma_od = feature_correlation(original, different_song, "chroma")
chroma_kd = feature_correlation(karaoke, different_song, "chroma")
 
print("\n=== MFCC-BASED CORRELATION (timbre similarity) ===")
print(f"Original  vs Karaoke        : r = {mfcc_ok:.4f}")
print(f"Original  vs Different Song : r = {mfcc_od:.4f}")
print(f"Karaoke   vs Different Song : r = {mfcc_kd:.4f}")
 
print("\n=== CHROMA-BASED CORRELATION (harmonic/pitch similarity) ===")
print(f"Original  vs Karaoke        : r = {chroma_ok:.4f}")
print(f"Original  vs Different Song : r = {chroma_od:.4f}")
print(f"Karaoke   vs Different Song : r = {chroma_kd:.4f}")
 

fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)
axs[0].plot(original[:SR*10], color="steelblue")
axs[0].set_title("Original Song (first 10 s)")
axs[1].plot(karaoke[:SR*10], color="seagreen")
axs[1].set_title("Karaoke / Music-only Version (first 10 s)")
axs[2].plot(different_song[:SR*10], color="indianred")
axs[2].set_title("Completely Different Song (first 10 s)")
plt.tight_layout()
plt.savefig("waveform_comparison.png", dpi=150)
plt.show()
 
labels = ["Orig-Karaoke", "Orig-Different", "Karaoke-Different"]
pearson_vals = [pearson_ok, pearson_od, pearson_kd]
mfcc_vals    = [mfcc_ok, mfcc_od, mfcc_kd]
chroma_vals  = [chroma_ok, chroma_od, chroma_kd]
 
x = np.arange(len(labels))
width = 0.25
plt.figure(figsize=(8, 5))
plt.bar(x - width, pearson_vals, width, label="Waveform (Pearson)")
plt.bar(x,          mfcc_vals,    width, label="MFCC (Timbre)")
plt.bar(x + width,  chroma_vals,  width, label="Chroma (Harmony)")
plt.xticks(x, labels)
plt.ylabel("Correlation coefficient (r)")
plt.title("Correlation Comparison Across Track Pairs")
plt.legend()
plt.tight_layout()
plt.savefig("correlation_bar_chart.png", dpi=150)
plt.show()
