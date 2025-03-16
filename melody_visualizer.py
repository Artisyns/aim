import matplotlib.pyplot as plt
import numpy as np

def plot_melody(melody_notes, note_durations=None):
    """
    Plots the melody as a piano roll using Matplotlib, ensuring no unintended overlap.

    Parameters:
        melody_notes (list of int): List of MIDI note numbers.
        note_durations (list of float, optional): Durations for each note in seconds.
                                                  If None, all notes default to 0.5 seconds.
    """
    # Close previous figure to prevent overlapping
    plt.close('all')
    
    # Create a new figure and axis
    fig, ax = plt.subplots(figsize=(12, 5))
    
    # Set default durations if none are provided
    if note_durations is None:
        note_durations = [0.5] * len(melody_notes)

    start_time = 0.0  # Initialize start time for the first note
    note_start_times = []
    note_end_times = []

    # Collect note timing data
    for duration in note_durations:
        note_start_times.append(start_time)
        note_end_times.append(start_time + duration)
        start_time = note_end_times[-1]  # Set the start time of the next note after the previous note's end

    # Ensure proper grid spacing for Y-axis (MIDI notes)
    min_pitch = min(melody_notes) - 2
    max_pitch = max(melody_notes) + 2

    # Plot each note with its correct start and end times
    for start, end, note in zip(note_start_times, note_end_times, melody_notes):
        ax.plot([start, end], [note, note], linewidth=10, color='black')  # Notes in black

    # Set axis labels and title
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("MIDI Note Number")
    ax.set_title("Piano Roll Visualization")

    # Align Y-axis (MIDI notes) with grid
    ax.set_yticks(range(min_pitch, max_pitch + 1))  # MIDI note numbers
    ax.set_ylim([min_pitch, max_pitch])  # Y-axis range
    ax.yaxis.grid(True, linestyle='--', linewidth=0.5)  # Horizontal grid lines

    # Align X-axis (time) with grid
    max_time = max(note_end_times) if note_end_times else 1
    ax.set_xticks(np.arange(0, max_time + 0.5, 0.5))  # Time grid every 0.5s
    ax.set_xlim([0, max_time])  # Time range
    ax.xaxis.grid(True, linestyle='--', linewidth=0.5)  # Vertical grid lines

    # Show the updated plot
    plt.show()
