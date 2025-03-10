# Intrusion-Detection-System
A Machine Learning-based Intrusion Detection System with a Streamlit web interface. Upload network traffic data, detect anomalies, and download results with a modern dark-themed UI. 🚀

# Intrusion Detection System

## Overview
This project is a **Machine Learning-based Intrusion Detection System** that detects anomalies in network traffic using a pre-trained model. The web interface is built using **Streamlit**.

## Features
- **Upload CSV**: Allows users to upload a CSV file containing network traffic data.
- **Data Preview**: Displays the first few rows of the uploaded dataset.
- **Intrusion Detection**: Uses a trained ML model to classify data into normal or malicious traffic.
- **Results Download**: Provides an option to download the predictions as a CSV file.
- **Dark UI Theme**: A modern, dark-themed UI for better user experience.

## Installation
### Prerequisites
Ensure you have **Python 3.8+** installed on your system.

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/intrusion-detection-system.git
   cd intrusion-detection-system
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Upload a CSV file with network traffic data.
2. View a preview of the uploaded data.
3. Click **Predict Anomalies** to detect potential intrusions.
4. Download the results for further analysis.

## File Structure
```
📂 intrusion-detection-system
│-- app.py  # Main application script
│-- intrusion_model.pkl  # Pre-trained ML model
│-- requirements.txt  # Required dependencies
│-- README.md  # Project documentation
```

## Dependencies
- **Streamlit** (For UI)
- **Pandas** (For data handling)
- **Joblib** (For loading the ML model)
- **Scikit-learn** (For ML model execution)

## Model Information
- The model is trained using a labeled dataset containing network traffic logs.
- It identifies different types of intrusions and normal traffic.
- Ensure the uploaded file has the correct feature columns for accurate predictions.

## License
This project is **open-source** under the MIT License.

## Contributing
Feel free to submit pull requests or report issues!

## Author
[Your Name](https://github.com/yourusername)



Upload CSV file to test
![Image](https://github.com/user-attachments/assets/13ddf112-a0c9-408a-9113-6220b855cc13)

See the preview of the data
![Image](https://github.com/user-attachments/assets/d3edfd93-8a46-4c01-a460-d57356dd8c40)


Initiate Prediction
![Image](https://github.com/user-attachments/assets/b35ea531-6a4f-45d3-b365-39b46c2f1d7a)
![image](https://github.com/user-attachments/assets/b4386e55-a324-496c-804a-26b87d0948c8)


Predict Data and save in 
![Image](https://github.com/user-attachments/assets/c4c5a000-e3e9-45f8-a562-967ece8ca802)
