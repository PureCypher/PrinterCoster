import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox, filedialog
import json
from pathlib import Path
class PrintCostCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("3D Print Cost Calculator")
        self.root.geometry("800x600")
        
        # Configure style for consistent appearance
        self.style = ttk.Style()
        self.style.configure("Title.TLabel", font=("", 12, "bold"))
        self.style.configure("Results.TLabel", font=("", 10))
        
        # Create and set up the main frame with scrollbar
        self.canvas = ttk.Canvas(root)
        self.scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.main_frame = ttk.Frame(self.canvas, padding=15)
        
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas_frame = self.canvas.create_window((0, 0), window=self.main_frame, anchor="nw")
        
        self.main_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)
        
        # Input variables
        self.power_cost = ttk.StringVar(value="0.15")
        self.power_usage = ttk.StringVar(value="120")
        self.print_time = ttk.StringVar(value="4.5")
        self.num_items = ttk.StringVar(value="1")
        
        # List to store filament spool frames
        self.spool_frames = []
        
        # Result variables
        self.power_cost_result = ttk.StringVar()
        self.filament_cost_result = ttk.StringVar()
        self.total_cost_result = ttk.StringVar()
        self.cost_per_item_result = ttk.StringVar()
        
        self.create_widgets()
        
    def on_frame_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
    def on_canvas_configure(self, event):
        self.canvas.itemconfig(self.canvas_frame, width=event.width)
        
    def create_spool_frame(self):
        frame = ttk.LabelFrame(self.main_frame, text=f"Filament Spool {len(self.spool_frames) + 1}",
                             padding=10, bootstyle="secondary")
        frame.grid(row=len(self.spool_frames) + 4, column=0, columnspan=2, sticky="ew", pady=5)
        
        spool_data = {
            'name': ttk.StringVar(value=f"Spool {len(self.spool_frames) + 1}"),
            'cost': ttk.StringVar(value="25.00"),
            'weight': ttk.StringVar(value="1000"),
            'used': ttk.StringVar(value="75")
        }
        
        # Spool input fields with consistent padding
        ttk.Label(frame, text="Name/Color:").grid(row=0, column=0, sticky="w", pady=2)
        ttk.Entry(frame, textvariable=spool_data['name']).grid(row=0, column=1, sticky="ew", pady=2, padx=(5, 10))
        
        ttk.Label(frame, text="Spool Cost ($):").grid(row=0, column=2, sticky="w", pady=2)
        ttk.Entry(frame, textvariable=spool_data['cost']).grid(row=0, column=3, sticky="ew", pady=2, padx=5)
        
        ttk.Label(frame, text="Total Weight (g):").grid(row=1, column=0, sticky="w", pady=2)
        ttk.Entry(frame, textvariable=spool_data['weight']).grid(row=1, column=1, sticky="ew", pady=2, padx=(5, 10))
        
        ttk.Label(frame, text="Used Weight (g):").grid(row=1, column=2, sticky="w", pady=2)
        ttk.Entry(frame, textvariable=spool_data['used']).grid(row=1, column=3, sticky="ew", pady=2, padx=5)
        
        # Remove button with warning style
        ttk.Button(frame, text="Remove", command=lambda f=frame: self.remove_spool(f),
                  bootstyle="danger-outline").grid(row=0, column=4, rowspan=2, padx=10)
        
        self.spool_frames.append({'frame': frame, 'data': spool_data})
        self.on_frame_configure()
        
    def remove_spool(self, frame):
        for idx, spool_frame in enumerate(self.spool_frames):
            if spool_frame['frame'] == frame:
                frame.destroy()
                self.spool_frames.pop(idx)
                # Renumber remaining spool frames and update their styling
                for i, sf in enumerate(self.spool_frames, 1):
                    sf['frame'].configure(text=f"Filament Spool {i}")
                    sf['frame'].configure(bootstyle="default")
                break
        self.on_frame_configure()
    
    def create_widgets(self):
        # Title with improved styling
        title_label = ttk.Label(self.main_frame, text="3D Print Cost Calculator",
                              style="Title.TLabel", bootstyle="primary")
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 15))
        
        # Basic inputs section with improved styling
        basic_frame = ttk.LabelFrame(self.main_frame, text="Basic Information",
                                   padding=15, bootstyle="secondary")
        basic_frame.grid(row=1, column=0, columnspan=2, sticky="ew", pady=5)
        
        # Grid configuration for better alignment
        basic_frame.columnconfigure(1, weight=1)
        
        labels = ["Cost of Power ($/kWh):", "Power Usage (watts):",
                 "Print Time (hours):", "Number of Items:"]
        vars = [self.power_cost, self.power_usage, self.print_time, self.num_items]
        
        for i, (label, var) in enumerate(zip(labels, vars)):
            ttk.Label(basic_frame, text=label).grid(row=i, column=0, sticky="w", pady=5)
            ttk.Entry(basic_frame, textvariable=var).grid(row=i, column=1, sticky="ew", padx=(10, 0), pady=5)
        
        # Button frame with improved styling
        button_frame = ttk.Frame(self.main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=15)
        
        ttk.Button(button_frame, text="Add Filament Spool",
                  command=self.create_spool_frame,
                  bootstyle="info").grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Reset All",
                  command=self.reset_all,
                  bootstyle="warning").grid(row=0, column=1, padx=5)
        
        # Add initial spool frame
        self.create_spool_frame()
        
        # Action buttons with bootstrap styles
        action_frame = ttk.Frame(self.main_frame)
        action_frame.grid(row=98, column=0, columnspan=2, pady=20)
        
        ttk.Button(action_frame, text="Calculate",
                  command=self.calculate,
                  bootstyle="primary").grid(row=0, column=0, padx=5)
        ttk.Button(action_frame, text="Save Settings",
                  command=self.save_settings,
                  bootstyle="success").grid(row=0, column=1, padx=5)
        ttk.Button(action_frame, text="Load Settings",
                  command=self.load_settings,
                  bootstyle="info").grid(row=0, column=2, padx=5)
        ttk.Button(action_frame, text="Export Results",
                  command=self.export_results,
                  bootstyle="secondary").grid(row=0, column=3, padx=5)
        
        # Results section with improved styling for dark mode
        results_frame = ttk.LabelFrame(self.main_frame, text="Results",
                                     padding=15, bootstyle="success")
        results_frame.grid(row=99, column=0, columnspan=2, sticky="ew", pady=10)
        
        results = [
            ("Power Cost:", self.power_cost_result),
            ("Total Filament Cost:", self.filament_cost_result),
            ("Total Cost:", self.total_cost_result),
            ("Cost per Item:", self.cost_per_item_result)
        ]
        
        for i, (label, var) in enumerate(results):
            ttk.Label(results_frame, text=label,
                     style="Results.TLabel").grid(row=i, column=0, sticky="w", pady=5, padx=5)
            ttk.Label(results_frame, textvariable=var,
                     bootstyle="primary").grid(row=i, column=1, sticky="w", pady=5, padx=5)
        
    def validate_float(self, value, field_name):
        try:
            return float(value)
        except ValueError:
            messagebox.showerror("Invalid Input", f"Please enter a valid number for {field_name}", icon="error")
            return None
            
    def calculate(self):
        # Get and validate basic inputs
        power_cost = self.validate_float(self.power_cost.get(), "Power Cost")
        power_usage = self.validate_float(self.power_usage.get(), "Power Usage")
        print_time = self.validate_float(self.print_time.get(), "Print Time")
        num_items = self.validate_int(self.num_items.get(), "Number of Items")
        
        if None in (power_cost, power_usage, print_time, num_items):
            return
            
        # Calculate power cost
        power_cost_value = (power_usage / 1000) * print_time * power_cost
        
        # Calculate total filament cost
        total_filament_cost = 0
        filament_details = []
        
        for spool in self.spool_frames:
            spool_data = spool['data']
            name = spool_data['name'].get()
            cost = self.validate_float(spool_data['cost'].get(), f"Spool Cost ({name})")
            weight = self.validate_float(spool_data['weight'].get(), f"Spool Weight ({name})")
            used = self.validate_float(spool_data['used'].get(), f"Used Weight ({name})")
            
            if None in (cost, weight, used):
                return
                
            spool_cost = (used / weight) * cost
            total_filament_cost += spool_cost
            filament_details.append(f"{name}: ${spool_cost:.2f}")
        
        # Calculate total and per-item costs
        total_cost = power_cost_value + total_filament_cost
        cost_per_item = total_cost / num_items
        
        # Update result labels with formatted values
        self.power_cost_result.set(f"${power_cost_value:.2f}")
        self.filament_cost_result.set(f"${total_filament_cost:.2f}\n" + "\n".join(filament_details))
        self.total_cost_result.set(f"${total_cost:.2f}")
        self.cost_per_item_result.set(f"${cost_per_item:.2f}")
        
    def validate_int(self, value, field_name):
        try:
            result = int(value)
            if result <= 0:
                messagebox.showerror("Invalid Input", f"{field_name} must be greater than 0", icon="error")
                return None
            return result
        except ValueError:
            messagebox.showerror("Invalid Input", f"Please enter a valid whole number for {field_name}", icon="error")
            return None
    def reset_all(self):
        # Reset basic inputs
        self.power_cost.set("0.15")
        self.power_usage.set("120")
        self.print_time.set("4.5")
        self.num_items.set("1")
        
        # Remove all spools except the first one
        while len(self.spool_frames) > 1:
            self.remove_spool(self.spool_frames[-1]['frame'])
            
        # Reset first spool
        first_spool = self.spool_frames[0]['data']
        first_spool['name'].set("Spool 1")
        first_spool['cost'].set("25.00")
        first_spool['weight'].set("1000")
        first_spool['used'].set("75")
        
        # Clear results
        self.power_cost_result.set("")
        self.filament_cost_result.set("")
        self.total_cost_result.set("")
        self.cost_per_item_result.set("")
    
    def save_settings(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json")],
            title="Save Settings As"
        )
        if not file_path:
            return
            
        settings = {
            'basic': {
                'power_cost': self.power_cost.get(),
                'power_usage': self.power_usage.get(),
                'print_time': self.print_time.get(),
                'num_items': self.num_items.get()
            },
            'spools': []
        }
        
        for spool in self.spool_frames:
            settings['spools'].append({
                'name': spool['data']['name'].get(),
                'cost': spool['data']['cost'].get(),
                'weight': spool['data']['weight'].get(),
                'used': spool['data']['used'].get()
            })
            
        with open(file_path, 'w') as f:
            json.dump(settings, f, indent=2)
            
        messagebox.showinfo("Success", "Settings saved successfully!")
    
    def load_settings(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json")],
            title="Load Settings"
        )
        if not file_path:
            return
            
        try:
            with open(file_path, 'r') as f:
                settings = json.load(f)
                
            # Load basic settings
            self.power_cost.set(settings['basic']['power_cost'])
            self.power_usage.set(settings['basic']['power_usage'])
            self.print_time.set(settings['basic']['print_time'])
            self.num_items.set(settings['basic']['num_items'])
            
            # Remove existing spools
            while self.spool_frames:
                self.remove_spool(self.spool_frames[0]['frame'])
                
            # Load spools
            for spool in settings['spools']:
                self.create_spool_frame()
                current_spool = self.spool_frames[-1]['data']
                current_spool['name'].set(spool['name'])
                current_spool['cost'].set(spool['cost'])
                current_spool['weight'].set(spool['weight'])
                current_spool['used'].set(spool['used'])
                
            messagebox.showinfo("Success", "Settings loaded successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load settings: {str(e)}")
    
    def export_results(self):
        if not self.total_cost_result.get():
            messagebox.showwarning("No Results", "Please calculate results before exporting.")
            return
            
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("CSV files", "*.csv")],
            title="Export Results As"
        )
        if not file_path:
            return
            
        try:
            with open(file_path, 'w') as f:
                f.write("3D Print Cost Calculator - Results\n")
                f.write("-" * 40 + "\n\n")
                
                f.write("Basic Information:\n")
                f.write(f"Power Cost per kWh: ${self.power_cost.get()}\n")
                f.write(f"Power Usage: {self.power_usage.get()} watts\n")
                f.write(f"Print Time: {self.print_time.get()} hours\n")
                f.write(f"Number of Items: {self.num_items.get()}\n\n")
                
                f.write("Filament Spools:\n")
                for spool in self.spool_frames:
                    data = spool['data']
                    f.write(f"{data['name'].get()}:\n")
                    f.write(f"  Cost: ${data['cost'].get()}\n")
                    f.write(f"  Weight: {data['weight'].get()}g\n")
                    f.write(f"  Used: {data['used'].get()}g\n")
                f.write("\n")
                
                f.write("Results:\n")
                f.write(f"Power Cost: {self.power_cost_result.get()}\n")
                f.write(f"Total Filament Cost: {self.filament_cost_result.get()}\n")
                f.write(f"Total Cost: {self.total_cost_result.get()}\n")
                f.write(f"Cost per Item: {self.cost_per_item_result.get()}\n")
                
            messagebox.showinfo("Success", "Results exported successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export results: {str(e)}")


def main():
    root = ttk.Window(themename="darkly")
    app = PrintCostCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()