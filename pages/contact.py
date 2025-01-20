import dash_bootstrap_components as dbc
from dash import html
from  dash import dcc

def make_contact_us():
    return dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Contact Us"), className="mb-4 text-center")
        ]),
        
        dbc.Row([
            dbc.Col(html.P([
                "We’d love to hear from you! Whether you have questions, feedback, or suggestions, feel free to reach out to us using the contact information below or by filling out the form."
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
                "We aim to respond to all inquiries within 24-48 hours. Thank you for reaching out to AO MeMe Gen!"
            ]), className="mt-4 text-center")
        ]),
    ], className="mt-5")
