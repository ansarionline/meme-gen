import dash_bootstrap_components as dbc
from dash import html
from  dash import dcc

def make_about():
    return dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("About AO MeMe Gen"), className="mb-4")
        ]),
        
        dbc.Row([
            dbc.Col(html.P([
                "Welcome to ",
                html.A("AO MeMe Gen", href="https://aomultiverse.com", target="_blank"),
                ", a meme generator tool created by Ansari Codes. ",
                "Our mission is to make meme creation simple, easy, and accessible to everyone. Whether you're creating memes for fun or for sharing across the web, AO MeMe Gen provides a broad and flexible platform for your needs."
            ]))
        ]),
        
        dbc.Row([
            dbc.Col(html.H2("Our Purpose"), className="mt-4")
        ]),
        
        dbc.Row([
            dbc.Col(html.P([
                "At AO MeMe Gen, our purpose is to generate memes in a way that's not only simple but also broad and wide-ranging. ",
                "We aim to empower creativity and help users express their ideas effortlessly through memes."
            ]))
        ]),
        
        dbc.Row([
            dbc.Col(html.H2("Contact Information"), className="mt-4")
        ]),
        
        dbc.Row([
            dbc.Col(dbc.ListGroup([
                dbc.ListGroupItem(["Email: ", html.A("info@aomultiverse.com", href="mailto:info@aomultiverse.com")]),
                dbc.ListGroupItem("Phone: +92 334 3324444"),
                dbc.ListGroupItem(["Website: ", html.A("aomultiverse.com", href="https://aomultiverse.com", target="_blank")]),
            ]))
        ]),
        
        dbc.Row([
            dbc.Col(html.P([
                "Feel free to reach out if you have any questions, suggestions, or feedback. We're here to assist you and make your meme creation journey enjoyable and productive."
            ]), className="mt-4")
        ]),
    ], className="mt-5")
