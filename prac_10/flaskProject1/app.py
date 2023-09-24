from flask import Flask

app = Flask(__name__)


# Temperature conversion function (Celsius to Fahrenheit)
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# Route for Celsius to Fahrenheit conversion
@app.route('/f/<celsius_str>')
def convert_celsius_to_fahrenheit(celsius_str):
    try:
        celsius = float(celsius_str)

        fahrenheit = celsius_to_fahrenheit(celsius)

        return f"{fahrenheit}"
    except ValueError:
        return "Invalid input."


if __name__ == '__main__':
    app.run()
