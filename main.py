import os
import glob
import datetime
import itertools as it


PRE_PUBLISH_PATH = "./ready-for-publish/"
PUBLISHED_PATH = "./_posts/"


def main() -> None:
    posts_to_publish = [
        filename for filename in
        it.chain(glob.iglob(f"{PRE_PUBLISH_PATH}**.md", recursive=True),
                 glob.iglob(f"{PRE_PUBLISH_PATH}**.markdown", recursive=True))
        if filename.strip(PRE_PUBLISH_PATH)[:10] < datetime.date.today().isoformat()
    ]

    for post_path in posts_to_publish:
        os.replace(post_path, post_path.replace(
            PRE_PUBLISH_PATH, PUBLISHED_PATH))


if __name__ == "__main__":
    main()
