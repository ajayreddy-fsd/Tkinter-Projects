import tkinter as tk
from tkinter import messagebox


class AverageCalculator:

    def __init__(self):
        # to create window
        self.window = tk.Tk()
        self.window.title('tk')
        self.window.geometry('400x2000')

        # to create all the frames that are to be used in this class
        self.test1score_frame = tk.Frame(self.window)
        self.test2score_frame = tk.Frame(self.window)
        self.test3score_frame = tk.Frame(self.window)
        self.result_frame = tk.Frame(self.window)
        self.button_frame = tk.Frame(self.window)

        # to create all the widgets
        # widgets set-1
        # to create label1 and userEntry1 inorder to get the user-test1 score
        self.label1 = tk.Label(self.test1score_frame,
                               text='Enter the score for test 1: ', padx=25)
        self.userEntry1 = tk.Entry(self.test1score_frame)

        # to create label2 and userEntry2 inorder to get the user-test2 score
        self.label2 = tk.Label(self.test2score_frame,
                               text='Enter the score for test 2: ', padx=25)
        self.userEntry2 = tk.Entry(self.test2score_frame)

        # to create label3 and userEntry3 inorder to get the user-test3 score
        self.label3 = tk.Label(self.test3score_frame,
                               text='Enter the score for test 3: ', padx=25)
        self.userEntry3 = tk.Entry(self.test3score_frame)

        # widgets set-2
        # to create buttons
        self.avg_button = tk.Button(
            self.button_frame, text='Average', command=self.calculateAverage)
        self.quit_button = tk.Button(
            self.button_frame, text='Quit', command=self.quit)

        # widgets set-3
        # to create result-label
        self.result = tk.StringVar(self.window, 'Average:')
        self.result_label = tk.Label(
            self.result_frame, textvariable=self.result)

        # to pack all the widgets created
        # packing all three labels and userEntries
        self.label1.pack(side='left')
        self.userEntry1.pack()
        self.label2.pack(side='left')
        self.userEntry2.pack()
        self.label3.pack(side='left')
        self.userEntry3.pack()

        # pakcing result-label
        self.result_label.pack()

        # pakcing both the buttons
        self.avg_button.pack(side='left', padx=5)
        self.quit_button.pack()

        # packing all the frames
        self.test1score_frame.pack()
        self.test2score_frame.pack()
        self.test3score_frame.pack()
        self.result_frame.pack()
        self.button_frame.pack()

        # to run mainloop
        self.window.mainloop()

    def calculateAverage(self):
        try:
            test1_score = float(self.userEntry1.get())
            test2_score = float(self.userEntry2.get())
            test3_score = float(self.userEntry3.get())
            average = (test1_score + test2_score + test3_score)/3
            print(average)
            self.result.set(f"Average: {average}")

        except Exception:
            # error window pops up when user enters invalid input
            messagebox.showerror(
                'invalid input', 'Enter valid integer or float')

    def quit(self):
        if messagebox.askyesno('Confirm?', 'Click yes to quit'):
            self.window.destroy()


avg1 = AverageCalculator()
