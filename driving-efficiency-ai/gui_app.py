import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("battery_model.pkl")  # Ensure this file exists

# Tips logic
def get_tips(speed, braking, accel):
    tips = []
    if speed > 80:
        tips.append("Maintain moderate speeds.")
    if braking > 2:
        tips.append("Avoid frequent hard braking.")
    if accel > 2:
        tips.append("Accelerate smoothly.")
    return tips

# Prediction and result display
def predict_usage():
    try:
        speed = float(entry_speed.get())
        terrain = int(entry_terrain.get())
        braking = int(entry_brake.get())
        accel = float(entry_accel.get())
        temp = float(entry_temp.get())

        user_input = (speed, terrain, braking, accel, temp)
        input_df = pd.DataFrame([user_input], columns=['speed', 'terrain_type', 'braking_events', 'acceleration', 'ambient_temp'])

        usage = model.predict(input_df)[0]
        tips = get_tips(speed, braking, accel)

        # Create result window
        result_win = tk.Toplevel(app)
        result_win.title("Prediction & Tips")
        result_win.geometry("900x700")
        result_win.configure(bg="#f0f4f7")

        # Top frame for results and tips
        top_frame = tk.Frame(result_win, bg="#f0f4f7", padx=20, pady=20)
        top_frame.pack(fill="x")

        tk.Label(top_frame, text=f"🔋 Predicted Battery Usage: {usage:.2f} kWh/km", font=('Arial', 14, 'bold'), bg="#f0f4f7", anchor="w").pack(anchor="w")

        if tips:
            tk.Label(top_frame, text="💡 Tips to Improve Efficiency:", font=('Arial', 12, 'bold'), bg="#f0f4f7", pady=10).pack(anchor="w")
            for tip in tips:
                tk.Label(top_frame, text=f"• {tip}", font=('Arial', 11), bg="#f0f4f7").pack(anchor="w")
        else:
            tk.Label(top_frame, text="✅ Your driving is efficient!", font=('Arial', 12), bg="#f0f4f7").pack(anchor="w")

        # Graph frame
        graph_frame = tk.Frame(result_win, bg="#ffffff", bd=2, relief="groove", padx=10, pady=10)
        graph_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Create figure with spaced subplots
        fig = Figure(figsize=(7.5, 5.5), dpi=100)
        fig.subplots_adjust(hspace=0.5)  # Space between graphs

        # Bar chart: driving inputs
        ax1 = fig.add_subplot(211)
        ax1.bar(['Speed', 'Terrain', 'Braking', 'Accel', 'Temp'], user_input, color='skyblue')
        ax1.set_title("📊 Driving Input Summary", fontsize=10)
        ax1.set_ylabel("Value")
        ax1.grid(True, linestyle="--", alpha=0.5)

        # Line chart: battery usage
        ax2 = fig.add_subplot(212)
        ax2.plot(['Avg Usage', 'Your Prediction'], [0.5, usage], marker='o', color='green', linewidth=2)
        ax2.set_title("📈 Battery Usage Comparison", fontsize=10)
        ax2.set_ylabel("kWh/km")
        ax2.grid(True, linestyle="--", alpha=0.5)

        canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

        # Footer
        tk.Label(result_win, text="Built by Sanjeev • Driving Efficiency AI", font=('Arial', 8), bg="#f0f4f7", fg="gray").pack(pady=(0, 10))

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------------------- GUI Layout ----------------------------

app = tk.Tk()
app.title("EV Battery Usage Predictor")
app.geometry("450x400")
app.configure(bg="#e6f2ff")

tk.Label(app, text="Enter Driving Parameters", font=('Arial', 14, 'bold'), bg="#e6f2ff").pack(pady=10)

frame_inputs = tk.Frame(app, bg="#e6f2ff")
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Speed (km/h):", bg="#e6f2ff").grid(row=0, column=0, sticky='e')
entry_speed = tk.Entry(frame_inputs)
entry_speed.grid(row=0, column=1)

tk.Label(frame_inputs, text="Terrain Type (0-Flat, 1-Hill):", bg="#e6f2ff").grid(row=1, column=0, sticky='e')
entry_terrain = tk.Entry(frame_inputs)
entry_terrain.grid(row=1, column=1)

tk.Label(frame_inputs, text="Braking Events:", bg="#e6f2ff").grid(row=2, column=0, sticky='e')
entry_brake = tk.Entry(frame_inputs)
entry_brake.grid(row=2, column=1)

tk.Label(frame_inputs, text="Acceleration (m/s²):", bg="#e6f2ff").grid(row=3, column=0, sticky='e')
entry_accel = tk.Entry(frame_inputs)
entry_accel.grid(row=3, column=1)

tk.Label(frame_inputs, text="Ambient Temp (°C):", bg="#e6f2ff").grid(row=4, column=0, sticky='e')
entry_temp = tk.Entry(frame_inputs)
entry_temp.grid(row=4, column=1)

tk.Button(app, text="Predict Usage", command=predict_usage, bg="#4CAF50", fg="white", font=('Arial', 11)).pack(pady=20)

app.mainloop()
