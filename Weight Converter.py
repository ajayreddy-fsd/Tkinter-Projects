import tkinter as tk
from tkinter import messagebox  # for message boxes


class KiloConverter:
    def __init__(self):
        # window creation
        self.window = tk.Tk()  # window creation
        self.window.title('Kilo Converter')  # window title
        self.window.geometry('600x500')  # width & length of the window

        # layout creation
        self.top_frame = tk.Frame(self.window)
        self.bottom_frame = tk.Frame(self.window)
        self.result_frame = tk.Frame(self.window)

        # widget creation
        self.prompt_label = tk.Label(
            self.top_frame, text='enter weight in kg', padx=20, fg='blue', font=("arial", 12))
        self.kilo_entry = tk.Entry(self.top_frame, bg='lightcyan')

        # buttons
        # command = functionality, pass function without any args
        self.result_btn = tk.Button(
            self.bottom_frame, text='convert', padx=10, command=self.calculate)
        self.exit_btn = tk.Button(
            self.bottom_frame, text='exit', padx=10, command=self.exit)

        # result widget
        self.result = tk.StringVar(self.window, 'result = ')
        # uses text-variable instead of text
        self.result_label = tk.Label(
            self.result_frame, textvariable=self.result, fg='blue')

        # packing (first packed first displayed)
        self.prompt_label.pack(side='left', padx=10)
        self.kilo_entry.pack()

        # pack buttons
        # not left, will be center aligned
        self.result_btn.pack(side='left', padx=10)
        self.exit_btn.pack()
        self.result_label.pack()

        # imp misc
        self.top_frame.pack(padx=20, pady=20)
        self.bottom_frame.pack()
        self.result_frame.pack(pady=20)
        self.window.mainloop()

    def calculate(self):
        try:
            kg = self.kilo_entry.get()
            result = float(kg)*2.204
            print(result)

            # one way of displaying output using messagebox
            messagebox.showinfo("RESULT = ", f"{result}")

            self.result.set(f"Result -> {kg}kg = {result}lb")

        except Exception:
            messagebox.showerror('bad input', 'input to be int or float')

    def exit(self):
        if messagebox.askyesno('sure?', 'sure?'):
            self.window.destroy()


k1 = KiloConverter()
