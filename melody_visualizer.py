import matplotlib.pyplot as plt
import numpy as np

def plot_melody(melody_notes, note_durations=None):
    """
    Plots the melody as a piano roll using Matplotlib, with all notes in black, aligned to the grid, 
    and without overlapping previous notes.

    Parameters:
        melody_notes (list of int): List of MIDI note numbers.
        note_durations (list of float, optional): Durations for each note in seconds.
                                                  If None, all notes default to 0.5 seconds.
    """
    # Clear previous figure and create a new one
    plt.close('all')  # Closes all previous plots to avoid overlapping
    fig, ax = plt.subplots(figsize=(12, 5))
    
    # Set default durations if none are provided
    if note_durations is None:
        note_durations = [0.5] * len(melody_notes)

    start_time = 0.0  # Initialize start time
    note_start_times = []
    note_end_times = []

    # Collect note timing data
    for duration in note_durations:
        note_start_times.append(start_time)
        note_end_times.append(start_time + duration)
        start_time += duration

    # Plot the melody
    for start, end, note in zip(note_start_times, note_end_times, melody_notes):
        ax.plot([start, end], [note, note], linewidth=8, color='black')  # Draw notes in black

    # Set axis labels and title
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("MIDI Note Number")
    ax.set_title("Piano Roll Visualization")

    # Align the Y-axis (MIDI note numbers) with the grid
    ax.set_yticks(range(min(melody_notes) - 1, max(melody_notes) + 2))  # Set MIDI note ticks
    ax.yaxis.grid(True, linestyle='--', linewidth=0.5)  # Add horizontal grid lines

    # Align the X-axis (time) with the grid
    max_time = max(note_end_times) if note_end_times else 1
    ax.set_xticks(np.arange(0, max_time + 0.5, 0.5))  # Time grid every 0.5s
    ax.xaxis.grid(True, linestyle='--', linewidth=0.5)  # Add vertical grid lines

    plt.show()



