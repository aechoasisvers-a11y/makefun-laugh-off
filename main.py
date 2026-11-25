import os

LINE = "My smart fridge emailed my doctor about my midnight snacks \u2014 I never knew betrayal could be so cold."


def check(text):
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line, no newlines allowed")
    encoded = text.encode("utf-8")
    if encoded.decode("utf-8") != text:
        raise ValueError("entry is not valid UTF-8 round-trip text")
    return True


def main():
    check(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Verify the written file round-trips exactly: re-read and re-check.
    with open(path, "rb") as f:
        raw = f.read()
    if raw != LINE.encode("utf-8"):
        raise ValueError("written entry.txt does not match the entry line")
    check(raw.decode("utf-8"))


if __name__ == "__main__":
    main()
