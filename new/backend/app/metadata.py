''' Metadata

Contains metadata details. Typically for developers and not production users.
Descriptions are reflected on the generated Doc page

'''

# The tags for the FastAPI OpenAPI auto documenter
tags_metadata = [
    {
        "name": "Buckets",
        "description": "Operations with Buckets",
    },
    {
        "name": "Events",
        "description": "Operations with Events",
    },
    {
        "name": "Event Bucket Assignment",
        "description": "Operations with Events",
    }
]

swagger_ui_parameters = {
    "syntaxHighlight": True
}

app_title = 'Speny Backend FastAPI'
app_version = '1.1.0'
app_desc = '''
The Spenny Money Tracking backend system
'''
