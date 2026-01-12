def load_filepath_and_text(filename, split = "|"):
    with open(filename, encoding="utf-8") as f:
        file_path_and_text = [line.strip().split(split) for line in f]
    return file_path_and_text

