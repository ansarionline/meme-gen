import dash_bootstrap_components as dbc
from dash import html
from  dash import dcc

def make_privacy_policy():
    return dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Privacy Policy"), className="mb-4")
        ]),
        
        dbc.Row([
            dbc.Col(html.P([
                "Welcome to AO MeMe Gen, accessible from ",
                html.A("aomultiverse.com", href="https://aomultiverse.com", target="_blank"),
                ". Your privacy is important to us. This Privacy Policy outlines how we collect, use, and protect your information when you use our website."
            ]))
        ]),
        
        dbc.Row([
            dbc.Col(html.H2("Information We Collect"), className="mt-4")
        ]),
        
        dbc.Row([
            dbc.Col(html.P([
                "We do not collect any personal data unless explicitly provided by you, such as when contacting us via email or phone. ",
                "AO MeMe Gen does not track your activities beyond the necessary operational functionality of the site."
            ]))
        ]),
        
        dbc.Row([
            dbc.Col(html.H2("User Uploaded Content"), className="mt-4")
        ]),
        
        dbc.Row([
            dbc.Col(html.P([
                "Any images or content you upload to AO MeMe Gen are processed solely for meme creation purposes. ",
                "We do not view, track, or store your uploaded content. All uploaded files remain under your control, and their use is entirely your responsibility."
            ]))
        ]),
        
        dbc.Row([
            dbc.Col(html.H2("User Responsibility"), className="mt-4")
        ]),
        
        dbc.Row([
            dbc.Col(html.P([
                "You are solely responsible for the content you create and upload on AO MeMe Gen. ",
                "We do not monitor or review any content, and we disclaim any responsibility for content misuse or violations of third-party rights."
            ]))
        ]),
        
        dbc.Row([
            dbc.Col(html.H2("Third-Party Services"), className="mt-4")
        ]),
        
        dbc.Row([
            dbc.Col(html.P([
                "Our website may contain links to third-party services, such as advertisements through Google AdSense. ",
                "These third parties may collect data as per their privacy policies. We recommend reviewing their policies before engaging with their services."
            ]))
        ]),
        
        dbc.Row([
            dbc.Col(html.H2("Cookies"), className="mt-4")
        ]),
        
        dbc.Row([
            dbc.Col(html.P([
                "We may use cookies to improve your browsing experience. Cookies help us understand user behavior and enhance the site's functionality, but they do not personally identify you."
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
                "If you have any questions about our Privacy Policy, please feel free to contact us."
            ]), className="mt-4")
        ]),
        
        dbc.Row([
            dbc.Col(html.P([
                "This Privacy Policy was created to comply with advertising and data protection requirements, including those set by Google AdSense."
            ]), className="mt-4 text-muted")
        ]),
    ], className="mt-5")
