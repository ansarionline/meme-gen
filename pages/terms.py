import dash_bootstrap_components as dbc
from dash import html
from  dash import dcc

def make_terms_of_service():
    return dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Terms of Service"), className="mb-4")
        ]),
        
        dbc.Row([
            dbc.Col(html.P([
                "Welcome to AO MeMe Gen, accessible from ",
                html.A("aomultiverse.com", href="https://aomultiverse.com", target="_blank"),
                ". By accessing or using our website, you agree to comply with and be bound by the following terms and conditions."
            ]))
        ]),
        
        dbc.Row([
            dbc.Col(html.H2("Acceptance of Terms"), className="mt-4")
        ]),
        
        dbc.Row([
            dbc.Col(html.P([
                "By accessing and using AO MeMe Gen, you acknowledge that you have read, understood, and agree to be bound by these Terms of Service. ",
                "If you do not agree with any part of these terms, you may not use our services."
            ]))
        ]),
        
        dbc.Row([
            dbc.Col(html.H2("User Responsibilities"), className="mt-4")
        ]),
        
        dbc.Row([
            dbc.Col(dbc.ListGroup([
                dbc.ListGroupItem("You agree to use AO MeMe Gen only for lawful purposes."),
                dbc.ListGroupItem("You are solely responsible for any content you create, upload, or share on our website."),
                dbc.ListGroupItem("You must not use the website to distribute harmful, offensive, or illegal content."),
                dbc.ListGroupItem("You must not attempt to disrupt the website's functionality or security."),
            ]))
        ]),
        
        dbc.Row([
            dbc.Col(html.H2("Intellectual Property"), className="mt-4")
        ]),
        
        dbc.Row([
            dbc.Col(html.P([
                "All content available on AO MeMe Gen, including logos, text, and graphics, is the property of AO MeMe Gen and is protected by copyright laws. ",
                "You may not reproduce, distribute, or create derivative works without our prior written consent."
            ]))
        ]),
        
        dbc.Row([
            dbc.Col(html.H2("Uploaded Content"), className="mt-4")
        ]),
        
        dbc.Row([
            dbc.Col(html.P([
                "You retain ownership of any images or content you upload to AO MeMe Gen. ",
                "However, by uploading content, you grant us a limited license to use it solely for the purpose of generating memes. ",
                "We do not monitor or track your uploaded content, and you are responsible for ensuring it does not infringe on third-party rights."
            ]))
        ]),
        
        dbc.Row([
            dbc.Col(html.H2("Limitations of Liability"), className="mt-4")
        ]),
        
        dbc.Row([
            dbc.Col(html.P([
                "AO MeMe Gen provides its services on an 'as-is' basis and makes no guarantees regarding availability, accuracy, or reliability. ",
                "We are not liable for any damages or losses resulting from your use of the website."
            ]))
        ]),
        
        dbc.Row([
            dbc.Col(html.H2("Termination of Use"), className="mt-4")
        ]),
        
        dbc.Row([
            dbc.Col(html.P([
                "We reserve the right to suspend or terminate your access to AO MeMe Gen at any time, without notice, if you violate these terms or engage in harmful activities."
            ]))
        ]),
        
        dbc.Row([
            dbc.Col(html.H2("Governing Law"), className="mt-4")
        ]),
        
        dbc.Row([
            dbc.Col(html.P([
                "These Terms of Service shall be governed and interpreted in accordance with the laws of your jurisdiction, without regard to its conflict of law provisions."
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
                "If you have any questions or concerns regarding these terms, please contact us."
            ]), className="mt-4")
        ]),
        
        dbc.Row([
            dbc.Col(html.P([
                "These terms are effective as of the latest update and are subject to change without notice."
            ]), className="mt-4 text-muted")
        ]),
    ], className="mt-5")
