import qrcode
import tkinter as tk
from tkinter import messagebox, filedialog, ttk 
import os

# --- Core Logic Function ---
def generate_qr_code():
    url = url_entry.get().strip()
    
    if not url:
        messagebox.showerror("Input Error", "Please enter a URL to generate the QR code.")
        return

    try:
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            initialfile="qrcode.png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
            title="Save QR Code Image As"
        )

        if not file_path:
            return 

        # QR Code Generation Logic
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        
        img.save(file_path)

        messagebox.showinfo("Success", f"QR Code successfully saved to:\n{os.path.basename(file_path)}") 
        url_entry.delete(0, tk.END) 
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# --- GUI Setup ---
root = tk.Tk()
root.title("Mind Bogaling QR Code Generator")

root.geometry("450x250") 
root.resizable(False, False)


style = ttk.Style()
style.theme_use('vista') 

style.configure('TFrame', background="#faf9f9") 
style.configure('TLabel', background='#f0f0f0', font=('Segoe UI', 10))
style.configure('TButton', font=('Segoe UI', 10, 'bold'), padding=8)
style.map('TButton', 
          background=[('active', '#5cb85c'), ('pressed', '#4cae4c')], 
          foreground=[('active', 'white')])


main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.pack(fill=tk.BOTH, expand=True)

# 1. Label
url_label = ttk.Label(main_frame, text="Enter URL to Encode:")
url_label.pack(pady=(10, 5))

# 2. Input Field (Entry Widget) - using ttk.Entry
url_entry = ttk.Entry(main_frame, width=50, font=('Segoe UI', 10))
url_entry.pack(pady=5, padx=10)
url_entry.focus_set() 

# 3. Button - using ttk.Button
generate_button = ttk.Button(main_frame, text="Generate & Save QR Code", command=generate_qr_code)
generate_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()