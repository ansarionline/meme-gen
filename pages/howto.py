import dash_bootstrap_components as dbc
from dash import html
from  dash import dcc
def make_how_to_use():
    return dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("How to Use AO MeMe Gen"), className="mb-4 text-center")
        ]),
        
        dbc.Row([
            dbc.Col(html.P([
                "Creating memes with AO MeMe Gen is simple and easy! Follow the steps below to generate and download your own custom memes."
            ],style={'fontSize':'18px'}))
        ]),

        dbc.Row([
            dbc.Col(html.H2("Step 1: Upload Your Image"), className="mt-4")
        ]),
        
        dbc.Row([
            dbc.Col(html.P([
                "You can upload your own images to create personalized memes. Simply click the 'Upload Image' button and select an image from your device."
            ],style={'fontSize':'18px'}))
        ]),
        
        dbc.Row([
            dbc.Col(html.H2("Step 2: Add Text to Your Meme"), className="mt-4")
        ]),
        
        dbc.Row([
            dbc.Col(html.P([
                "After selecting a template or uploading your image, you can add custom text to your meme. Enter your desired text in the text boxes provided, and adjust the font size, color, and position to fit your needs."
            ],style={'fontSize':'18px'}))
        ]),
        
        dbc.Row([
            dbc.Col(html.H2("Step 3: Customize Your Meme"), className="mt-4")
        ]),
        
        dbc.Row([
            dbc.Col(html.P([
                "You can further customize your meme by adjusting the image and text positioning. Use the tools provided to make your meme exactly how you want it."
            ],style={'fontSize':'18px'}))
        ]),
        
        dbc.Row([
            dbc.Col(html.H2("Step 4: Download Your Meme"), className="mt-4")
        ]),
        
        dbc.Row([
            dbc.Col(html.P([
                "Once you're happy with your meme, click the 'Generate' button to save your meme to your device. You can now share it with friends or on social media!"
            ],style={'fontSize':'18px'}))
        ]),
        
        dbc.Row([
            dbc.Col(html.H2("Need Help?"), className="mt-4")
        ]),
        
        dbc.Row([
            dbc.Col(html.P([
                "If you have any questions or need help using the tool, feel free to reach out to us. We are here to assist you!"
            ],style={'fontSize':'18px'}))
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
                "If you're experiencing any issues or need further instructions, please don't hesitate to contact us."
            ]), className="mt-4 text-center",style={'fontSize':'18px'})
        ]),
    ], className="mt-5")
