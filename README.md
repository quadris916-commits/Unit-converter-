# Advanced Unit Converter

A modern Python Tkinter app for converting between different units with a sleek dark UI.

## Features

- Dark themed advanced interface.
- Length conversion.
- Weight conversion.
- Temperature conversion.
- Time conversion.
- Swap units button.
- Conversion history panel.
- Easy-to-use dropdown menus.

## Supported Categories

### Length
- Millimeter
- Centimeter
- Meter
- Kilometer
- Inch
- Foot
- Yard
- Mile

### Weight
- Milligram
- Gram
- Kilogram
- Ton
- Pound
- Ounce

### Temperature
- Celsius
- Fahrenheit
- Kelvin

### Time
- Second
- Minute
- Hour
- Day
- Week

## Requirements

- Python 3.8 or above
- Tkinter (usually included with Python)

## How to Run

1. Save the file `advanced_unit_converter.py`.
2. Open terminal in the same folder.
3. Run:

```bash
python advanced_unit_converter.py
```

## How to Use

1. Select a unit category.
2. Enter the value you want to convert.
3. Choose the **From** and **To** units.
4. Click **Convert**.
5. Use **Swap** to switch units quickly.
6. Use **Clear** to reset the fields.

## Example

- `10 Kilometer = 10000 Meter`
- `100 Celsius = 212 Fahrenheit`
- `2 Hour = 7200 Second`

## File

- `advanced_unit_converter.py` — main application file.

## Notes

- Temperature conversion is handled separately because it does not use a simple multiplier.
- The history panel stores the last 10 conversions during runtime.

## Future Improvements

- Save history to a file.
- Add currency converter.
- Add area and volume units.
- Add light theme toggle.
