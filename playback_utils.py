
import os
import pretty_midi
from IPython.display import Audio, display
from ipywidgets import Button
from google.colab import files

# Default SoundFont path – must exist in the environment
soundfont_url = "https://www.dropbox.com/scl/fi/ruczr63ev3ac4xxi3q9fd/FluidR3_GM.sf2?rlkey=ih7q2m0vpp5cvvjxq1cq3s23i&dl=1"
soundfont_path = "/content/FluidR3_GM.sf2"

def save_and_play(midi_object, filename="output.mid", show_info=None):
    """
    Saves a PrettyMIDI object, renders to audio, plays in Colab,
    and shows a download button for the MIDI file.
    """
    midi_object.write(filename)
    wav_filename = filename.replace(".mid", ".wav")
    os.system(f"fluidsynth -ni {soundfont_path} {filename} -F {wav_filename} -r 44100")
    display(Audio(filename=wav_filename, rate=44100))

    if show_info:
        print("🎛️ Parameters used:")
        for k, v in show_info.items():
            print(f" - {k}: {v}")

    # Download button
    button = Button(description="⬇️ Download MIDI File")
    button.on_click(lambda b: files.download(filename))
    display(button)
