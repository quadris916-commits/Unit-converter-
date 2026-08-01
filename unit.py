import tkinter as tk
from tkinter import ttk, messagebox

UNIT_MAP = {
    'Length': {
        'Millimeter': 0.001,
        'Centimeter': 0.01,
        'Meter': 1.0,
        'Kilometer': 1000.0,
        'Inch': 0.0254,
        'Foot': 0.3048,
        'Yard': 0.9144,
        'Mile': 1609.344,
    },
    'Weight': {
        'Milligram': 0.000001,
        'Gram': 0.001,
        'Kilogram': 1.0,
        'Ton': 1000.0,
        'Pound': 0.45359237,
        'Ounce': 0.028349523125,
    },
    'Temperature': {
        'Celsius': 'C',
        'Fahrenheit': 'F',
        'Kelvin': 'K',
    },
    'Time': {
        'Second': 1,
        'Minute': 60,
        'Hour': 3600,
        'Day': 86400,
        'Week': 604800,
    }
}

THEME = {
    'bg': '#0f172a',
    'panel': '#111827',
    'card': '#1f2937',
    'accent': '#38bdf8',
    'accent2': '#22c55e',
    'text': '#e5e7eb',
    'muted': '#94a3b8',
    'entry_bg': '#0b1220',
}


class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Advanced Unit Converter')
        self.root.geometry('860x560')
        self.root.minsize(860, 560)
        self.root.configure(bg=THEME['bg'])

        self.category_var = tk.StringVar(value='Length')
        self.from_var = tk.StringVar()
        self.to_var = tk.StringVar()
        self.value_var = tk.StringVar()
        self.result_var = tk.StringVar(value='0.0')
        self.history = []

        self.setup_style()
        self.build_ui()
        self.update_units()

    def setup_style(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background=THEME['bg'])
        style.configure('Card.TFrame', background=THEME['card'])
        style.configure('TLabel', background=THEME['bg'], foreground=THEME['text'], font=('Segoe UI', 11))
        style.configure('Header.TLabel', background=THEME['bg'], foreground=THEME['text'], font=('Segoe UI', 22, 'bold'))
        style.configure('Sub.TLabel', background=THEME['bg'], foreground=THEME['muted'], font=('Segoe UI', 10))
        style.configure('TButton', font=('Segoe UI', 10, 'bold'), padding=8)
        style.map('TButton', background=[('active', THEME['accent'])])
        style.configure('TCombobox', fieldbackground=THEME['entry_bg'], background=THEME['entry_bg'], foreground=THEME['text'])
        style.configure('TEntry', fieldbackground=THEME['entry_bg'], foreground=THEME['text'])
        style.configure('Treeview', background=THEME['panel'], fieldbackground=THEME['panel'], foreground=THEME['text'], rowheight=28)
        style.configure('Treeview.Heading', font=('Segoe UI', 10, 'bold'))

    def build_ui(self):
        top = ttk.Frame(self.root)
        top.pack(fill='x', padx=24, pady=(20, 8))

        ttk.Label(top, text='Advanced Unit Converter', style='Header.TLabel').pack(anchor='w')
        ttk.Label(top, text='Convert length, weight, temperature, and time with a modern dark UI.', style='Sub.TLabel').pack(anchor='w', pady=(4, 0))

        main = ttk.Frame(self.root)
        main.pack(fill='both', expand=True, padx=24, pady=16)

        left = ttk.Frame(main, style='Card.TFrame')
        left.pack(side='left', fill='both', expand=True, padx=(0, 12))

        right = ttk.Frame(main, style='Card.TFrame', width=280)
        right.pack(side='right', fill='y')
        right.pack_propagate(False)

        for frame in (left, right):
            frame.configure(padding=18)

        ttk.Label(left, text='Converter').grid(row=0, column=0, columnspan=3, sticky='w', pady=(0, 14))

        ttk.Label(left, text='Category').grid(row=1, column=0, sticky='w', pady=8)
        self.category_cb = ttk.Combobox(left, textvariable=self.category_var, values=list(UNIT_MAP.keys()), state='readonly', width=20)
        self.category_cb.grid(row=1, column=1, sticky='w', pady=8)
        self.category_cb.bind('<<ComboboxSelected>>', lambda e: self.update_units())

        ttk.Label(left, text='Value').grid(row=2, column=0, sticky='w', pady=8)
        self.value_entry = ttk.Entry(left, textvariable=self.value_var, width=24)
        self.value_entry.grid(row=2, column=1, sticky='w', pady=8)

        ttk.Label(left, text='From').grid(row=3, column=0, sticky='w', pady=8)
        self.from_cb = ttk.Combobox(left, textvariable=self.from_var, state='readonly', width=20)
        self.from_cb.grid(row=3, column=1, sticky='w', pady=8)

        ttk.Label(left, text='To').grid(row=4, column=0, sticky='w', pady=8)
        self.to_cb = ttk.Combobox(left, textvariable=self.to_var, state='readonly', width=20)
        self.to_cb.grid(row=4, column=1, sticky='w', pady=8)

        btn_frame = ttk.Frame(left)
        btn_frame.grid(row=5, column=0, columnspan=3, sticky='w', pady=(18, 10))
        ttk.Button(btn_frame, text='Convert', command=self.convert).pack(side='left', padx=(0, 8))
        ttk.Button(btn_frame, text='Swap', command=self.swap_units).pack(side='left', padx=(0, 8))
        ttk.Button(btn_frame, text='Clear', command=self.clear_fields).pack(side='left')

        result_card = ttk.Frame(left, style='Card.TFrame')
        result_card.grid(row=6, column=0, columnspan=3, sticky='ew', pady=(18, 0))
        result_card.configure(padding=14)

        ttk.Label(result_card, text='Result', style='Sub.TLabel').pack(anchor='w')
        ttk.Label(result_card, textvariable=self.result_var, font=('Segoe UI', 24, 'bold'), foreground=THEME['accent']).pack(anchor='w', pady=(4, 0))

        history_title = ttk.Label(right, text='History')
        history_title.pack(anchor='w')
        ttk.Label(right, text='Last 10 conversions', style='Sub.TLabel').pack(anchor='w', pady=(4, 12))

        self.history_box = tk.Listbox(right, bg=THEME['panel'], fg=THEME['text'], highlightthickness=0, bd=0, font=('Consolas', 10), activestyle='none')
        self.history_box.pack(fill='both', expand=True)

        self.value_entry.focus()
        self.root.bind('<Return>', lambda e: self.convert())

    def update_units(self):
        category = self.category_var.get()
        units = list(UNIT_MAP[category].keys())
        self.from_cb['values'] = units
        self.to_cb['values'] = units
        self.from_var.set(units[0])
        self.to_var.set(units[1] if len(units) > 1 else units[0])
        self.result_var.set('0.0')

    def convert(self):
        category = self.category_var.get()
        from_unit = self.from_var.get()
        to_unit = self.to_var.get()

        try:
            value = float(self.value_var.get())
        except ValueError:
            messagebox.showerror('Invalid Input', 'Please enter a valid number.')
            return

        if category == 'Temperature':
            result = self.convert_temperature(value, from_unit, to_unit)
        else:
            result = self.convert_linear(value, category, from_unit, to_unit)

        self.result_var.set(f'{result:.6g}')
        entry = f'{value:g} {from_unit} = {result:.6g} {to_unit}'
        self.history.insert(0, entry)
        self.history = self.history[:10]
        self.refresh_history()

    def convert_linear(self, value, category, from_unit, to_unit):
        base_value = value * UNIT_MAP[category][from_unit]
        return base_value / UNIT_MAP[category][to_unit]

    def convert_temperature(self, value, from_unit, to_unit):
        c = value
        if from_unit == 'Fahrenheit':
            c = (value - 32) * 5 / 9
        elif from_unit == 'Kelvin':
            c = value - 273.15

        if to_unit == 'Celsius':
            return c
        if to_unit == 'Fahrenheit':
            return (c * 9 / 5) + 32
        return c + 273.15

    def swap_units(self):
        a, b = self.from_var.get(), self.to_var.get()
        self.from_var.set(b)
        self.to_var.set(a)

    def clear_fields(self):
        self.value_var.set('')
        self.result_var.set('0.0')
        self.history_box.delete(0, tk.END)

    def refresh_history(self):
        self.history_box.delete(0, tk.END)
        for item in self.history:
            self.history_box.insert(tk.END, item)


if __name__ == '__main__':
    root = tk.Tk()
    app = UnitConverterApp(root)
    root.mainloop()