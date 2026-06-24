# temperature_converter.py 


class TemperatureConverter:
    def _validate_kelvin(self, kelvin: float) -> None:
        """Raise valuerror if input kelvin is negetive"""
        if kelvin < 0:
            raise ValueError("Kelvin scale temperature can't be negative!")
    
    def _round_value(self, value: float, decimals: int = 2) -> float:
        """Function to round long float value for readable"""
        return round(value, decimals)
        
    def celsius_to_kelvin(self, celsius: float = 0.0) -> float:
        """Function for convert celsius to kelvin"""
        result = celsius + 273.15
        self._validate_kelvin(result)
        return self._round_value(result)
        

    def kelvin_to_celsius(self, kelvin: float = 273.15) -> float:
        """Function for convert kelvin to celsius"""
        self._validate_kelvin(kelvin)
        result = kelvin - 273.15
        return self._round_value(result)

    def celsius_to_fahrenheit(self, celsius: float = 0.0) -> float:
        """Function for convert celsius to fahrenheit"""
        result = (celsius * 9 / 5) + 32
        return self._round_value(result)

    def fahrenheit_to_celsius(self, fahrenheit: float = 32.0) -> float:
        """Function for convert fahrenheit to celsius"""
        result = (fahrenheit - 32) * 5 / 9
        return self._round_value(result)

    def fahrenheit_to_kelvin(self, fahrenheit: float = 32.0) -> float:
        """Function for convert fahrenheit to kelvin"""
        result = (fahrenheit - 32) * 5 / 9 + 273.15
        self._validate_kelvin(result)
        return self._round_value(result)

    def kelvin_to_fahrenheit(self, kelvin: float = 273.15) -> float:
        """Function for convert kelvin to fahrenheit"""
        self._validate_kelvin(kelvin)
        result = (kelvin - 273.15) * 9 / 5 + 32
        return self._round_value(result)
