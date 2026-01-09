# BioStream Pro v5.1: Genomic Data Pipeline & Workstation



## 🧪 Project Overview
**BioStream Pro** is a high-performance Python workstation designed to automate the processing of raw genomic sequences. Developed by a biochemist for bioinformatic applications, this tool bridges the gap between molecular biology research and computational efficiency. It provides a GUI-based environment for DNA-to-Protein translation, molecular weight estimation, and GC-content analysis.

This project demonstrates the application of **biochemistry domain expertise** through software engineering, focusing on robust data parsing, algorithmic sequence manipulation, and user-centric design.

---

## 🚀 Key Features
* **FASTA File Support:** Robust parsing of multi-line `.fasta` and `.txt` files, handling headers and internal whitespace automatically.
* **Central Dogma Automation:** Seamlessly performs DNA transcription and RNA translation using an internal $O(1)$ codon mapping engine.
* **Biochemical Metrics:**
    * **Molecular Weight (MW):** Precise calculation based on individual nucleotide monophosphate weights plus terminal phosphate adjustments.
    * **GC-Content:** Instant calculation of GC percentage, a critical metric for genomic stability and primer design.
* **Interactive GUI:** A modern, dark-themed interface built with `CustomTkinter` for an industrial-grade user experience.
* **Export Utility:** Generates professional-grade `.txt` reports with timestamps for laboratory record-keeping.

---

## 🧬 Scientific Logic & Math
The application utilizes a dictionary-based hashing strategy for the **Standard Genetic Code**, ensuring fast and accurate translation of RNA to Amino Acids.

### Molecular Weight Calculation
The tool uses the following biochemical estimation for single-stranded DNA:
$$MW = \sum (w_{i} \times n_{i}) + 79.0$$

Where:
* $w_{i}$ represents the molecular weight of nucleotides (A: 313.21, T: 304.19, C: 289.18, G: 329.21 g/mol).
* $79.0$ accounts for the terminal phosphate group.



---

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **GUI Framework:** `CustomTkinter` (Advanced UI development)
* **Logic:** Standard Library (`datetime`, `filedialog`, `messagebox`)
* **Data Structure:** Python Dictionaries for optimized codon lookup.

---

## 📦 Installation & Usage
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/BioStream-Pro.git](https://github.com/YourUsername/BioStream-Pro.git)
    cd BioStream-Pro
    ```
2.  **Install dependencies:**
    ```bash
    pip install customtkinter
    ```
3.  **Run the application:**
    ```bash
    python biostream_pro.py
    ```

---

## 📊 Analytics Roadmap
* **Batch Processing:** Add functionality to process 100+ FASTA files simultaneously and output a CSV.
* **SQL Integration:** Implement a local SQLite database to track historical sequence analyses.
* **Bio-Dashboard:** Develop a Power BI template to visualize nucleotide distribution trends across different species.

---

## 👨‍🔬 About the Author
As an **MSc Biochemistry graduate** transitioning into **Data Analytics**, I specialize in building tools that make complex biological data accessible and actionable. My portfolio focuses on the intersection of Python automation, SQL database management, and Power BI visualization within the life sciences sector.

---
*Developed for the intersection of Biology and Data Science.*