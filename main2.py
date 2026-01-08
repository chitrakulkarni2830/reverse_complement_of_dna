import customtkinter as ctk
from tkinter import filedialog, messagebox
from datetime import datetime

# --- Genetic & Chemistry Engine ---
CODON_TABLE = {
    'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
    'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',
    'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
    'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
    'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
    'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
    'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S', 'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
    'UAC':'Y', 'UAU':'Y', 'UAA':'*', 'UAG':'*', 'UGC':'C', 'UGU':'C', 'UGA':'*', 'UGG':'W',
}

def parse_fasta(content):
    """Robust parser for multi-line FASTA files."""
    lines = content.splitlines()
    # Join lines that aren't headers and remove all internal whitespace
    seq_lines = [line.strip() for line in lines if line.strip() and not line.startswith(">")]
    return "".join(seq_lines).upper()

def calculate_metrics(dna):
    weights = {"A": 313.21, "T": 304.19, "C": 289.18, "G": 329.21}
    mw = sum(weights.get(base, 0) for base in dna) + 79.0
    gc = (dna.count('G') + dna.count('C')) / len(dna) * 100 if dna else 0
    return mw, gc

def translate_rna(rna):
    protein = ""
    # Process codons in steps of 3
    for i in range(0, len(rna) - (len(rna) % 3), 3):
        protein += CODON_TABLE.get(rna[i:i+3], "?")
    return protein

# --- UI Controller ---
def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("Genomic Files", "*.fasta *.txt *.fa")])
    if file_path:
        try:
            with open(file_path, 'r') as f:
                raw_data = f.read()
                clean_seq = parse_fasta(raw_data)
                textbox_input.delete("0.0", "end")
                textbox_input.insert("0.0", clean_seq)
                process_dna()
        except Exception as e:
            messagebox.showerror("File Error", f"Could not read file: {e}")

def clear_all():
    textbox_input.delete("0.0", "end")
    label_stats.configure(text="MW: -- | GC Content: --")
    label_result_rc.configure(text="REVERSE COMPLEMENT: --")
    label_result_rna.configure(text="RNA TRANSCRIPT: --")
    label_result_prot.configure(text="PROTEIN SEQUENCE: --")

def download_report():
    dna = textbox_input.get("0.0", "end").strip().upper()
    if not dna: 
        messagebox.showwarning("Warning", "Nothing to export!")
        return
    
    mw, gc = calculate_metrics(dna)
    comp_map = str.maketrans("ATCG", "TAGC")
    rev_comp = dna.translate(comp_map)[::-1]
    rna = dna.replace("T", "U")
    protein = translate_rna(rna)

    file_path = filedialog.asksaveasfilename(defaultextension=".txt", initialfile="BioReport.txt")
    if file_path:
        with open(file_path, 'w') as f:
            f.write(f"GENOMIC REPORT - {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
            f.write(f"{'='*40}\n")
            f.write(f"Molecular Weight: {mw:.2f} g/mol\n")
            f.write(f"GC Content: {gc:.2f}%\n\n")
            f.write(f"PROTEIN SEQUENCE:\n{protein}\n")
        messagebox.showinfo("Success", "Report Saved!")

def process_dna():
    dna = textbox_input.get("0.0", "end").strip().upper().replace("\n", "").replace(" ", "")
    if not dna or not all(base in "ATCG" for base in dna):
        messagebox.showerror("Format Error", "Sequence must only contain A, T, C, G.")
        return
    
    mw, gc = calculate_metrics(dna)
    comp_map = str.maketrans("ATCG", "TAGC")
    rev_comp = dna.translate(comp_map)[::-1]
    rna = dna.replace("T", "U")
    protein = translate_rna(rna)

    label_stats.configure(text=f"MW: {mw:,.2f} g/mol  |  GC Content: {gc:.1f}%")
    label_result_rc.configure(text=f"REVERSE COMPLEMENT:\n{rev_comp}")
    label_result_rna.configure(text=f"RNA TRANSCRIPT:\n{rna}")
    label_result_prot.configure(text=f"PROTEIN SEQUENCE:\n{protein}")

# --- UI Layout ---
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title("BioStream Pro v5.1")
app.geometry("900x850")
app.configure(fg_color="#041C32")

# Header
ctk.CTkLabel(app, text="GENOMIC WORKSTATION", font=("Courier New", 30, "bold"), text_color="#A2FF86").pack(pady=20)

# Input Box
frame_in = ctk.CTkFrame(app, fg_color="#06283D", border_color="#245953", border_width=2)
frame_in.pack(padx=30, pady=10, fill="both")

ctk.CTkLabel(frame_in, text="DNA Input / FASTA Content:", text_color="#A2FF86").pack(anchor="w", padx=20, pady=(10,0))
textbox_input = ctk.CTkTextbox(frame_in, height=150, fg_color="#041C32", border_color="#245953", border_width=1)
textbox_input.pack(fill="x", padx=20, pady=10)

btn_file = ctk.CTkButton(frame_in, text="LOAD .FASTA FILE", fg_color="#245953", command=upload_file)
btn_file.pack(pady=10)

# Stats Bar
label_stats = ctk.CTkLabel(app, text="MW: -- | GC Content: --", font=("Arial", 16, "bold"), 
                           text_color="#041C32", fg_color="#A2FF86", corner_radius=10, height=45)
label_stats.pack(pady=10, padx=30, fill="x")

# Command Buttons (Syntax Fix Applied Here)
frame_cmds = ctk.CTkFrame(app, fg_color="transparent")
frame_cmds.pack(pady=15)

ctk.CTkButton(frame_cmds, text="ANALYZE", fg_color="#245953", command=process_dna, width=150).grid(row=0, column=0, padx=10)
ctk.CTkButton(frame_cmds, text="EXPORT", fg_color="#2D4263", command=download_report, width=150).grid(row=0, column=1, padx=10)
ctk.CTkButton(frame_cmds, text="CLEAR", fg_color="#7C0000", command=clear_all, width=150).grid(row=0, column=2, padx=10)

# Results
frame_out = ctk.CTkScrollableFrame(app, fg_color="#06283D", label_text="Biological Output", label_text_color="#A2FF86")
frame_out.pack(pady=10, padx=30, fill="both", expand=True)

label_result_rc = ctk.CTkLabel(frame_out, text="REVERSE COMPLEMENT: --", wraplength=800, font=("Consolas", 12))
label_result_rc.pack(pady=15)

label_result_rna = ctk.CTkLabel(frame_out, text="RNA TRANSCRIPT: --", wraplength=800, font=("Consolas", 12))
label_result_rna.pack(pady=15)

label_result_prot = ctk.CTkLabel(frame_out, text="PROTEIN SEQUENCE: --", wraplength=800, font=("Consolas", 14, "bold"), text_color="#A2FF86")
label_result_prot.pack(pady=15)

app.mainloop()