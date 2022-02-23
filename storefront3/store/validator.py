
from django.core.exceptions import ValidationError


def validate_file_size(file):
    max_size_mb = 10

    if file.size > max_size_mb * 1024:
        raise ValidationError(
            f'File cannot be uploaded because file must be below{max_size_mb}MB')
