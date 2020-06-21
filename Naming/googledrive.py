from __future__ import print_function

from apiclient import discovery, errors
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient.http import MediaFileUpload

# the scopes
SCOPES = (
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/presentations',
)

# The ID of a sample presentation.
# PRESENTATION_ID = '19rNf2_nKjW7QG8qg7MX_KdI99hqS6glBYnr3uvrJ7mQ'

# access and Permissions
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)

HTTP = creds.authorize(Http())
drive_service = discovery.build('drive', 'v2', http=HTTP)


name = 'form.pdf'
def gupload(name):
    folder_id = '1KRH3uGLCfBHhI54tO1ydhCAKGoJvBlvS'
    file_metadata = {
        'title': name,
        'parents': [{'id': folder_id}]
        }
    media = MediaFileUpload(name,
                        mimetype='image/jpeg',
                        resumable=True)

    file = drive_service.files().insert(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()

    print('File ID: %s' % file.get('id'))
