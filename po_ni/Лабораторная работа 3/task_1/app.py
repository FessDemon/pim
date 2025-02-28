import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Загрузка данных
url = ("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
       "IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv")
df = pd.read_csv(url)
# df

# Создание приложения Dash с внешними стилями
app = dash.Dash(__name__, external_stylesheets=['./assets/styles.css'])

# Layout приложения
app.layout = html.Div([
    html.H1("Анализ запусков SpaceX", style={'text-align': 'center'}),

    # Выпадающий список для выбора стартового комплекса
    dcc.Dropdown(
        id='site-dropdown',
        options=[
            {'label': 'Все стартовые комплексы', 'value': 'ALL'},
            * [{'label': site, 'value': site} for site in df['Launch Site'].unique()]
        ],
        value='ALL',
        placeholder="Выберите стартовый комплекс",
        searchable=True,
        style={'width': '50%', 'margin': 'auto'}
    ),

    # Круговая диаграмма
    html.Div(dcc.Graph(id='success-pie-chart'), style={'margin': '20px'}),

    # Ползунок для выбора диапазона полезной нагрузки
    html.P("Диапазон массы полезной нагрузки (кг):"),
    dcc.RangeSlider(
        id='payload-slider',
        min=df['Payload Mass (kg)'].min(),
        max=df['Payload Mass (kg)'].max(),
        step=1000,
        marks={str(i): str(i) for i in range(0, 10001, 2500)},
        value=[df['Payload Mass (kg)'].min(), df['Payload Mass (kg)'].max()]
    ),

    # Точечная диаграмма
    html.Div(dcc.Graph(id='success-payload-scatter-chart'), style={'margin': '20px'})
])


# Callback для обновления круговой диаграммы
@app.callback(
    Output('success-pie-chart', 'figure'),
    [Input('site-dropdown', 'value')]
)
def update_pie_chart(selected_site):
    if selected_site == 'ALL':
        # Фильтруем только успешные запуски (class == 1)
        success_only_df = df[df['class'] == 1]

        # Группировка данных по стартовым комплексам и подсчет успешных запусков
        success_counts = success_only_df.groupby('Launch Site').size().reset_index(name='count')

        # Создание списка уникальных стартовых комплексов
        launch_sites = success_counts['Launch Site'].unique()

        # Определение цветовой палитры для стартовых комплексов
        color_map = px.colors.qualitative.Plotly[:len(launch_sites)]  # Берем столько цветов, сколько комплексов

        # Создание круговой диаграммы для всех стартовых комплексов с учетом только успешных запусков
        fig = px.pie(
            success_counts,
            values='count',
            names='Launch Site',
            title='Общая успешность запусков по всем стартовым комплексам',
            color='Launch Site',  # Используем стартовые комплексы как категории для цветов
            color_discrete_sequence=color_map,  # Уникальные цвета для каждого комплекса
            labels={'Launch Site': 'Стартовый комплекс'}
        )
        fig.update_traces(textinfo='percent+label')  # Показывать проценты и метки

    else:
        # Фильтрация данных для выбранного стартового комплекса
        filtered_df = df[df['Launch Site'] == selected_site]
        success_counts = filtered_df['class'].value_counts().reset_index()
        success_counts.columns = ['class', 'count']

        # Создание круговой диаграммы для конкретного стартового комплекса
        fig = px.pie(
            success_counts,
            values='count',
            names='class',
            title=f'Успешность запусков для {selected_site}',
            color='class',
            color_discrete_map={0: 'red', 1: 'green'},  # Цветовая кодировка для успешности
            labels={'class': 'Результат миссии'}
        )

    return fig


# Callback для обновления точечной диаграммы
@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    [Input('site-dropdown', 'value'), Input('payload-slider', 'value')]
)
def update_scatter_chart(selected_site, payload_range):
    low, high = payload_range
    filtered_df = df[(df['Payload Mass (kg)'] >= low) & (df['Payload Mass (kg)'] <= high)]

    if selected_site != 'ALL':
        filtered_df = filtered_df[filtered_df['Launch Site'] == selected_site]

    fig = px.scatter(
        filtered_df,
        x='Payload Mass (kg)',
        y='class',
        color='Booster Version Category',
        title='Зависимость успешности запуска от массы полезной нагрузки',
        labels={
            'Payload Mass (kg)': 'Масса полезной нагрузки (кг)',
            'class': 'Результат миссии',
            'Booster Version Category': 'Категория ускорителя'
        }
    )
    return fig


# Запуск сервера
if __name__ == '__main__':
    app.run_server(debug=True)
