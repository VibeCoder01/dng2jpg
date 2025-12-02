#!/usr/bin/env python3
import os
import sys
import traceback
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText

try:
    import rawpy
    from PIL import Image
except ImportError as e:
    missing = str(e)
    print("Missing dependency:", missing)
    print("Install with: pip install rawpy Pillow")
    sys.exit(1)


class DNGToJPGApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DNG to JPG Converter")

        self.folder_path = tk.StringVar()
        self.overwrite = tk.BooleanVar(value=False)

        # Folder selection frame
        folder_frame = tk.Frame(root, padx=10, pady=10)
        folder_frame.pack(fill=tk.X)

        tk.Label(folder_frame, text="Selected folder:").pack(anchor="w")
        entry_frame = tk.Frame(folder_frame)
        entry_frame.pack(fill=tk.X, pady=(2, 5))

        self.folder_entry = tk.Entry(entry_frame, textvariable=self.folder_path)
        self.folder_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        browse_btn = tk.Button(entry_frame, text="Browse...", command=self.browse_folder)
        browse_btn.pack(side=tk.LEFT, padx=(5, 0))

        # Options frame
        options_frame = tk.Frame(root, padx=10)
        options_frame.pack(fill=tk.X)

        overwrite_cb = tk.Checkbutton(
            options_frame,
            text="Overwrite existing JPG files",
            variable=self.overwrite
        )
        overwrite_cb.pack(anchor="w")

        # Convert button
        convert_btn = tk.Button(
            root,
            text="Convert DNG → JPG",
            command=self.convert_clicked,
            padx=10,
            pady=5
        )
        convert_btn.pack(pady=(5, 5))

        # Log output
        log_frame = tk.Frame(root, padx=10, pady=5)
        log_frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(log_frame, text="Log:").pack(anchor="w")
        self.log_text = ScrolledText(log_frame, height=15)
        self.log_text.pack(fill=tk.BOTH, expand=True)

    def log(self, msg):
        self.log_text.insert(tk.END, msg + "\n")
        self.log_text.see(tk.END)
        self.root.update_idletasks()

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path.set(folder)

    def convert_clicked(self):
        folder = self.folder_path.get().strip()
        if not folder:
            messagebox.showwarning("No folder", "Please select a folder first.")
            return

        if not os.path.isdir(folder):
            messagebox.showerror("Invalid folder", "The selected path is not a folder.")
            return

        self.log_text.delete("1.0", tk.END)
        self.log(f"Selected folder: {folder}")
        self.log(f"Overwrite existing JPGs: {self.overwrite.get()}")
        self.log("Scanning for DNG files...")

        dng_files = [
            f for f in os.listdir(folder)
            if f.lower().endswith(".dng")
        ]

        if not dng_files:
            self.log("No DNG files found in this folder.")
            messagebox.showinfo("No files", "No DNG files found in the selected folder.")
            return

        self.log(f"Found {len(dng_files)} DNG file(s). Starting conversion...\n")

        converted = 0
        skipped = 0
        errors = 0

        for idx, dng_name in enumerate(dng_files, start=1):
            dng_path = os.path.join(folder, dng_name)
            base, _ = os.path.splitext(dng_name)
            jpg_name = base + ".jpg"
            jpg_path = os.path.join(folder, jpg_name)

            if os.path.exists(jpg_path) and not self.overwrite.get():
                self.log(f"[{idx}/{len(dng_files)}] Skipping existing: {jpg_name}")
                skipped += 1
                continue

            try:
                self.log(f"[{idx}/{len(dng_files)}] Converting: {dng_name}")
                with rawpy.imread(dng_path) as raw:
                    rgb = raw.postprocess()

                img = Image.fromarray(rgb)
                img.save(jpg_path, "JPEG", quality=90)
                converted += 1
            except Exception as e:
                errors += 1
                self.log(f"  ERROR converting {dng_name}: {e}")
                traceback.print_exc()

        self.log("\nConversion complete.")
        self.log(f"Converted: {converted}")
        self.log(f"Skipped (existing JPG): {skipped}")
        self.log(f"Errors: {errors}")

        messagebox.showinfo(
            "Done",
            f"Conversion complete.\n\n"
            f"Converted: {converted}\n"
            f"Skipped (existing JPG): {skipped}\n"
            f"Errors: {errors}"
        )


def main():
    root = tk.Tk()
    app = DNGToJPGApp(root)
    root.minsize(500, 400)
    root.mainloop()


if __name__ == "__main__":
    main()
