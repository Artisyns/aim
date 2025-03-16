import matplotlib.pyplot as plt
import numpy as np

def plot_piano_roll(melody_notes, note_durations=None):
    """
    Plots a piano roll visualization of the melody.

    Parameters:
        melody_notes (list of int): List of MIDI note numbers for the melody.
        note_durations (list of float, optional): Corresponding durations for each note in seconds.
                                                  If None, all notes default to 0.5 seconds.
    """
    # Set default durations if none are provided
    if note_durations is None:
        note_durations = [0.5] * len(melody_notes)  # Default to 0.5 seconds per note

    # Generate time axis
    start_times = np.cumsum([0] + note_durations[:-1])  # Calculate note start times

    # Create the piano roll plot
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.barh(melody_notes, note_durations, left=start_times, height=0.6, color='blue')

    ax.set_xlabel("Time (seconds)")
    ax.set_ylabel("MIDI Note Number")
    ax.set_title("Piano Roll Visualization")
    ax.set_yticks(range(min(melody_notes), max(melody_notes) + 1, 2))
    ax.grid(True, linestyle="--", alpha=0.6)

    plt.show()
