import pretty_midi
import matplotlib.pyplot as plt
import numpy as np

def plot_melody(melody_notes, note_durations=None):
    """
    Plots the melody as a piano roll using Matplotlib, ensuring no unintended overlap.
    It also generates the audio and plays it.

    Parameters:
        melody_notes (list of int): List of MIDI note numbers.
        note_durations (list of float, optional): Durations for each note in seconds.
                                                  If None, all notes default to 0.5 seconds.
    """
    # Initialize the start time for the first note
    start_time = 0.0

    # Create a PrettyMIDI object and an instrument (e.g., Acoustic Grand Piano)
    midi = pretty_midi.PrettyMIDI()
    instrument = pretty_midi.Instrument(program=0)  # Acoustic Grand Piano

    # Set default durations if none are provided
    if note_durations is None:
        note_durations = [0.5] * len(melody_notes)

    # Create Note objects with specified durations and add them to the instrument
    for note_number, duration in zip(melody_notes, note_durations):
        note = pretty_midi.Note(
            velocity=100,  # Note velocity (volume)
            pitch=note_number,  # MIDI note number
            start=start_time,  # Start time in seconds
            end=start_time + duration  # End time in seconds
        )
        instrument.notes.append(note)
        start_time += duration  # Update the start time for the next note

    # Add the instrument to the PrettyMIDI object
    midi.instruments.append(instrument)

    # Synthesize the audio
    audio = midi.synthesize()

    # Play the audio
    from IPython.display import Audio
    display(Audio(audio, rate=44100))

    # Now, let's visualize the melody as a piano roll
    # Initialize a figure for plotting
    plt.close('all')  # Close any previous figures
    fig, ax = plt.subplots(figsize=(12, 5))

    # Collect note start and end times for plotting
    note_start_times = []
    note_end_times = []

    # Calculate start and end times for each note
    start_time = 0.0  # Reset the start time for visualization
    for duration in note_durations:
        note_start_times.append(start_time)
        note_end_times.append(start_time + duration)
        start_time = note_end_times[-1]  # Update start time for the next note

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
