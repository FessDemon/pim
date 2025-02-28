import dash
from dash import dcc, html, Input, Output, State
import requests
import pandas as pd
import plotly.express as px

# Инициализация Dash приложения с подключением внешнего CSS
app = dash.Dash(__name__, external_stylesheets=['/assets/styles.css'])

# Функция для получения курсов валют
def get_exchange_rates(base_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['rates']
    else:
        return None

# Создание DataFrame из курсов валют
def create_dataframe(rates, base_currency):
    df = pd.DataFrame(list(rates.items()), columns=['Currency', 'Rate'])
    df['Base Currency'] = base_currency
    return df

# Layout приложения
app.layout = html.Div([
    html.H1("Конвертер валют и график курсов"),

    # Выбор базовой валюты
    html.Label("Выберите базовую валюту:"),
    dcc.Dropdown(
        id='base-currency',
        options=[
            {'label': 'USD', 'value': 'USD'},
            {'label': 'EUR', 'value': 'EUR'},
            {'label': 'RUB', 'value': 'RUB'},
            {'label': 'GBP', 'value': 'GBP'}
        ],
        value='RUB'
    ),

    # График курсов валют
    dcc.Graph(id='currency-chart'),

    # Конвертер валют
    html.Div([
        html.H3("Конвертер валют"),
        html.Label("Из валюты:"),
        dcc.Input(id="from-currency", type="text", value="USD"),
        html.Label("В валюту:"),
        dcc.Input(id="to-currency", type="text", value="RUB"),
        html.Label("Сумма:"),
        dcc.Input(id="amount", type="number", value=1),
        html.Button("Конвертировать", id="convert-button", n_clicks=0),
        html.Div(id="conversion-result")
    ])
])

# Callback для обновления графика курсов
@app.callback(
    Output('currency-chart', 'figure'),
    [Input('base-currency', 'value')]
)
def update_graph(base_currency):
    rates = get_exchange_rates(base_currency)
    if rates:
        df = create_dataframe(rates, base_currency)
        fig = px.histogram(
            df,
            x="Currency",  # Ось X - названия валют
            y="Rate",      # Ось Y - значения курсов
            log_y=True,    # Логарифмическая шкала по Y
            title=f"Курс валют относительно {base_currency}"  # Заголовок графика
        )
        
        # Настройка русских подписей
        fig.update_layout(
            xaxis_title="Валюта",  # Подпись оси X
            yaxis_title="Курс (логарифмическая шкала)",  # Подпись оси Y
            font=dict(family="Arial", size=14),  # Шрифт для текста
            title_font=dict(size=20)  # Размер шрифта для заголовка
        )
        
        return fig
    else:
        return {}

# Callback для конвертации валют
@app.callback(
    Output('conversion-result', 'children'),
    [Input('convert-button', 'n_clicks')],
    [State('from-currency', 'value'),
     State('to-currency', 'value'),
     State('amount', 'value')]
)
def convert_currency(n_clicks, from_currency, to_currency, amount):
    if n_clicks > 0:
        rates = get_exchange_rates(from_currency)
        if rates and to_currency in rates:
            converted_amount = amount * rates[to_currency]
            return f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"
        else:
            return "Ошибка: Не удалось получить данные о курсах валют."
    return ""

# Запуск сервера
if __name__ == '__main__':
    app.run_server(debug=True)
