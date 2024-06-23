import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
import json

# Function to open the link
def open_link(url):
    webbrowser.open_new(url)

# Function to add a new question
def add_question():
    category = category_combobox.get()
    question = new_question_entry.get()
    link = new_link_entry.get()
    if category and question and link:
        categories[category].append((question, link))
        update_category_frame(category)
        save_data()  # Save data after making changes

# Function to delete a question
def delete_question(category, index):
    confirm_delete = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this question?")
    if confirm_delete:
        del categories[category][index]
        update_category_frame(category)
        save_data()  # Save data after making changes

# Function to update the frame of a specific category
def update_category_frame(category):
    # Clear the frame
    for widget in category_frames[category].winfo_children():
        widget.destroy()

    # Add the existing questions and buttons
    for index, (question, link) in enumerate(categories[category]):
        question_frame = ttk.Frame(category_frames[category], style='Question.TFrame')
        question_frame.pack(fill="x", pady=2)
        
        question_label = ttk.Label(question_frame, text=question, style='Question.TLabel')
        question_label.pack(side="left", padx=5)
        
        delete_button = ttk.Button(question_frame, text="✖", width=2, style='Delete.TButton', command=lambda c=category, i=index: delete_question(c, i))
        delete_button.pack(side="right", padx=5)
        
        link_button = ttk.Button(question_frame, text="Open Link", style='Link.TButton', command=lambda url=link: open_link(url))
        link_button.pack(side="right", padx=5)

# Function to save data to file
def save_data():
    with open('interview_data.txt', 'w') as f:
        json.dump(categories, f)

# Function to load data from file
def load_data():
    global categories
    try:
        with open('interview_data.txt', 'r') as f:
            categories = json.load(f)
    except FileNotFoundError:
        categories = {
            "Basic Questions": [
                ("Amstrong Number", "https://www.geeksforgeeks.org/problems/armstrong-numbers2727/1"),
                ("Factorial", "https://www.geeksforgeeks.org/problems/factorial5739/1"),
                ("Fibonacci Series", "https://www.geeksforgeeks.org/problems/nth-fibonacci-number1335/1"),
                ("Prime Number", "https://www.geeksforgeeks.org/problems/prime-number2314/1"),
                ("Pallindrome in String", "https://www.geeksforgeeks.org/problems/palindrome-string0817/1")
            ],
            "Sorting Algorithms": [
                ("Bubble Sort", "https://www.geeksforgeeks.org/problems/bubble-sort/1"),
                ("Selection Sort", "https://www.geeksforgeeks.org/problems/selection-sort/1"),
                ("Insertion Sort", "https://www.geeksforgeeks.org/problems/insertion-sort/1"),
                ("Merge Sort", "https://leetcode.com/problems/sort-an-array/solutions/329672/merge-sort/1"),
                ("Quick Sort", "https://www.geeksforgeeks.org/problems/quick-sort/1")
            ],
            "Searching Algorithms": [
                ("Linear Search", "https://www.geeksforgeeks.org/problems/nth-fibonacci-number1335/1"),
                ("Binary Search", "https://www.geeksforgeeks.org/problems/binary-search-1587115620/1")
            ]
        }

# Create dictionaries to hold the frames for each category
category_frames = {}

# Main application window
root = tk.Tk()
root.title("Basic Interview Practice")

# Set the background color of the root window
root.configure(background='#e6f2ff')

# Call load_data() before creating category frames
load_data()

# Define styles
style = ttk.Style()
style.configure('TFrame', background='#e6f2ff')  # Match root background color
style.configure('TLabel', background='#e6f2ff', foreground='#000000')
style.configure('TButton', background='#e0e0e0', foreground='#000000')
style.configure('Question.TFrame', background='#ffffff')
style.configure('Question.TLabel', background='#ffffff', foreground='#000000')
style.configure('Delete.TButton', background='#ffcccc', foreground='#ff0000')
style.configure('Link.TButton', background='#cce5ff', foreground='#0000ff')

# Create frames for each category
for category in categories:
    frame = ttk.LabelFrame(root, text=category, padding="10", style='TFrame')
    frame.pack(fill="x", padx=10, pady=5)
    category_frames[category] = frame
    update_category_frame(category)

# Add a section at the bottom for adding new questions
add_frame = ttk.LabelFrame(root, text="Add New Question", padding="10", style='TFrame')
add_frame.pack(fill="x", padx=10, pady=10)

ttk.Label(add_frame, text="Category:", style='TLabel').pack(side="left", padx=5)
category_combobox = ttk.Combobox(add_frame, values=list(categories.keys()))
category_combobox.pack(side="left", fill="x", expand=True, padx=5)

ttk.Label(add_frame, text="Question:", style='TLabel').pack(side="left", padx=5)
new_question_entry = ttk.Entry(add_frame)
new_question_entry.pack(side="left", fill="x", expand=True, padx=5)

ttk.Label(add_frame, text="Link:", style='TLabel').pack(side="left", padx=5)
new_link_entry = ttk.Entry(add_frame)
new_link_entry.pack(side="left", fill="x", expand=True, padx=5)

add_button = ttk.Button(add_frame, text="Add", style='TButton', command=add_question)
add_button.pack(side="right", padx=5)

# Start the main loop
root.mainloop()
