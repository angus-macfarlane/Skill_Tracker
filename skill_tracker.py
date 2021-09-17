import tkinter as tk
import pickle

main_window = tk.Tk()  # creates main window
main_window.geometry('720x640+250-120')  # creates size of window

with open('mypickle.pickle', 'rb') as f:
    unpickled_file = pickle.load(f)
    # npickled_file = unpickled_file.read()
    print("Printing file: ")
    print(type(unpickled_file))

    l = []
    i = 0
    for key in unpickled_file:
        print(key, unpickled_file[key])

    for key in unpickled_file:
        l.append(key)

    for val in unpickled_file:
        l.insert(i + 1, unpickled_file[val])
        i += 2
    print(l)


    def read_from_pickle(l):
        i = 0
        j = 1
        while i < len(l):
            global row_counter
            global column_counter
            entry_text = skill_input_text.get()
            skill_input_text.set("")
            time = time_input.get()
            time_input.set("")

            x0 = l[j][0]
            y0 = 100
            x1 = 0
            y1 = 0
            if skill_dictionary == {}:  # first time
                frame1.rowconfigure(l[j][2], weight=1)
                frame1.columnconfigure(l[j][1], weight=1)
                new_label = tk.Canvas(frame1, width=150, height=50)
                new_label.create_rectangle(x0, y0, x1, y1, fill="red")
                new_label.create_text(30, 27, text=l[i])x
                skill_dictionary[l[i]] = []
                skill_dictionary.setdefault(l[i], []).append(time)
                new_label.grid(row=row_counter, column=column_counter, padx=5, pady=10)
                column_counter += 1
                skill_dictionary.setdefault(l[i], []).append(column_counter)
                skill_dictionary.setdefault(l[i], []).append(row_counter)
                # if column_counter == 3:
                #     column_counter = 0
                #     row_counter += 1

            else:  # column_counter in (0, 1, 2, 3):
                frame1.rowconfigure(row_counter, weight=1)
                frame1.columnconfigure(column_counter, weight=1)
                new_label = tk.Canvas(frame1, width=150, height=50)
                new_label.create_rectangle(x0, y0, x1, y1, fill="red")
                new_label.create_text(30, 27, text=entry_text)
                skill_dictionary[entry_text] = []
                skill_dictionary.setdefault(entry_text, []).append(time)
                new_label.grid(row=row_counter, column=column_counter, padx=5, pady=10)
                column_counter += 1
                skill_dictionary.setdefault(entry_text, []).append(column_counter)
                skill_dictionary.setdefault(entry_text, []).append(row_counter)
                if column_counter == 3:
                    column_counter = 0
                    row_counter += 1

    read_from_pickle(l)

skill_input_text = tk.StringVar()  # ?What does this mean?
time_input = tk.StringVar()
row_counter = 0
column_counter = 0
# Make 4x4 grid
main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=1)
# add input box
add_skill_entry = tk.Entry(main_window, bg="gray", textvariable=skill_input_text)
add_skill_entry.grid(column=0, row=0, sticky="s")
# add input box
time_tracker = tk.Entry(main_window, bg="gray", textvariable=time_input)
time_tracker.grid(column=0, row=1, sticky="n")
# display skill and graph
skill_dictionary = {}
frame1 = tk.Frame(main_window, bg="white", height="300", width="300")
frame1.grid_propagate(0)
frame1.grid(row=0, column=1, rowspan=2)


# add input from skill_input to frame: the characters, background, and a rectangle. And, adding time to the rectangle parameter.
def add_to_frame():
    global row_counter
    global column_counter
    entry_text = skill_input_text.get()
    skill_input_text.set("")
    time = time_input.get()
    time_input.set("")

    x0 = time
    y0 = 100
    x1 = 0
    y1 = 0
    if skill_dictionary == {}:  # first time
        frame1.rowconfigure(row_counter, weight=1)
        frame1.columnconfigure(column_counter, weight=1)
        new_label = tk.Canvas(frame1, width=150, height=50)
        new_label.create_rectangle(x0, y0, x1, y1, fill="red")
        new_label.create_text(30, 27, text=entry_text)
        skill_dictionary[entry_text] = []
        skill_dictionary.setdefault(entry_text, []).append(time)
        new_label.grid(row=row_counter, column=column_counter, padx=5, pady=10)
        column_counter += 1
        skill_dictionary.setdefault(entry_text, []).append(column_counter)
        skill_dictionary.setdefault(entry_text, []).append(row_counter)
        # if column_counter == 3:
        #     column_counter = 0
        #     row_counter += 1

    else:  # column_counter in (0, 1, 2, 3):
        frame1.rowconfigure(row_counter, weight=1)
        frame1.columnconfigure(column_counter, weight=1)
        new_label = tk.Canvas(frame1, width=150, height=50)
        new_label.create_rectangle(x0, y0, x1, y1, fill="red")
        new_label.create_text(30, 27, text=entry_text)
        skill_dictionary[entry_text] = []
        skill_dictionary.setdefault(entry_text, []).append(time)
        new_label.grid(row=row_counter, column=column_counter, padx=5, pady=10)
        column_counter += 1
        skill_dictionary.setdefault(entry_text, []).append(column_counter)
        skill_dictionary.setdefault(entry_text, []).append(row_counter)
        if column_counter == 3:
            column_counter = 0
            row_counter += 1


skill_dictionary_pickled = pickle.dumps(skill_dictionary)
skill_dictionary_unpickled = pickle.loads(skill_dictionary_pickled)
print(skill_dictionary_unpickled)

# add time button
# add_time_button = tk.Button(main_window, text="ADD TIME", command=add_to_frame)
# add_time_button.grid(column=0, row=2, sticky="n")

# add skill button
# add_skill_button = tk.Button(main_window, text="ADD SKILL", command=add_to_frame)
# add_skill_button.grid(column=0, row=1, sticky="n")

# submit button for both
submit_button = tk.Button(main_window, text="Submit", command=add_to_frame)
submit_button.grid(column=0, row=1, sticky="s")

main_window.mainloop()  # makes it so the main window opens (and stays open?)

print(skill_dictionary)

with open('mypickle.pickle', 'wb') as f:
    print("Pickling file")
    pickle.dump(skill_dictionary, f, protocol=pickle.HIGHEST_PROTOCOL)
    print("file pickled")


main_window.mainloop()  # makes it so the main window opens (and stays open?)

# Put what is in the dictionary back into the function so that it builds what was in there when it was closed.
