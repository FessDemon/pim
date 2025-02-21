import dash
from dash import dcc, html, callback, Output, Input
import pandas as pd
import plotly.express as px
import os

# Создание приложения Dash
app = dash.Dash(__name__, external_stylesheets=['styles.css'])

# Путь к данным
DATA_PATH = "po_ni/Лабораторная работа 2/task_2/data/covid_polymatica.xlsx"

# Загрузка данных
if not os.path.exists(DATA_PATH):
    raise FileNotFoundError("Файл с данными не найден. "
                            "Убедитесь, что данные находятся в папке 'data'.")

df = pd.read_excel(DATA_PATH)
df = df.rename(columns={'Регион ': 'region',
                        'Федеральный округ': 'FederalDistrict',
                        'дата': 'date',
                        'случаи заболевания': 'casesofdisease',
                        'население': 'population',
                        'количество смертей': 'numberofdeaths'})
# df
# df.info()

# df['date'] = pd.to_datetime(df['date'])
# df
# df.info()


# Разметка приложения
app.layout = html.Div([
    html.H1("Статистика по COVID-19 в России", className="title"),

    # Выбор региона
    html.Label("Выберите регион:", className="label"),
    dcc.Dropdown(
        id='region-dropdown',
        options=[
            {'label': region, 'value': region}
            for region in df['region'].unique()],
        value=df['region'].iloc[0],
        className="dropdown"
    ),

    # Выбор начальной даты
    html.Label("Начальная дата:", className="label"),
    dcc.DatePickerSingle(
        id='start-date-picker',
        min_date_allowed=df['date'].min(),
        max_date_allowed=df['date'].max(),
        initial_visible_month=df['date'].min(),
        date=df['date'].min(),
        className="datepicker"
    ),

    # Выбор конечной даты
    html.Label("Конечная дата:", className="label"),
    dcc.DatePickerSingle(
        id='end-date-picker',
        min_date_allowed=df['date'].min(),
        max_date_allowed=df['date'].max(),
        initial_visible_month=df['date'].max(),
        date=df['date'].max(),
        className="datepicker"
    ),

    # График заболевших
    dcc.Graph(id='confirmed-graph', className="graph"),

    # График смертей
    dcc.Graph(id='deaths-graph', className="graph")
])


# Callback для обновления графиков
@callback(
    [Output('confirmed-graph', 'figure'),
     Output('deaths-graph', 'figure')],
    [Input('region-dropdown', 'value'),
     Input('start-date-picker', 'date'),
     Input('end-date-picker', 'date')]
)
def update_graphs(region, start_date, end_date):
    filtered_df = df[(df['region'] == region) &
                     (df['date'] >= start_date) &
                     (df['date'] <= end_date)]

    # График заболевших
    confirmed_fig = px.line(filtered_df,
                            x='date',
                            y='casesofdisease',
                            title=f"Количество заболевших в {region}")
    confirmed_fig.update_layout(xaxis_title="Дата", yaxis_title="Заболевшие")

    # График смертей
    deaths_fig = px.line(filtered_df,
                         x='date',
                         y='numberofdeaths',
                         title=f"Количество смертей в {region}")
    deaths_fig.update_layout(xaxis_title="Дата", yaxis_title="Смерти")

    return confirmed_fig, deaths_fig


if __name__ == '__main__':
    app.run_server(debug=True)
