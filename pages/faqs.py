import dash_bootstrap_components as dbc
from dash import html
from  dash import dcc

def make_faqs():
    return dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Frequently Asked Questions (FAQs)"), className="mb-4 text-center")
        ]),
        
        dbc.Row([
            dbc.Col(html.P([
                "Find answers to common questions about AO MeMe Gen below. ",
                "If you have any additional questions, feel free to reach out to us."
            ]))
        ]),
        
        dbc.Row([
            dbc.Col(html.H2("General Questions"), className="mt-4")
        ]),
        
        dbc.Accordion([
            dbc.AccordionItem([
                html.P("AO MeMe Gen is an online meme generator that allows users to create memes in a simple, easy, broad, and wide-ranging way."),
            ], title="What is AO MeMe Gen?"),

            dbc.AccordionItem([
                html.P([
                    "No, you don't need to create an account to generate memes. AO MeMe Gen is free to use without any registration requirements."
                ]),
            ], title="Do I need to create an account to generate memes?"),

            dbc.AccordionItem([
                html.P("Yes, you can upload your own images and add text to create custom memes."),
            ], title="Can I upload my own images?"),

            dbc.AccordionItem([
                html.P("No, we do not store any of your uploaded images. All content is processed on the client-side, and you are responsible for your uploaded content."),
            ], title="Do you store the images I upload?"),
        ], start_collapsed=True),
        
        dbc.Row([
            dbc.Col(html.H2("Usage Questions"), className="mt-4")
        ]),
        
        dbc.Accordion([
            dbc.AccordionItem([
                html.P("You can create memes by selecting a template, adding text, and downloading the final image."),
            ], title="How do I create a meme?"),

            dbc.AccordionItem([
                html.P("Yes, once you create a meme, you can download it to your device with a single click."),
            ], title="Can I download my memes?"),

            dbc.AccordionItem([
                html.P("Yes, AO MeMe Gen is completely free to use. However, ads may be displayed to support the platform."),
            ], title="Is AO MeMe Gen free to use?"),
        ], start_collapsed=True),
        
        dbc.Row([
            dbc.Col(html.H2("Technical Support"), className="mt-4")
        ]),

        dbc.Accordion([
            dbc.AccordionItem([
                html.P("If you encounter issues, try refreshing the page or clearing your browser cache. For further assistance, contact us."),
            ], title="What should I do if I encounter an issue?"),

            dbc.AccordionItem([
                html.P("For any questions or support inquiries, feel free to contact us via email or phone."),
            ], title="How can I contact support?"),
        ], start_collapsed=True),
        
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
                "If you don't find the answer to your question here, please feel free to reach out to us via the provided contact details."
            ]), className="mt-4 text-center")
        ]),
    ], className="mt-5")
