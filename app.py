import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from pydub import AudioSegment
import os

# Initialize Tkinter root
root = tk.Tk()
root.withdraw()  # Hide the root window

def get_time_in_ms(hhmmss):
    """Convert HHMMSS time format to milliseconds."""
    hh, mm, ss = map(int, hhmmss.split(":"))
    return (hh * 3600 + mm * 60 + ss) * 1000

def trim_audio(file_path, start_time, end_time, export_path):
    """Trim the audio file from start_time to end_time and save as MP3."""
    audio = AudioSegment.from_file(file_path)
    start_ms = get_time_in_ms(start_time)
    end_ms = get_time_in_ms(end_time)
    
    trimmed_audio = audio[start_ms:end_ms]
    trimmed_audio.export(export_path, format="mp3")

def main():
    # Ask the user to select audio files
    file_paths = filedialog.askopenfilenames(
        title="Select Audio Files",
        filetypes=(("Audio Files", "*.mp3 *.wav *.flac"), ("All Files", "*.*"))
    )

    if not file_paths:
        messagebox.showinfo("No File Selected", "No audio files were selected.")
        return

    # Ask the user for start and end times in HH:MM:SS format
    start_time = simpledialog.askstring("Start Time", "Enter start time (HH:MM:SS):")
    end_time = simpledialog.askstring("End Time", "Enter end time (HH:MM:SS):")

    # Check if the user inputted times
    if not start_time or not end_time:
        messagebox.showinfo("Invalid Input", "Start and end times are required.")
        return

    # Process each selected file
    for file_path in file_paths:
        file_name, _ = os.path.splitext(os.path.basename(file_path))
        export_path = f"{file_name}_trimmed.mp3"
        
        try:
            trim_audio(file_path, start_time, end_time, export_path)
            messagebox.showinfo("Success", f"Trimmed audio saved as {export_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while processing {file_name}: {e}")

if __name__ == "__main__":
    main()
