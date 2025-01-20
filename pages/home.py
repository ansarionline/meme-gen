from dash import dcc, html, Input, Output, no_update, State
from skimage import io as skio
import skimage.data as data
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

image_formats = [
    {'label': 'PNG', 'value': 'png'},
    {'label': 'JPEG', 'value': 'jpeg'},
    {'label': 'SVG', 'value': 'svg'},
    {'label': 'PDF', 'value': 'pdf'},
    {'label': 'EPS', 'value': 'eps'},
    {'label': 'GIF', 'value': 'gif'},
    {'label': 'WebP', 'value': 'webp'},
    {'label': 'TIFF', 'value': 'tiff'},
    {'label': 'BMP', 'value': 'bmp'},
    {'label': 'JSON', 'value': 'json'}
]

fonts = [
    {"label": "Arial", "value": "Arial, sans-serif"},
    {"label": "Helvetica", "value": "Helvetica, sans-serif"},
    {"label": "Times New Roman", "value": "'Times New Roman', Times, serif"},
    {"label": "Verdana", "value": "Verdana, Geneva, sans-serif"},
    {"label": "Tahoma", "value": "Tahoma, Geneva, sans-serif"},
    {"label": "Georgia", "value": "Georgia, serif"},
    {"label": "Courier New", "value": "'Courier New', Courier, monospace"},
    {"label": "Comic Sans MS", "value": "'Comic Sans MS', cursive, sans-serif"},
    {"label": "Roboto", "value": "'Roboto', sans-serif"},
    {"label": "Lato", "value": "'Lato', sans-serif"},
    {"label": "Open Sans", "value": "'Open Sans', sans-serif"},
    {"label": "Montserrat", "value": "'Montserrat', sans-serif"},
    {"label": "Merriweather", "value": "'Merriweather', serif"},
    {"label": "Ubuntu", "value": "'Ubuntu', sans-serif"},
    {"label": "Pacifico", "value": "'Pacifico', cursive"}]

def open_d(app, modal, opener):
    @app.callback(
        Output(modal, "is_open", allow_duplicate=True),
        Input(opener, 'n_clicks')
    )
    def toggle_modal(open_clicks):
        return True

def meme_generation_column():
    return dbc.Col(
        [
            html.H4("Text", className="mb-4"),
            dbc.Form(
                [
                    dbc.InputGroup([
                    html.H6("Text", className="mb-4",style={'marginRight':'25px'}),
                        dbc.Input(type="text", id="meme-text", placeholder="Enter text", className="mb-2")]),
                    dbc.InputGroup([
                    html.H6("Pos", className="mb-4",style={'marginRight':'30px'}),
                        dbc.Input('text-x', placeholder='Horizontal Pos (0-1)', type='number', min=0, max=1, value=0.5),
                        dbc.Input('text-y', placeholder='Vertical Pos (0-1)', type='number', min=0, max=1, value=0.5),
                        dbc.Input('text-angle', placeholder='Angle (0-180)', type='number', min=0, max=180, value=0)
                    ]),
                    dbc.InputGroup([
                    html.H6("Font", className="mb-4",style={'marginRight':'27px'}),
                        dbc.Select(id='text-font', placeholder='Font', options=fonts, value="Arial, sans-serif"),
                        dbc.Input(id='text-size', placeholder='Size', value=20, type='number', min=5, step=1),
                        dbc.Input(type="color", id="text-color", value="#000000", className="mb-2", placeholder="Text Color", style={"height": '40px'})
                    ])
                ]
            ),
            html.H4("Background", className="mb-4"),
            dbc.Form([
                dbc.InputGroup([
                    html.H6("Box", className="mb-4",style={'marginRight':'30px'}),
                                dbc.Input(type="number", id="border-pad", value=1, className="mb-2",
                                        placeholder="Area", style={"height": '40px'}),
                                dbc.Input(type="color", id="border-bg", value="#FFFFFF", 
                                        className="mb-2", placeholder="Box Bg", style={"height": '40px'}),
                                dbc.Input(type="number", id="border-ops", value=0.1, min=0,max=1,step=0.005,
                                        className="mb-2", placeholder="Box Opacity", style={"height": '40px'})]),
                dbc.InputGroup([
                    html.H6("Border", className="mb-4"),
                                dbc.Input(type="number", id="border-width",
                                        placeholder="Border Width", className="mb-2", value=0),
                                dbc.Input(type="color", id="border-color", value="#FFFFFF", 
                                        className="mb-2", placeholder="Border Color", style={"height": '40px'})]),
                dbc.ButtonGroup([dbc.Button("Add Text", id="add-text-btn",
                                color="primary"),
                                dbc.Select(id='text-to-remove',style={'marginLeft':'40%'}),
                                dbc.Button("Remove", id="rem-text-btn",
                                color="danger")],style={'width':'100%'})
            ]),
            html.H4("Generate", className="mb-4"),
            dbc.Form([
                dbc.InputGroup([
                    dbc.Input(type="number", id="width", value=1080,
                            className="mb-2", placeholder="Width", style={"height": '40px'}),
                    dbc.Input(type="number", id="height", value=720,
                            className="mb-2", placeholder="Height", style={"height": '40px'}),
                    dbc.Select(id="formatttt", value='png', className="mb-2",
                    placeholder="Format", style={"height": '40px'},options=image_formats),
                    dbc.Button("Generate", id="gen-btn", color="success")
                ]),
            ]),
            dbc.Modal([
                dbc.ModalTitle('Done'),
                dbc.ModalBody([
                    dbc.Label('Done!!!\nClick the `Save` to save.'),
                    dbc.Label('',id='status'),
                    dbc.Button("Save", id="save-btn", color="success")])
            ], id='dialog')
        ]
    )

# Validate value
def validate(value, els):
    return value if value is not None and len(str(value)) > 0 else els

def register_meme_generation_column(app):
    open_d(app, 'dialog', 'gen-btn')

    @app.callback(
        Input('gen-btn', 'n_clicks'),
        State('img-preview', 'figure')
    )
    def do_export(n, fig):
        if n:
            fig = go.Figure(fig)
            fig.to_image(format='png')
        return
    @app.callback(
        [Output('img-preview', 'figure', allow_duplicate=True),
        Output('text-store', 'data', allow_duplicate=True),
        Output('text-to-remove', 'options', allow_duplicate=True)],
        Input('rem-text-btn', 'n_clicks'),
        State('text-to-remove', 'value'),
        State('text-store', 'data'),
        State('img-preview', 'figure')
    )
    def remove_text(n_clicks, text_to_remove, data, fig):
        from dash import callback_context
        fig = go.Figure(fig)
        if not callback_context.triggered:
            return fig, data, [{'label': 'No text to remove', 'value': ''}]
        triggered_input = callback_context.triggered[0]['prop_id'].split('.')[0]
        if triggered_input == 'rem-text-btn' and n_clicks:
            global filtered_data
            filtered_data = [annotation for annotation in data if annotation['text'] != text_to_remove]
            if text_to_remove:
                filtered_data = [annotation for annotation in data if annotation['text'] != text_to_remove]                
                fig.update_layout(annotations=filtered_data)
                options = [{'label': a['text'], 'value': a['text']} for a in filtered_data]
            else:
                options = [{'label': 'No text to remove', 'value': ''}]
        else:
            options = [{'label': 'No text to remove', 'value': ''}]
        return fig, filtered_data if n_clicks else data, options

    @app.callback(
        [Output('img-preview', 'figure', allow_duplicate=True),
         Output('text-store', 'data', allow_duplicate=True),
         Output('text-to-remove', 'options', allow_duplicate=True)],
        Input('add-text-btn', 'n_clicks'),
        [
            State('meme-text', 'value'),
            State('text-color', 'value'),
            State('text-x', 'value'),
            State('text-y', 'value'),
            State('text-font', 'value'),
            State('text-size', 'value'),
            State('text-angle', 'value'),
            State('border-pad', 'value'),
            State('border-bg', 'value'),
            State('border-ops', 'value'),
            State('border-width', 'value'),
            State('border-color', 'value'),
            State('img-preview', 'figure'),
            State('text-store', 'data')
        ]
    )
    def add(c, text, tc, x, y, fnt, sz, tn, bp, bg, bo, bw, bc, im, data):
        fig = go.Figure(im)
        rgba_color = f"rgba({int(bg[1:3], 16)}, {int(bg[3:5], 16)}, {int(bg[5:7], 16)}, {bo})"
        data.append({
            'x': validate(x, 0.5),
            'y': validate(y, 0.5),
            'xref': 'paper',
            'yref': 'paper',
            'text': validate(text, ''),
            'showarrow': False,
            'font': {
                'size': validate(int(sz), 15),
                'color': validate(tc, "#000000"),
                'family': validate(fnt, 'Arial')
            },
            'align': 'center',
            'bordercolor': validate(bc, "#000000"),
            'borderwidth': validate(bw, 1),
            'bgcolor': validate(rgba_color, None),
            'textangle': validate(tn, 0),
            'borderpad': validate(bp, 1)
        })
        fig.update_layout(annotations=data)
        options = [{'label': a['text'], 'value': a['text']} for a in data]
        return fig, data, options

    app.clientside_callback(
        """
        function(n_clicks, fig, w, h, frm) {
            if (n_clicks && fig) {
                // Convert the figure to a PNG byte object
                return new Promise(function(resolve, reject) {
                    Plotly.toImage(fig, {format: frm, width:w, height:h})
                        .then(function(imageData) {
                            // Create a data URI for the image
                            var base64Img = "data:image/"+frm+";base64," + imageData.split(',')[1];
                            
                            // Create a download link
                            var downloadLink = document.createElement('a');
                            downloadLink.href = base64Img;
                            downloadLink.download = "ao-meme-gen-img000."+frm;
                            
                            // Trigger download
                            downloadLink.click();
                            
                            resolve();
                        }).catch(function(error) {
                            reject(error);
                        });
                });
            }
        }
        """,
        Output('status', 'children', allow_duplicate=True),
        Input('save-btn', 'n_clicks'),
        State('img-preview', 'figure'),
        State('width', 'value'),
        State('height', 'value'),
        State('formatttt', 'value'),
        prevent_initial_call=True
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

def init_plot():
    image = data.chelsea()
    fig = px.imshow(image)
    fig.update_layout(
    xaxis_visible=False, 
    yaxis_visible=False, 
    showlegend=False,
    dragmode="drawrect")
    return fig


def home():
    return dbc.Row([
        dbc.Col([
            html.H4("Image"),
                    dcc.Upload(
            id="upload-image",
            children=html.Div(
                [html.A("Select an Image")],
                className="text-center border p-3 bg-light",
            ),
            multiple=False,
            style={'cursor':'pointer'}
        ),
            dbc.Spinner([dcc.Graph(
                    id='img-preview',
                    style={"width": "95%","marginTop": "5px"},
                    config=config,
                    figure=init_plot()
            )], type='grow')
        ]),
        dcc.Store(id='text-store',data=[]),
        meme_generation_column()
    ],style={'margin':'10px','alignItems':'row',"border":'2px'}),
