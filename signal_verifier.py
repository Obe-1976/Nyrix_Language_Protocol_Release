import os
import hashlib
import wave
import contextlib

AUDIO_DIR = "../audio"

def hash_file(filepath):
    with open(filepath, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def analyze_audio_file(filepath):
    try:
        with contextlib.closing(wave.open(filepath, 'rb')) as wf:
            frames = wf.getnframes()
            rate = wf.getframerate()
            duration = frames / float(rate)
            channels = wf.getnchannels()
            sample_width = wf.getsampwidth()
            return {
                "channels": channels,
                "sample_width": sample_width,
                "frame_rate": rate,
                "duration_seconds": round(duration, 2)
            }
    except wave.Error:
        return {"error": "Unsupported file format or not a .wav"}

def main():
    print("🔍 NYRIXAI Drift Signal Verifier")
    print("Scanning folder:", AUDIO_DIR)
    for filename in os.listdir(AUDIO_DIR):
        if filename.endswith(".mp3") or filename.endswith(".wav"):
            full_path = os.path.join(AUDIO_DIR, filename)
            print(f"\n🎧 File: {filename}")
            print("SHA-256 Hash:", hash_file(full_path))
            analysis = analyze_audio_file(full_path)
            for k, v in analysis.items():
                print(f"{k.capitalize()}: {v}")

if __name__ == "__main__":
    main()