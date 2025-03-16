import matplotlib.pyplot as plt
import numpy as np

def plot_melody(melody_notes, note_durations=None):
    """
    Plots the melody as a piano roll.

    Parameters:
        melody_notes (list of int): List of MIDI note numbers.
        note_durations (list of float, optional): Durations for each note in seconds.
    """
    # If no durations are provided, default to 0.5 seconds for each note
    if note_durations is None:
        note_durations = [0.5] * len(melody_notes)

    # Create a new figure for plotting
    fig, ax = plt.subplots(figsize=(12, 5))

    # Calculate start and end times for each note
    note_start_times = []
    note_end_times = []
    start_time = 0.0
    for duration in note_durations:
        note_start_times.append(start_time)
        note_end_times.append(start_time + duration)
        start_time = note_end_times[-1]

    # Set the range for Y-axis (MIDI note numbers)
    min_pitch = min(melody_notes) - 2
    max_pitch = max(melody_notes) + 2

    # Plot each note
    for start, end, note in zip(note_start_times, note_end_times, melody_notes):
        ax.plot([start, end], [note, note], linewidth=10, color='black')  # Plot notes in black

    # Set axis labels and title
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("MIDI Note Number")
    ax.set_title("Piano Roll Visualization")

    # Y-axis: MIDI notes
    ax.set_yticks(range(min_pitch, max_pitch + 1))
    ax.set_ylim([min_pitch, max_pitch])
    ax.yaxis.grid(True, linestyle='--', linewidth=0.5)

    # X-axis: Time (with grid)
    max_time = max(note_end_times) if note_end_times else 1
    ax.set_xticks(np.arange(0, max_time + 0.5, 0.5))
    ax.set_xlim([0, max_time])
    ax.xaxis.grid(True, linestyle='--', linewidth=0.5)

    # Show the plot
    plt.show()

