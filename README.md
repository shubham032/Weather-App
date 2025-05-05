# 🌦️ Weather App

A simple Django-based weather application that allows users to search for the current weather of any city using the OpenWeatherMap API.

## 📋 Features

- 🌍 Search for weather by city name.
- 🌡️ Displays temperature, weather condition, and description.
- 🌤️ Shows an icon representing the current weather.
- 🖥️ Responsive design with a clean and modern UI.

## 🛠️ Technologies Used

- **Backend**: Django 5.1.6 🐍
- **Frontend**: HTML5, CSS3 🎨
- **API**: OpenWeatherMap API 🌐

## 🚀 Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites

- Python 3.8+ 🐍
- Django 5.1.6 🐍
- An OpenWeatherMap API key 🔑

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/weather-app.git
   cd weather-app

2.Create a virtual environment and activate it:
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
3.Install the required dependencies:
   pip install django requests
   
4.Add your OpenWeatherMap API key in the views.py file:
   api_key = 'your_openweathermap_api_key'
   
5.Run the development server:
   python manage.py runserver
6.Open your browser and navigate to:
  http://127.0.0.1:8000/
## 📂 Project Structure
weather_app/
├── weather_app/
│   ├── [settings.py]      # Project settings
│   ├── [urls.py]           # Project URL configuration
│   ├── wsgi.py           # WSGI application
├── weather_api/
│   ├── templates/
│   │   ├── [home.html]     # Main template for the weather app
│   ├── [views.py]          # View logic for the app
│   ├── [urls.py]           # App-specific URL configuration
│   ├── [models.py]         # Models (currently unused)
├── [manage.py]             # Django management script

## 🌟 Features in Detail
## 🌍 Search Weather by City
Users can enter the name of a city in the search bar to get the current weather details.

## 🌡️ Weather Details
The app displays:

- City name
- Weather condition (e.g., Clear, Rainy)
- Temperature in Celsius
- Weather description
- Weather icon
## 🎨 Responsive Design
The app uses CSS Flexbox for a clean and responsive layout.
## 🛡️ License
This project is licensed under the MIT License. See the LICENSE file for details.

## 🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

