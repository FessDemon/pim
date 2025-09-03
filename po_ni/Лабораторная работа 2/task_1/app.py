import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Загрузка данных
url = ("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud"
       "/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files"
       "/airline_data.csv")
airline_data = pd.read_csv(url)

# Создание приложения Dash с внешними стилями
app = dash.Dash(__name__, external_stylesheets=['./assets/styles.css'])

# Дизайн макета приложения
app.layout = html.Div([
    # Заголовок
    html.H1("Анализ задержки вылетов самолетов"),

    # Ввод года
    html.Div([
        html.Label("Выберите год:", style={'font-weight': 'bold'}),
        dcc.Dropdown(
            id="year-dropdown",
            options=[
                {'label': str(year), 'value': year}
                for year in range(2010, 2021)],
            value=2010
        )
    ]),

    # Блок для линейных графиков
    html.Div([
        # Первый и второй графики
        html.Div([
            dcc.Graph(id="carrier-delay-graph"),
            dcc.Graph(id="weather-delay-graph")
        ], className="graph-container"),

        # Третий и четвертый графики
        html.Div([
            dcc.Graph(id="nas-delay-graph"),
            dcc.Graph(id="security-delay-graph")
        ], className="graph-container")
    ]),

    # Пятый график
    html.Div([
        dcc.Graph(id="late-aircraft-delay-graph")
    ])
])


# Функция для фильтрации данных по году
def filter_data_by_year(data, year):
    return data[data['Year'] == int(year)]


# Обратный вызов для обновления графиков
@app.callback(
    [Output("carrier-delay-graph", "figure"),
     Output("weather-delay-graph", "figure"),
     Output("nas-delay-graph", "figure"),
     Output("security-delay-graph", "figure"),
     Output("late-aircraft-delay-graph", "figure")],
    [Input("year-dropdown", "value")]
)
def update_graphs(selected_year):
    filtered_data = filter_data_by_year(airline_data, selected_year)

    # Среднемесячные значения задержек
    avg_carrier_delay = (
        filtered_data
        .groupby(['Month', 'Reporting_Airline'])['CarrierDelay']
        .mean()
        .reset_index()
    )
    avg_weather_delay = (
        filtered_data
        .groupby(['Month', 'Reporting_Airline'])['WeatherDelay']
        .mean()
        .reset_index()
    )
    avg_nas_delay = (
        filtered_data
        .groupby(['Month', 'Reporting_Airline'])['NASDelay']
        .mean()
        .reset_index()
    )
    avg_security_delay = (
        filtered_data
        .groupby(['Month', 'Reporting_Airline'])['SecurityDelay']
        .mean()
        .reset_index()
    )
    avg_late_aircraft_delay = (
        filtered_data
        .groupby(['Month', 'Reporting_Airline'])['LateAircraftDelay']
        .mean()
        .reset_index()
    )

    # График CarrierDelay
    carrier_figure = px.line(
        avg_carrier_delay,
        x='Month',
        y='CarrierDelay',
        color='Reporting_Airline',
        title='Среднемесячная задержка по вине перевозчика'
    )

    # График WeatherDelay
    weather_figure = px.line(
        avg_weather_delay,
        x='Month',
        y='WeatherDelay',
        color='Reporting_Airline',
        title='Среднемесячная задержка из-за погоды'
    )

    # График NASDelay
    nas_figure = px.line(
        avg_nas_delay,
        x='Month',
        y='NASDelay',
        color='Reporting_Airline',
        title='Среднемесячная задержка из-за НВС'
    )

    # График SecurityDelay
    security_figure = px.line(
        avg_security_delay,
        x='Month',
        y='SecurityDelay',
        color='Reporting_Airline',
        title='Среднемесячная задержка из-за безопасности'
    )

    # График LateAircraftDelay
    late_aircraft_figure = px.line(
        avg_late_aircraft_delay,
        x='Month',
        y='LateAircraftDelay',
        color='Reporting_Airline',
        title='Среднемесячная задержка из-за опозданий самолета'
    )

    return (
        carrier_figure,
        weather_figure,
        nas_figure,
        security_figure,
        late_aircraft_figure
    )


# Запуск приложения
if __name__ == "__main__":
    app.run_server(debug=True)
