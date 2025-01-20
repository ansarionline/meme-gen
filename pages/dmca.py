from dash import html
import dash_bootstrap_components as dbc

def make_dmca():
    return dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("DMCA Policy"), width=12),
        ], className="mt-5"),
        
        dbc.Row([
            dbc.Col(html.P("At AO MeMe Gen, accessible from https://aomultiverse.com, we respect the intellectual property rights of others. It is our policy to respond to any claim that content posted on our website infringes on the copyright or other intellectual property rights of any person or entity."), width=12),
        ], className="mb-4"),

        dbc.Row([
            dbc.Col(html.H2("Reporting Copyright Infringements"), width=12),
        ], className="mt-4"),

        dbc.Row([
            dbc.Col(html.P("If you believe that material available on our site infringes your copyright, please notify us by providing the following information:"), width=12),
        ], className="mb-3"),

        dbc.Row([
            dbc.Col(dbc.ListGroup([
                dbc.ListGroupItem("A physical or electronic signature of the copyright owner or a person authorized to act on their behalf."),
                dbc.ListGroupItem("Identification of the copyrighted work claimed to have been infringed."),
                dbc.ListGroupItem("Identification of the material that is claimed to be infringing and where it is located on the website."),
                dbc.ListGroupItem("Your contact information, including your address, telephone number, and email address."),
                dbc.ListGroupItem("A statement that you have a good faith belief that the use of the material in the manner complained of is not authorized by the copyright owner, its agent, or the law."),
                dbc.ListGroupItem("A statement that the information in the notification is accurate, and under penalty of perjury, that you are authorized to act on behalf of the copyright owner."),
            ]), width=12),
        ], className="mb-4"),

        dbc.Row([
            dbc.Col(html.P("You can submit your DMCA notice to our designated agent via email or phone:"), width=12),
        ], className="mb-3"),

        dbc.Row([
            dbc.Col(dbc.ListGroup([
                dbc.ListGroupItem("Email: info@aomultiverse.com"),
                dbc.ListGroupItem("Phone: +92 334 3324444"),
            ]), width=12),
        ], className="mb-4"),

        dbc.Row([
            dbc.Col(html.P("Upon receipt of a valid DMCA notice, we will take appropriate actions, including removing the reported content from our website."), width=12),
        ], className="mb-4"),

        dbc.Row([
            dbc.Col(html.H2("Counter-Notification"), width=12),
        ], className="mt-4"),

        dbc.Row([
            dbc.Col(html.P("If you believe that your content was removed or disabled by mistake or misidentification, you may submit a counter-notification by providing the following information:"), width=12),
        ], className="mb-3"),

        dbc.Row([
            dbc.Col(dbc.ListGroup([
                dbc.ListGroupItem("Your physical or electronic signature."),
                dbc.ListGroupItem("Identification of the material that has been removed or to which access has been disabled and the location at which the material appeared before it was removed or disabled."),
                dbc.ListGroupItem("A statement under penalty of perjury that you have a good faith belief that the material was removed or disabled as a result of mistake or misidentification."),
                dbc.ListGroupItem("Your name, address, telephone number, and email address, and a statement that you consent to the jurisdiction of the federal court in your jurisdiction."),
            ]), width=12),
        ], className="mb-4"),

        dbc.Row([
            dbc.Col(html.P("You can submit your counter-notification to our designated agent via email or phone:"), width=12),
        ], className="mb-3"),

        dbc.Row([
            dbc.Col(dbc.ListGroup([
                dbc.ListGroupItem("Email: info@aomultiverse.com"),
                dbc.ListGroupItem("Phone: +92 334 3324444"),
            ]), width=12),
        ], className="mb-4"),

        dbc.Row([
            dbc.Col(html.P("Please note that under Section 512(f) of the DMCA, any person who knowingly materially misrepresents that material or activity was removed or disabled by mistake or misidentification may be subject to liability."), width=12),
        ], className="mb-4"),

        dbc.Row([
            dbc.Col(html.H2("Repeat Infringers"), width=12),
        ], className="mt-4"),

        dbc.Row([
            dbc.Col(html.P("We will terminate the accounts of users who are found to be repeat infringers."), width=12),
        ], className="mb-4"),
    ], className="mt-5")
