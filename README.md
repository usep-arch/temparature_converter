# 🌡️ Robust Temperature Converter CLI

A modular and reliable Command Line Interface (CLI) application built with Python for converting temperatures between **Celsius**, **Fahrenheit**, and **Kelvin**.

The project focuses on clean architecture, strong input validation, and accurate temperature calculations while preventing common runtime errors.

---

## ✨ Features

- **Input Validation**
  - Prevents invalid data types and unexpected user inputs.
  - Blocks scientifically impossible values such as negative Kelvin temperatures.

- **Accurate Temperature Conversion**
  - Supports conversion between:
    - Celsius (°C)
    - Fahrenheit (°F)
    - Kelvin (K)
  - Provides clean output with decimal rounding for better readability.

- **Modular Architecture**
  - Separates responsibilities into different files:
    - Conversion logic
    - Input handling
    - Application control

- **Error Handling**
  - Handles invalid inputs safely.
  - Prevents crashes from `KeyboardInterrupt` and `EOFError`.
  - Provides a smooth user experience in the terminal.

---

## 🛠️ Project Structure

```text
Temperature-Converter-CLI/
│
├── temperature_converter.py  # Core temperature conversion logic
├── input_taker.py            # Handles user input and validation
└── main.py                   # Main CLI application controller
```

---

## 🚀 How to Run

1. Make sure Python is installed.

2. Clone the repository:

```bash
git clone <repository-url>
```

3. Navigate to the project folder:

```bash
cd Temperature-Converter-CLI
```

4. Run the application:

```bash
python main.py
```

---

## 📌 Example Usage

```text
Enter temperature value: 100
Convert from: Celsius
Convert to: Fahrenheit

Result: 212.00°F
```

---

## 🎯 Project Goals

This project was created to practice:

- Python modular programming
- Exception handling
- Input validation
- Clean CLI application design
- Writing maintainable code

---

## 📄 License

This project is open-source and available for learning and improvement.