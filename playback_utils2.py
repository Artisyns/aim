
import os
import subprocess
import urllib.request
import pretty_midi
from IPython.display import Audio, display
from ipywidgets import Button
from google.colab import files

# Constants
SOUNDFONT_PATH = "/content/FluidR3_GM.sf2"
SOUNDFONT_URL = "https://ftp.osuosl.org/pub/musescore/soundfont/FluidR3_GM.sf2"

def ensure_fluidsynth_installed():
    """Ensure that fluidsynth is installed."""
    subprocess.call(['apt-get', 'install', '-y', 'fluidsynth'])

def ensure_soundfont_exists(path=SOUNDFONT_PATH, url=SOUNDFONT_URL):
    """Download the SoundFont if it does not exist."""
    if not os.path.exists(path):
        print("🎵 Downloading SoundFont...")
        urllib.request.urlretrieve(url, path)
    else:
        print("🎵 SoundFont already exists.")

def save_and_play(midi_object, filename="output.mid", show_info=None):
    """
    Save a PrettyMIDI object to a file, convert it to WAV using fluidsynth, and play it.
    
    Parameters:
    - midi_object: pretty_midi.PrettyMIDI
    - filename: str
    - show_info: dict or None
    """
    ensure_fluidsynth_installed()
    ensure_soundfont_exists()

    # Save MIDI file
    midi_object.write(filename)

    # Convert to WAV
    wav_filename = filename.replace(".mid", ".wav")
    result = subprocess.run(["fluidsynth", "-ni", SOUNDFONT_PATH, filename, "-F", wav_filename, "-r", "44100"])

    if result.returncode != 0 or not os.path.exists(wav_filename):
        print("❌ Failed to create WAV file. Check fluidsynth and MIDI input.")
        return

    # Playback
    display(Audio(filename=wav_filename, rate=44100))

    # Print metadata
    if show_info:
        print("🎛️ Parameters used:")
        for k, v in show_info.items():
            print(f" - {k}: {v}")

    # Download button
    button = Button(description="⬇️ Download MIDI File")
    button.on_click(lambda b: files.download(filename))
    display(button)
