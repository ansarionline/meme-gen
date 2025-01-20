from dash import Dash, dcc, html, Input, Output, no_update
from skimage import io as skio
import numpy as np
import plotly.express as px
import dash_bootstrap_components as dbc
import pages.home as home
import pages.about as about
import pages.dmca as dmca
import pages.privacy as privacy
import pages.terms as terms
import pages.contact as contact
import pages.faqs as faqs
import pages.howto as howto
import base64
import io

app = Dash(__name__,
            external_stylesheets=[dbc.themes.BOOTSTRAP],
            meta_tags=[
            {"name": "viewport", 
                "content": "width=device-width,initial-scale=1,maximum-scale=1.5,minimum-scale=0.5"},
            {"name": "google-adsense-account", "content": "ca-pub-6076513831764218"}
            ],
            prevent_initial_callbacks=True,
            suppress_callback_exceptions=True
            )
app.title = 'AO MeMe Gen'
server = app.server
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/")),
        dbc.NavItem(dbc.NavLink("About", href="/about")),
        dbc.NavItem(dbc.NavLink("DMCA", href="/dmca")),
        dbc.NavItem(dbc.NavLink("Privacy", href="/privacy-policy")),
        dbc.NavItem(dbc.NavLink("Terms", href="/terms-of-service")),
        dbc.NavItem(dbc.NavLink("Contact", href="/contact")),
        dbc.NavItem(dbc.NavLink("FAQs", href="/faqs")),
        dbc.NavItem(dbc.NavLink("Guide", href="/how-to")),
    ],
brand=dbc.InputGroup([
    dbc.Row(
        [
            dbc.Col(
                html.Img(src='assets/favicon.webp',
                        style={'width': '50px', 'height': '50px', "margin": '5px', 'border-radius': '15px'}),
                width="auto", 
                align="center"
            ),
            dbc.Col(
                html.Div(
                    [
                        html.H4('AO MeMe Generator', style={"margin": '5px', 'textAlign': 'left', "position": "relative"}),
                        html.Div('Pro.', style={
                            "position": "absolute", 
                            "top": "-10px", 
                            "right": "0", 
                            "font-size": "18px",  # Adjust the font size if needed
                            "font-weight": "bold"
                        }),
                    ]
                ),
                width="auto",  # Ensures the text doesn't stretch
                align="center"  # Aligns the text vertically with the image
            ),
        ],
        align="center"
    ),
],
style={'backgroundColor': '#eeeeee'}),
    color="#eeeeee",
    className="mb-2", style={'width':'100%'}
)

app.layout = html.Div(dcc.Loading([
    dcc.Location(id="url", refresh=False),
    navbar,
    html.Div(id="page-content"),
    html.Footer(
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(navbar, width=12),  
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(html.P("© 2025 AO MeMe Gen | Created by Ansari Codes"), className="text-center", width=12),
                    ],
                    className="mb-3", 
                ),
            ],
            fluid=True, 
        ),
        style={"background-color": "#f8f9fa", "padding": "10px 0", "margin-top": "20px"})],
        fullscreen=True,type='circle',style={'size':'200px'},color='black'))

home.register_meme_generation_column(app)
@app.callback(
    [Output("img-preview", "figure",allow_duplicate=True),
    Output('text-store','data',allow_duplicate=True)],
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
        return fig,[]
    except Exception as e:
        print(e)
        return no_update,[]

@app.callback(
    Output("page-content", "children", allow_duplicate=True),
    Input("url", "pathname"),
)
def display_page(pathname):
    if pathname == "/about":
        return about.make_about()
    if pathname == "/dmca":
        return dmca.make_dmca()
    if pathname == "/privacy-policy":
        return privacy.make_privacy_policy()
    if pathname == "/terms-of-service":
        return terms.make_terms_of_service()
    if pathname == "/contact":
        return contact.make_contact_us()
    if pathname == "/faqs":
        return faqs.make_faqs()
    if pathname == "/how-to":
        return howto.make_how_to_use()
    else:
        return home.home()
if __name__ == '__main__':
    app.run(debug=False,use_reloader=False)
