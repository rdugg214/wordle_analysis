from dash import Dash, html, Input, Output
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

grid = dag.AgGrid(
    id="quickstart-grid",
    rowData=df.to_dict("records"),
    columnDefs=[{"field": i} for i in df.columns],
    defaultColDef={"minWidth":100, "maxWidth": 100},
    columnSize="sizeToFit",
)

cell_style = {
    "styleConditions": [
        {
            "condition": "params.data.letter_1_score >= 2",
            "style": {"backgroundColor": "#79A86B"},
        },
        {
            "condition": "params.data.letter_1_score == 2",
            "style": {"backgroundColor": "#79A86B"},
        },
        {
            "condition": "params.data.letter_1_score == 1",
            "style": {"backgroundColor": "#C5B565"},
        },
        {
            "condition": "params.data.letter_1_score == 0",
            "style": {"backgroundColor": "#797C7E"},
        },
        {
            "condition": "params.data.letter_1_score == -1",
            "style": {"backgroundColor": "#D3D6DA"},
        },
    ],
    "defaultStyle": {"backgroundColor": "#D3D6DA", "textAlign": "center"},
}

column_defs = []
for column in df.columns:
    col_num = int(column[7:8])
    column_defs.append(
        {
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
            }
        }
    )

default_cell_details = "text-center"

grid = dag.AgGrid(
    id="quickstart-grid",
    rowData=df.to_dict("records"),
    columnDefs=column_defs,
    defaultColDef={"minWidth":50, "maxWidth": 50},
    columnSize="sizeToFit",
    dashGridOptions={"animateRows": False}
)

app.layout = html.Div([html.H4("Wordle"), grid, html.Div(id="quickstart-output")])


@app.callback(
    Output("quickstart-output", "children"), Input("quickstart-grid", "cellClicked")
)
def display_cell_clicked_on(cell):
    if cell is None:
        return "Click on a cell"
    return f"clicked on cell value:  {cell['value']}, column:   {cell['colId']}, row index:   {cell['rowIndex']}"


if __name__ == '__main__':
    app.run(debug=True)