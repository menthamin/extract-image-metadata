import PIL.Image


def get_image_metadata(image_obj):

    metadata = image_obj._getexif()

    company = metadata[271]
    model = metadata[272]
    time_stamp = metadata[36868]
    time_stamp_offset = metadata[36881]
    gps_info = metadata[34853]

    return [company, model, time_stamp, time_stamp_offset, gps_info]
