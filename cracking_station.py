# Cracking Station ©Edison_Plaku
# Single-file Python GUI hash cracker (educational / lab use)
# Requirements: Python 3.x (no external libraries)

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import hashlib
import threading
import time
import queue
import os

# -------------------- Hash Utilities --------------------

HASH_ALGOS = {
    "MD5": hashlib.md5,
    "SHA-1": hashlib.sha1,
    "SHA-224": hashlib.sha224,
    "SHA-256": hashlib.sha256,
    "SHA-384": hashlib.sha384,
    "SHA-512": hashlib.sha512,
}

def detect_hash_type(h):
    h = h.strip().lower()
    ln = len(h)
    if ln == 32:
        return "MD5", 0.90
    if ln == 40:
        return "SHA-1", 0.90
    if ln == 56:
        return "SHA-224", 0.85
    if ln == 64:
        return "SHA-256", 0.92
    if ln == 96:
        return "SHA-384", 0.85
    if ln == 128:
        return "SHA-512", 0.90
    return "Unknown", 0.0

def hash_word(word, algo):
    return HASH_ALGOS[algo](word.encode()).hexdigest()

# -------------------- GUI App --------------------

class CrackingStation(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cracking Station ©Edison_Plaku")
        self.geometry("1200x700")
        self.configure(bg="#0b1020")
        self._setup_style()

        self.wordlist = []
        self.stop_flag = threading.Event()
        self.task_queue = queue.Queue()

        self._build_ui()

    def _setup_style(self):
        style = ttk.Style(self)
        style.theme_use("default")
        style.configure("TFrame", background="#0b1020")
        style.configure("TLabel", background="#0b1020", foreground="#dbe2ff")
        style.configure("TButton", background="#1b2a6b", foreground="white")
        style.configure("Treeview",
                        background="#0f1733",
                        fieldbackground="#0f1733",
                        foreground="#e9edff")
        style.map("TButton",
                  background=[("active", "#3a6df0")])

    def _build_ui(self):
        left = ttk.Frame(self)
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        right = ttk.Frame(self)
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # --- Hash Input ---
        ttk.Label(left, text="Hash input").pack(anchor="w")
        self.hash_text = tk.Text(left, height=6, bg="#0f1733", fg="#e9edff", insertbackground="white")
        self.hash_text.pack(fill=tk.X, pady=5)

        row = ttk.Frame(left)
        row.pack(fill=tk.X, pady=5)

        self.detect_lbl = ttk.Label(row, text="Detected: -")
        self.detect_lbl.pack(side=tk.LEFT)

        ttk.Button(row, text="Identify hash type", command=self.identify).pack(side=tk.LEFT, padx=5)

        self.algo_var = tk.StringVar(value="Auto")
        algo_menu = ttk.Combobox(row, textvariable=self.algo_var,
                                 values=["Auto"] + list(HASH_ALGOS.keys()),
                                 state="readonly", width=12)
        algo_menu.pack(side=tk.RIGHT)

        # --- Wordlist ---
        ttk.Label(left, text="Lista e fjalëkalimeve").pack(anchor="w", pady=(10, 0))
        wrow = ttk.Frame(left)
        wrow.pack(fill=tk.X)

        ttk.Button(wrow, text="Ngarko .txt", command=self.load_wordlist).pack(side=tk.LEFT)
        self.wl_lbl = ttk.Label(wrow, text="asnjë skedar i zgjedhur")
        self.wl_lbl.pack(side=tk.LEFT, padx=10)

        self.manual_words = tk.Text(left, height=5, bg="#0f1733", fg="#e9edff", insertbackground="white")
        self.manual_words.pack(fill=tk.X, pady=5)
        self.manual_words.insert("1.0", "Ose fut fjalëkalime manualisht (një për rresht)")

        # --- Options ---
        opt = ttk.Frame(left)
        opt.pack(fill=tk.X, pady=5)
        self.case_var = tk.BooleanVar()
        self.trim_var = tk.BooleanVar(value=True)
        self.stop_first_var = tk.BooleanVar()

        ttk.Checkbutton(opt, text="Case-sensitive", variable=self.case_var).pack(side=tk.LEFT)
        ttk.Checkbutton(opt, text="Trim whitespace", variable=self.trim_var).pack(side=tk.LEFT, padx=10)
        ttk.Checkbutton(opt, text="Stop on first match", variable=self.stop_first_var).pack(side=tk.LEFT)

        # --- Execution ---
        ex = ttk.Frame(left)
        ex.pack(fill=tk.X, pady=10)
        ttk.Button(ex, text="Run", command=self.run).pack(side=tk.LEFT)
        ttk.Button(ex, text="Clear", command=self.clear).pack(side=tk.LEFT, padx=10)

        self.status_lbl = ttk.Label(left, text="Ready")
        self.status_lbl.pack(anchor="w")

        self.log = tk.Text(left, height=8, bg="#0f1733", fg="#8ff0a4", insertbackground="white")
        self.log.pack(fill=tk.BOTH, expand=True, pady=5)
        self.log.insert("end", "[Ready] Waiting for input...\n")

        # --- Results ---
        ttk.Label(right, text="Rezultatet").pack(anchor="w")
        cols = ("#", "Hash", "Password", "Algoritmi", "Koha")
        self.tree = ttk.Treeview(right, columns=cols, show="headings")
        for c in cols:
            self.tree.heading(c, text=c)
            self.tree.column(c, anchor="w")
        self.tree.pack(fill=tk.BOTH, expand=True)

    # -------------------- Actions --------------------

    def identify(self):
        hashes = self._get_hashes()
        if not hashes:
            return
        algo, conf = detect_hash_type(hashes[0])
        self.detect_lbl.config(text=f"Detected: {algo} • Confidence: {int(conf*100)}%")

    def load_wordlist(self):
        path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if not path:
            return
        with open(path, "r", errors="ignore") as f:
            self.wordlist = [line.rstrip("\n") for line in f]
        self.wl_lbl.config(text=os.path.basename(path))
        self._log(f"Loaded wordlist: {len(self.wordlist)} entries")

    def run(self):
        hashes = self._get_hashes()
        if not hashes:
            messagebox.showwarning("Warning", "No hashes provided.")
            return

        words = self._get_words()
        if not words:
            messagebox.showwarning("Warning", "No wordlist or manual words.")
            return

        algo_sel = self.algo_var.get()
        self.stop_flag.clear()
        self.tree.delete(*self.tree.get_children())

        t = threading.Thread(target=self._crack, args=(hashes, words, algo_sel), daemon=True)
        t.start()

    def clear(self):
        self.hash_text.delete("1.0", "end")
        self.manual_words.delete("1.0", "end")
        self.tree.delete(*self.tree.get_children())
        self.log.delete("1.0", "end")
        self.status_lbl.config(text="Ready")

    # -------------------- Core --------------------

    def _crack(self, hashes, words, algo_sel):
        start_all = time.time()
        idx = 1

        for h in hashes:
            if self.stop_flag.is_set():
                break

            algos = [algo_sel] if algo_sel != "Auto" else list(HASH_ALGOS.keys())

            for algo in algos:
                if algo not in HASH_ALGOS:
                    continue

                t0 = time.time()
                for w in words:
                    ww = w
                    if self.trim_var.get():
                        ww = ww.strip()
                    if not self.case_var.get():
                        ww = ww.lower()

                    if hash_word(ww, algo) == h.lower():
                        dt = int((time.time() - t0) * 1000)
                        self._add_result(idx, h, ww, algo, f"{dt} ms")
                        idx += 1
                        self._log(f"[MATCH] {h} -> {ww} ({algo})")
                        if self.stop_first_var.get():
                            self.stop_flag.set()
                        break

        self.status_lbl.config(text=f"Done in {int((time.time()-start_all)*1000)} ms")

    # -------------------- Helpers --------------------

    def _get_hashes(self):
        return [h.strip() for h in self.hash_text.get("1.0", "end").splitlines() if h.strip()]

    def _get_words(self):
        manual = [w for w in self.manual_words.get("1.0", "end").splitlines() if w.strip()]
        return list(dict.fromkeys(self.wordlist + manual))

    def _add_result(self, i, h, p, a, k):
        self.tree.insert("", "end", values=(i, h[:32] + "...", p, a, k))

    def _log(self, msg):
        self.log.insert("end", msg + "\n")
        self.log.see("end")

# -------------------- Run --------------------

if __name__ == "__main__":
    app = CrackingStation()
    app.mainloop()
