from dash import dcc,Dash, html, Input, Output, State
import dash_ag_grid as dag
import pandas as pd
from nyt_games.games.wordle.wordle_game import Wordle

app = Dash(__name__)

df = pd.DataFrame({
    "letter_1": ['', '', '', '', ''],
    "letter_2": ['', '', '', '', ''],
    "letter_3": ['', '', '', '', ''],
    "letter_4": ['', '', '', '', ''],
    "letter_5": ['', '', '', '', ''],
    "letter_1_score": [-1, -1, -1, -1, -1],
    "letter_2_score": [-1, -1, -1, -1, -1],
    "letter_3_score": [-1, -1, -1, -1, -1],
    "letter_4_score": [-1, -1, -1, -1, -1],
    "letter_5_score": [-1, -1, -1, -1, -1],
})

def setup_grid_values() -> list[dict[str, str|int]]:
    base_grids = {}
    for i in range(1, 6):
        base_grids[f'letter_{i}'] = ''

    for i in range(1, 6):
        base_grids[f'letter_{i}_score'] = -1

    grid_values = []
    for i in range(6):
        grid_values.append(base_grids)
    
    return grid_values

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
    rowData=setup_grid_values(),
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

wordle = Wordle()
wordle.create_new_game()

@app.callback(
    Output("wordle-grid", "rowData"),
    Input("word_input", "value"),
    State("wordle-grid", "rowData")
)
def update(word_input:str, row_data:list[dict[str, str|int]]):
    if word_input is None or len(word_input) != 5:
        return row_data
    
    to_update_index = 0
    for i in range(6):
        if row_data[i]['letter_1_score'] == -1:
            to_update_index = i
            break
    
    for i, letter in enumerate(word_input.upper()):
        row_data[to_update_index][f'letter_{i+1}'] = letter

    word_score = wordle.make_guess(word_input)

    for i, letter_score in enumerate(word_score):
        row_data[to_update_index][f'letter_{i+1}_score'] = letter_score

    return row_data

app.layout = html.Div([html.H4("Wordle"), grid, html.Div(id="quickstart-output"), input_field])


if __name__ == '__main__':
    app.run(debug=True)