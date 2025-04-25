import os
import subprocess
import urllib.request
import pretty_midi
from IPython.display import Audio, display
from ipywidgets import Button
from google.colab import files

import os
import urllib.request
import subprocess

# Check everything
print("🔍 MIDI exists:", os.path.exists("my_chords.mid"))
print("🔍 SoundFont exists:", os.path.exists("/content/FluidR3_GM.sf2"))

# Try converting manually and capture result
print("🔨 Running FluidSynth...")
result = os.system("fluidsynth -ni /content/FluidR3_GM.sf2 my_chords.mid -F my_chords.wav -r 44100")
print("✅ fluidsynth result code:", result)
print("🎧 WAV created:", os.path.exists("my_chords.wav"))


# Install fluidsynth (safe to rerun in Colab)
subprocess.call(['apt-get', 'install', '-y', 'fluidsynth'])

# SoundFont location and URL
soundfont_path = "/content/FluidR3_GM.sf2"
soundfont_url = "https://www.dropbox.com/scl/fi/ruczr63ev3ac4xxi3q9fd/FluidR3_GM.sf2?rlkey=ih7q2m0vpp5cvvjxq1cq3s23i&dl=1"

# Ensure SoundFont exists
if not os.path.exists(soundfont_path):
    print("🎵 Downloading SoundFont...")
    urllib.request.urlretrieve(soundfont_url, soundfont_path)
else:
    print("🎵 SoundFont already exists.")


def save_and_play(midi_object, filename="output.mid", show_info=None):
    """
    Saves a PrettyMIDI object, renders to audio, plays in Colab,
    and shows a download button for the MIDI file.
    """
    # Save MIDI
    midi_object.write(filename)

    # Render MIDI to WAV
    wav_filename = filename.replace(".mid", ".wav")
    result = os.system(f"fluidsynth -ni {soundfont_path} {filename} -F {wav_filename} -r 44100")

    # Check if rendering worked
    if not os.path.exists(wav_filename):
        print("❌ fluidsynth failed to create WAV file.")
        return

    # Play audio
    display(Audio(filename=wav_filename, rate=44100))

    # Print parameters if provided
    if show_info:
        print("🎛️ Parameters used:")
        for k, v in show_info.items():
            print(f" - {k}: {v}")

    # Download button for MIDI file
    button = Button(description="⬇️ Download MIDI File")
    button.on_click(lambda b: files.download(filename))
    display(button)
