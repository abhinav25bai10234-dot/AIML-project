# Laptop Price Prediction Tool

## 📌 Project Overview
This project is a Machine Learning-based application designed to estimate the retail price of laptops based on their hardware specifications. Instead of relying on a single factor like RAM, this tool uses a **Random Forest Regressor** to analyze multiple features including Brand, Processor, Graphics (GPU), and Storage capacity.

The goal of this project was to create a realistic tool that mirrors how consumers actually evaluate laptop value in the real world.

## 📊 Dataset Description
The model is trained using the **Hina Ismail Laptop Price Dataset** (data.csv). 
Key features analyzed by the model:
* **Brand:** Manufacturer (Apple, Dell, HP, etc.)
* **Processor:** CPU Type (i3, i5, i7, Ryzen, etc.)
* **RAM:** Memory capacity in GB.
* **Storage:** Disk space in GB.
* **GPU:** Graphics card brand (NVIDIA, Intel, AMD).
* **Spec Rating:** A normalized score (1-100) representing the overall build quality and features.

## 🛠️ Installation & Setup
To run this project locally, ensure you have Python 3.x installed.

1. **Clone the repository** (or download the files).
2. **Install the required libraries** using the terminal:
   ```bash
   pip install pandas scikit-learn numpy matplotlib seaborn
