from dash import dcc,Dash, html, Input, Output, State
import dash_ag_grid as dag
import pandas as pd

app = Dash(__name__)

df = pd.DataFrame({
    "letter_1": ['A', '', '', '', ''],
    "letter_2": ['R', '', '', '', ''],
    "letter_3": ['O', '', '', '', ''],
    "letter_4": ['S', '', '', '', ''],
    "letter_5": ['E', '', '', '', ''],
    "letter_1_score": [2, -1, -1, -1, -1],
    "letter_2_score": [1, -1, -1, -1, -1],
    "letter_3_score": [0, -1, -1, -1, -1],
    "letter_4_score": [0, -1, -1, -1, -1],
    "letter_5_score": [0, -1, -1, -1, -1],
})

column_defs = []
for column in df.columns:
    col_num = int(column[7:8])
    is_score_column = column[-6:] == '_score'
    column_def = {
        "field": column, 
        'cellStyle': {
            "styleConditions": [
                {
                    "condition": f"params.data.letter_{col_num}_score == 2",
                    "style": {"backgroundColor": "#79A86B"},
                },
                {
                    "condition": f"params.data.letter_{col_num}_score == 1",
                    "style": {"backgroundColor": "#C5B565"},
                },
                {
                    "condition": f"params.data.letter_{col_num}_score == 0",
                    "style": {"backgroundColor": "#797C7E"},
                },
                {
                    "condition": f"params.data.letter_{col_num}_score == -1",
                    "style": {"backgroundColor": "#D3D6DA"},
                },
            ],
            "defaultStyle": {"backgroundColor": "#D3D6DA", "textAlign": "center"},
        },
    }
    if is_score_column:
        column_def['hide'] = 'true'
    
    column_defs.append(column_def)

default_cell_details = "text-center"

grid = dag.AgGrid(
    id="wordle-grid",
    rowData=df.to_dict("records"),
    columnDefs=column_defs,
    defaultColDef={"minWidth":50, "maxWidth": 50},
    columnSize="sizeToFit",
    dashGridOptions={"animateRows": False, "headerHeight":0, "editable": True, "flex": 1}
)

dcc.Input(id="dfalse", type="text", placeholder="Debounce False")

input_field = html.Div(
    [
        dcc.Input(id="word_input", type="text", placeholder="", debounce=True),
        html.Hr(),
        html.Div(id="number-out"),
    ]
)

@app.callback(
    Output("number-out", "children"),
    Input("word_input", "value"),
    State("wordle-grid", "rowData")
)
def update(word_input, row_data):
    # print(row_data.iloc[:, 0])
    word_from_table = ''
    for i in range(1, 6):
        word_from_table += row_data[0][f'letter_{i}']
    return f'The input word is: {word_input} and {word_from_table}'

app.layout = html.Div([html.H4("Wordle"), grid, html.Div(id="quickstart-output"), input_field])


if __name__ == '__main__':
    app.run(debug=True)