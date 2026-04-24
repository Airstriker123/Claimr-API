

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}


def allowed_file(filename: str) -> bool:
    return (
        #return true if
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
        #else return false
    )


def validate_file_size(file) -> bool:
    # return true if
    return (
        # return true if
            file.content_length < 10 * 1024 * 1024
            #else return false
    )  # 10MB upload max
