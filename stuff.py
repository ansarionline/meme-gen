import dash_bootstrap_components as dbc
from dash import html,Output,Input,State,no_update
import plotly.graph_objects as go

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
        Output(modal, "is_open"),
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
                    dbc.Input(type="text", id="meme-text", placeholder="Enter text", className="mb-2"),
                    dbc.InputGroup([
                        dbc.Input('text-x', placeholder='Horizontal Pos (0-1)', type='number', min=0, max=1),
                        dbc.Input('text-y', placeholder='Vertical Pos (0-1)', type='number', min=0, max=1),
                        dbc.Input('text-angle', placeholder='Angle (0-180)', type='number', min=0, max=180)
                    ]),
                    dbc.InputGroup([
                        dbc.Select(id='text-font', placeholder='Font', options=fonts),
                        dbc.Input(id='text-size', placeholder='Size', value=15, type='number', min=5, step=1),
                        dbc.Input(type="color", id="text-color", value="#000000", className="mb-2", placeholder="Text Color", style={"height": '40px'})
                    ])
                ]
            ),
            html.H4("Background", className="mb-4"),
            dbc.Form([
                dbc.InputGroup([dbc.Input(type="number", id="border-pad", value="1", className="mb-2", placeholder="Area", style={"height": '40px'}),
                                dbc.Input(type="color", id="border-bg", value="#FFFFFF", className="mb-2", placeholder="Border Bg", style={"height": '40px'})]),
                dbc.InputGroup([dbc.Input(type="number", id="border-width", placeholder="Border Width", className="mb-2", value=0),
                                dbc.Input(type="color", id="border-color", value="#FFFFFF", className="mb-2", placeholder="Border Color", style={"height": '40px'})]),
                dbc.Button("Add Text", id="add-text-btn", color="primary", style={'margin': '5px'})
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
                    dbc.Label('Done!!!\nClick the `Save` to save or `Copy link` button to copy the Meme address.'),
                    dbc.Label('',id='status'),
                    dbc.ButtonGroup([
                        dbc.Button("Save", id="save-btn", color="success"),
                        dbc.Button("Copy Link", id="copy-btn", color="info")
                    ])
                ])
            ], id='dialog')
        ]
    )

# Validate value
def validate(value, els):
    return value if value is not None and len(str(value)) > 0 else els

# Register the callback
def register_meme_generation_column(app):
    open_d(app, 'dialog', 'gen-btn')

    @app.callback(
        Input('gen-btn','n_clicks'),
        State('img-preview', 'figure')
    )
    def do_export(n,fig):
        fig = go.Figure(fig)
        fig.to_image(format='png')
        return

    @app.callback(
        [Output('img-preview', 'figure', allow_duplicate=True),
        Output('text-store', 'data', allow_duplicate=True)],
        [Input('add-text-btn', 'n_clicks')],
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
            State('border-width', 'value'),
            State('border-color', 'value'),
            State('img-preview', 'figure'),
            State('text-store', 'data')
        ]
    )
    def add(c, text, tc, x, y, fnt, sz, tn, bp, bg, bw, bc, im, data):
        fig = go.Figure(im)
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
            'bgcolor': validate(bg, '#ffffff'),
            'textangle': validate(tn, 0),
            'borderpad': validate(x, 1)
        })
        fig.update_layout(annotations=data)
        return fig, data

    # JavaScript callback to handle save and copy functionalities
    app.clientside_callback(
        """
        function(n_clicks, fig, w, h, formatttt) {
            if (n_clicks && fig) {
                // Use Plotly's toImage method to export the figure as the selected format
                return new Promise(function(resolve, reject) {
                    Plotly.toImage(fig, {format: formatttt, width: w, height: h})
                        .then(function(imageData) {
                            // Convert the image to Base64
                            var base64Img = "data:image/" + formatttt + ";base64," + imageData.split(',')[1];
                            
                            // Copy the Base64 image link to the clipboard
                            navigator.clipboard.writeText(base64Img).then(function() {
                                alert("Image link copied to clipboard!");
                            }).catch(function(error) {
                                alert("Failed to copy: " + error);
                            });
                            resolve();
                        }).catch(function(error) {
                            reject(error);
                        });
                });
            }
        }
        """,
        Output('dialog', 'is_open', allow_duplicate=True),
        Input('copy-btn', 'n_clicks'),
        State('img-preview', 'figure'),
        State('width', 'value'),
        State('height', 'value'),
        State('formatttt', 'value')
    )
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
        Output('status', 'children'),
        Input('save-btn', 'n_clicks'),
        State('img-preview', 'figure'),
        State('width', 'value'),
        State('height', 'value'),
        State('formatttt', 'value'),
        prevent_initial_call=True
    )