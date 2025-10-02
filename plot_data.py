import matplotlib.pyplot as plt
from data_loader import load_db_temperature
 
def plot_temperature_data():
    # Load the data
    df = load_db_temperature()

    # Plot the data
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['temp'], label='CPU Temperature (°C)', color='blue')

    plt.title('Database CPU Temperature Over Time')
    plt.xlabel('Time')  
    plt.ylabel('CPU Temperature (°C)')
    plt.legend()    
    plt.grid(True)

    # Show the plot
    plt.show()

if __name__ == "__main__":
    plot_temperature_data()
