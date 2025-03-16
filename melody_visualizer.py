# -*- coding: utf-8 -*-
"""melody_visualizer.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ttm39O6bkK3-0BrlvuuE-tuJEmNKBflP
"""

import matplotlib.pyplot as plt
import numpy as np

def plot_melody(melody_notes, note_durations=None):
    """
    Plots the melody as a piano roll using Matplotlib.

    Parameters:
        melody_notes (list of int): List of MIDI note numbers.
        note_durations (list of float, optional): Durations for each note in seconds.
                                                  If None, all notes default to 0.5 seconds.
    """
    # Clear previous figure
    plt.clf()  # Clears the current figure
    
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

    # Create a piano roll plot
    fig, ax = plt.subplots(figsize=(6, 3))
    
    for i, (note, start, end) in enumerate(zip(melody_notes, note_start_times, note_end_times)):
        ax.plot([start, end], [note, note], linewidth=8, label=f'Note {i+1}' if i == 0 else "")

    ax.set_xlabel("Time (s)")
    ax.set_ylabel("MIDI Note Number")
    ax.set_title("Piano Roll Visualization")
    ax.grid(True)

    plt.show()

