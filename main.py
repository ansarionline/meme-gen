from dash import Dash, dcc, html, Input, Output, no_update
from skimage import io as skio, data
import numpy as np
import plotly.express as px
import dash_bootstrap_components as dbc
import stuff
import base64
import io

def init_plot():
    image = data.chelsea()
    fig = px.imshow(image)
    fig.update_layout(
    xaxis_visible=False, 
    yaxis_visible=False, 
    showlegend=False,
    dragmode="drawrect")
    return fig

app = Dash(__name__,
            external_stylesheets=[dbc.themes.BOOTSTRAP],
        meta_tags=[{"name": "viewport", 
                "content": 
        "width=device-width,initial-scale=1,maximum-scale=1.5,minimum-scale=0.5"}],
        prevent_initial_callbacks=True
        )

config = {
    "modeBarButtonsToAdd": [
        "drawline",
        "drawopenpath",
        "drawclosedpath",
        "drawcircle",
        "drawrect",
        "eraseshape",
    ],
    "modeBarButtonsToRemove": [
        "toImage",
        "resetScale2d",
    ],
    "displaylogo":False
}


app.layout = [
    dbc.InputGroup([html.Img(src='assets/favicon.webp',
            style={'width':'50px','height':'50px',"margin":'5px','border-radius':'15px'}),
            html.H2('AO MeMe Generator Pro.',style={"margin":'5px'})],
            style={'backgroundColor':'#eeeeee'}),
    dbc.Row([
        dbc.Col([
            html.H4("Image"),
                    dcc.Upload(
            id="upload-image",
            children=html.Div(
                ["Drag and drop or ", html.A("Select an Image")],
                className="text-center border p-3 bg-light",
            ),
            multiple=False,
        ),
            dcc.Graph(
                    id='img-preview',
                    style={"width": "95%","marginTop": "5px"},
                    config=config,
                    figure=init_plot()
            )        
        ]),
        dcc.Store(id='text-store',data=[]),
        stuff.meme_generation_column()
    ],style={'margin':'10px','alignItems':'row',"border":'2px'}),
    html.Footer('AO Meme Generator © Copyright 2025: Developed by AnsariCodes.')]

stuff.register_meme_generation_column(app)
@app.callback(
    Output("img-preview", "figure"),
    Input("upload-image", "contents")
)
def update_image(contents):
    if contents is None:
        return no_update
    
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        image = skio.imread(io.BytesIO(decoded))
        image = np.array(image, dtype=np.uint8)
        fig = px.imshow(image)
        fig.update_layout(
    xaxis_visible=False, 
    yaxis_visible=False, 
    showlegend=False,
    dragmode="drawrect",
    margin=dict(l=0,r=0,t=0,b=0)
        )
        return fig
    except Exception as e:
        print(e)
        return no_update

if __name__ == '__main__':
    app.run_server(debug=False)
