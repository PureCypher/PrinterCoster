# 3D Print Cost Calculator
A modern desktop application built with Python and ttkbootstrap for calculating 3D printing costs. This tool helps makers accurately track expenses by considering power consumption, print time, and filament usage. Features a clean, modern Bootstrap-inspired interface with a professional dark mode design.
A modern desktop application built with Python and ttkbootstrap for calculating 3D printing costs. This tool helps makers accurately track expenses by considering power consumption, print time, and filament usage. Features a clean, modern Bootstrap-inspired interface with a professional look and feel.

## Features

### User Interface
- **Dark Mode**: Professional dark theme for reduced eye strain
- **Bootstrap-Inspired Design**: Modern, clean interface using ttkbootstrap
- **Themed Elements**:
  - Dark backgrounds with optimized contrast
  - Color-coded buttons for intuitive interaction
  - Secondary-styled input sections
  - Success-styled results display

### Basic Information
- **Power Usage**: Enter your printer's power consumption in watts
- **Print Time**: Duration of the print in hours
- **Electricity Cost**: Cost per kilowatt-hour (kWh)
- **Number of Items**: Quantity being printed (for per-item cost calculation)

### Filament Management
- Add multiple filament spools to track material costs
- For each spool, specify:
  - Name/Color
  - Spool Cost ($)
  - Total Weight (g)
  - Used Weight (g)
- Dynamically add/remove spools as needed

### Cost Calculations
- Power cost based on consumption and duration
- Individual filament costs based on usage
- Total combined cost
- Cost per item when printing multiple pieces

### Additional Features
- **Modern Dark UI**: Clean, Bootstrap-inspired interface with the "darkly" theme
- **Styled Actions**:
  - Primary calculate button
  - Info-styled add spool button
  - Success/Info/Secondary-styled operation buttons
- **Dark Mode Optimized**: Carefully selected color schemes for optimal visibility
- **Save Settings**: Store frequently used configurations (printer power, filament details)
- **Load Settings**: Quickly restore saved configurations
- **Export Results**: Save calculations to a text file for record keeping
- **Reset**: Clear all fields and return to default values

## Installation

1. Clone the repository
2. Install dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Requirements
- Python 3.x
- Dependencies listed in requirements.txt:
  - ttkbootstrap >= 1.10.1

## Usage

1. Install dependencies and run the application:
   ```bash
   # Install required packages
   pip install -r requirements.txt

   # Run the calculator
   python print_cost_calculator.py
   ```

   The dark mode interface will launch automatically, optimized for comfortable viewing.

2. Enter Basic Information:
   - Input your electricity cost per kWh
   - Enter your printer's power consumption
   - Specify print duration
   - Set number of items being printed

3. Manage Filament Spools:
   - Click "Add Filament Spool" for each material used
   - Enter spool details (cost, weight, usage)
   - Remove unused spools with the "Remove" button

4. Calculate Costs:
   - Click "Calculate" to compute all costs
   - View breakdown of power and material expenses
   - See total cost and cost per item

5. Additional Operations:
   - Save your settings for future use
   - Load previously saved configurations
   - Export results to a text file
   - Reset all fields to start fresh

## Tips
- Keep track of your printer's actual power consumption for accurate calculations
- Weigh your prints to get precise filament usage
- Save frequently used configurations to speed up future calculations
- Export important calculations for project documentation
- Dark mode interface is optimized for:
  - Reduced eye strain during long sessions
  - Better visibility in low-light environments
  - Clear contrast between interactive elements
- Use the modern interface elements for improved visibility:
  - Color-coded buttons for different actions
  - Clear visual hierarchy with consistent spacing
  - Enhanced results section with primary styling

## Notes
- All monetary values are in USD ($) and weights are in grams (g)
- Power calculations use kilowatt-hours (kWh) as the base unit
- UI features:
  - "Darkly" theme from ttkbootstrap
  - Secondary-styled input frames for clear section separation
  - Success-styled results section for easy readability
  - Semantic button colors:
    - Primary: Calculate
    - Info: Add Spool
    - Success: Save Settings
    - Secondary: Export
    - Danger-outline: Remove Spool
  - Optimized spacing and padding for improved visual hierarchy
