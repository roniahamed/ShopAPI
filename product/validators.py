from django.core.exceptions import ValidationError 
from django.template.defaultfilters import filesizeformat
import magic


def validate_file_size(value):

    limit = 2 * 1024 * 1024

    if value.size > limit:
        raise ValidationError(f"File size can't exceed { filesizeformat(limit)}. Current file size is {filesizeformat(value.size)}.")

def validate_file_mimetype(file):

    allowed_mime_types = ['image/jpeg', 'image/png', 'application/pdf']

    mime_type = magic.from_buffer(file.read(2048), mime=True)

    file.seek(0)

    file.seek(0)

    if mime_type not in allowed_mime_types:
        raise ValidationError(f"Unsupported file type:'{mime_type}'. Allowed types are JPEG, PNG, PDF.")
    
    