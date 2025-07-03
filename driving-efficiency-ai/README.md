# ⚡ Driving Efficiency AI - EV Battery Usage Predictor

This project predicts EV (Electric Vehicle) battery usage per kilometer using real-time driving inputs like speed, terrain type, braking, acceleration, and ambient temperature. It provides actionable tips and graphical visualizations to help improve driving efficiency.



## 🧠 Features

- 🔋 Predicts battery usage using a trained ML model
- 💡 Offers suggestions for energy-efficient driving
- 📊 Displays user inputs and predictions in graphs
- 🖥️ User-friendly GUI using Tkinter


## 📁 Project Structure

driving-efficiency-ai/
│
├── gui_app.py # Main GUI application
├── train_model.py # Script to train the model
├── generate_dataset.py # Script to generate sample data
├── battery_model.pkl # Trained battery prediction model
├── driving_data.csv # Sample dataset
├── README.md # You're here!
└── requirements.txt # Python dependencies

## 🔧 Installation

```bash
# Clone this repository
git clone https://github.com/Sanjeev-ssp/driving-efficiency-ai.git
cd driving-efficiency-ai

# Install dependencies
pip install -r requirements.txt

# Run the GUI
python gui_app.py

