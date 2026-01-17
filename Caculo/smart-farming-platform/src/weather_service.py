import requests
import json
from datetime import datetime

class WeatherService:
    """
    Weather API integration for climate-aware farming decisions
    Uses OpenWeatherMap API for real-time weather data
    """
    
    def __init__(self):
        # Replace with your actual API key from OpenWeatherMap
        self.api_key = "YOUR_API_KEY"  # Get free key from openweathermap.org
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        
        # Demo mode flag (set to False when you have API key)
        self.demo_mode = True
    
    def get_weather_data(self, city_name):
        """
        Fetch current weather data for specified city
        Returns weather information relevant for farming
        """
        if self.demo_mode or self.api_key == "YOUR_API_KEY":
            return self._get_demo_weather_data(city_name)
        
        try:
            # Construct API request
            params = {
                'q': city_name,
                'appid': self.api_key,
                'units': 'metric'  # Celsius temperature
            }
            
            response = requests.get(self.base_url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                return self._parse_weather_data(data)
            else:
                print(f"Weather API Error: {response.status_code}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"Weather API Request Error: {e}")
            return None
    
    def _parse_weather_data(self, api_data):
        """
        Parse API response into farming-relevant weather data
        """
        try:
            weather_data = {
                'city': api_data['name'],
                'country': api_data['sys']['country'],
                'temperature': round(api_data['main']['temp'], 1),
                'feels_like': round(api_data['main']['feels_like'], 1),
                'humidity': api_data['main']['humidity'],
                'pressure': api_data['main']['pressure'],
                'description': api_data['weather'][0]['description'],
                'main_weather': api_data['weather'][0]['main'],
                'wind_speed': api_data['wind']['speed'],
                'wind_direction': api_data['wind'].get('deg', 0),
                'visibility': api_data.get('visibility', 10000) / 1000,  # Convert to km
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            # Add farming-specific calculations
            weather_data.update(self._calculate_farming_metrics(weather_data))
            
            return weather_data
            
        except KeyError as e:
            print(f"Weather data parsing error: {e}")
            return None
    
    def _calculate_farming_metrics(self, weather_data):
        """
        FIXED: Calculate farming-specific metrics with scientifically correct thresholds
        """
        temp = weather_data['temperature']
        humidity = weather_data['humidity']
        
        print(f"DEBUG: Weather metrics - Temp: {temp}°C, Humidity: {humidity}%")
        
        # FIXED: Scientifically accurate heat stress thresholds
        if temp > 32:  # Crops start stress above 32°C
            heat_stress = "High"
        elif temp > 28:  # Moderate stress 28-32°C
            heat_stress = "Moderate" 
        elif temp < 10:  # Cold stress below 10°C
            heat_stress = "Cold Stress"
        else:
            heat_stress = "Low"
        
        # FIXED: Irrigation needs based on crop science
        if 'rain' in weather_data['description'].lower():
            irrigation_need = "Low"  # Rain provides water
        elif humidity < 40 and temp > 25:  # Hot and dry
            irrigation_need = "High"
        elif humidity < 60 and temp > 30:  # Very hot
            irrigation_need = "High" 
        elif humidity > 80:  # High humidity, less evaporation
            irrigation_need = "Low"
        else:
            irrigation_need = "Moderate"
        
        # FIXED: Disease risk based on fungal disease conditions
        if humidity > 80 and 15 < temp < 30:  # Optimal fungal conditions
            disease_risk = "High"
        elif humidity > 70 and 20 < temp < 28:  # Moderate fungal risk
            disease_risk = "Moderate"
        elif humidity < 50 or temp > 35 or temp < 10:  # Unfavorable for fungi
            disease_risk = "Low"
        else:
            disease_risk = "Moderate"
        
        # FIXED: Spraying conditions (low humidity, low wind)
        wind_speed = weather_data.get('wind_speed', 0)
        optimal_spraying = (humidity < 75 and wind_speed < 8 and 
                          'rain' not in weather_data['description'].lower())
        
        print(f"DEBUG: Calculated metrics - Heat: {heat_stress}, Irrigation: {irrigation_need}, Disease: {disease_risk}, Spray: {optimal_spraying}")
        
        return {
            'heat_stress': heat_stress,
            'irrigation_need': irrigation_need, 
            'disease_risk': disease_risk,
            'optimal_for_spraying': optimal_spraying
        }
    
    def _get_demo_weather_data(self, city_name):
        """
        Generate realistic demo weather data when API key is not available
        """
        import random
        from datetime import datetime
        
        # Demo weather scenarios based on city patterns
        city_weather = {
            'new york': {'temp': 22, 'humidity': 68, 'desc': 'partly cloudy', 'wind': 5.2},
            'london': {'temp': 18, 'humidity': 75, 'desc': 'light rain', 'wind': 8.1},
            'mumbai': {'temp': 32, 'humidity': 85, 'desc': 'humid', 'wind': 3.8},
            'delhi': {'temp': 35, 'humidity': 45, 'desc': 'clear sky', 'wind': 4.5},
            'tokyo': {'temp': 25, 'humidity': 70, 'desc': 'scattered clouds', 'wind': 6.5},
            'sydney': {'temp': 28, 'humidity': 60, 'desc': 'sunny', 'wind': 7.2}
        }
        
        # Get city-specific weather or use default
        city_key = city_name.lower()
        if city_key in city_weather:
            scenario = city_weather[city_key]
        else:
            # Random realistic scenario for unknown cities
            scenarios = list(city_weather.values())
            scenario = random.choice(scenarios)
        
        weather_data = {
            'city': city_name,
            'country': 'Demo',
            'temperature': scenario['temp'] + random.uniform(-3, 3),
            'feels_like': scenario['temp'] + random.uniform(-2, 4),
            'humidity': max(20, min(95, scenario['humidity'] + random.randint(-10, 10))),
            'pressure': random.randint(1010, 1025),
            'description': scenario['desc'],
            'main_weather': scenario['desc'].split()[0].title(),
            'wind_speed': scenario['wind'] + random.uniform(-2, 2),
            'wind_direction': random.randint(0, 360),
            'visibility': random.uniform(8, 15),
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Add farming metrics
        weather_data.update(self._calculate_farming_metrics(weather_data))
        
        return weather_data
    
    def get_farming_advice(self, weather_data):
        """
        Generate specific farming advice based on weather conditions
        """
        advice = []
        
        temp = weather_data['temperature']
        humidity = weather_data['humidity']
        description = weather_data['description'].lower()
        
        # Temperature-based advice
        if temp > 35:
            advice.append({
                'category': 'Temperature',
                'priority': 'High',
                'message': 'Extreme heat warning! Provide shade and increase irrigation frequency.'
            })
        elif temp > 30:
            advice.append({
                'category': 'Temperature',
                'priority': 'Medium',
                'message': 'Hot weather detected. Monitor crops for heat stress and ensure adequate water.'
            })
        elif temp < 5:
            advice.append({
                'category': 'Temperature',
                'priority': 'High',
                'message': 'Frost risk! Protect sensitive crops and consider greenhouse cultivation.'
            })
        
        # Humidity and disease risk
        if weather_data['disease_risk'] == 'High':
            advice.append({
                'category': 'Disease Prevention',
                'priority': 'High',
                'message': 'High disease risk due to humidity and temperature. Improve air circulation.'
            })
        
        # Irrigation advice
        if weather_data['irrigation_need'] == 'High':
            advice.append({
                'category': 'Irrigation',
                'priority': 'Medium',
                'message': 'Low humidity and warm temperature. Increase watering frequency.'
            })
        elif 'rain' in description:
            advice.append({
                'category': 'Irrigation',
                'priority': 'Low',
                'message': 'Rain expected. Reduce or skip irrigation to prevent waterlogging.'
            })
        
        # Spraying conditions
        if weather_data['optimal_for_spraying']:
            advice.append({
                'category': 'Spraying',
                'priority': 'Low',
                'message': 'Good conditions for pesticide/fertilizer application.'
            })
        else:
            advice.append({
                'category': 'Spraying',
                'priority': 'Medium',
                'message': 'Avoid spraying due to high humidity or wind conditions.'
            })
        
        return advice