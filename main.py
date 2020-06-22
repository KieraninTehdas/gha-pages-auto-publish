import os
import glob
import datetime
import itertools as it


PRE_PUBLISH_PATH = "./ready-for-publish/"
PUBLISHED_PATH = "./_posts/"


def main() -> int:
    posts_to_publish = [
        filename for filename in
        it.chain(glob.iglob(f"{PRE_PUBLISH_PATH}**.md", recursive=True),
                 glob.iglob(f"{PRE_PUBLISH_PATH}**.markdown", recursive=True))
        if filename.strip(PRE_PUBLISH_PATH)[:10] < datetime.date.today().isoformat()
    ]

    if not posts_to_publish:
        print("No unpublished posts - exiting")
        print("::set-output name=publishedPosts::0")
        return 0

    for post_path in posts_to_publish:
        os.replace(post_path, post_path.replace(
            PRE_PUBLISH_PATH, PUBLISHED_PATH))

    num_published_posts = len(posts_to_publish)

    print(f"Moved {num_published_posts} to _posts")
    print(f"::set-output name=publishedPosts::{num_published_posts}")
    return num_published_posts


if __name__ == "__main__":
    main()
