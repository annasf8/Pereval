def get_path_upload_photos(instance, file):
    return f'images/pereval-{instance.pereval.id}/{file}'