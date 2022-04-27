# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/


import glob
import os
import random
import shutil

from typing import Optional

from mastodon import Mastodon


def pick_cat() -> Optional[str]:
    images_queued = glob.glob("images-queued/*.jpeg")
    image_path = random.choice(images_queued)
    return image_path.split("/")[1]


def toot_cat():
    mastodon = Mastodon(access_token=os.getenv("MASTODON_ACCESS_TOKEN"), api_base_url=os.getenv("MASTODON_API_BASE_URL"))
    if image_name := pick_cat():
        try:
            media = mastodon.media_post(f"images-queued/{image_name}")
            mastodon.status_post(status="", sensitive=False, media_ids = [media.id])
            shutil.move(f"images-queued/{image_name}", f"images-tooted/{image_name}")
        except Exception as e:
            shutil.move(f"images-queued/{image_name}", f"images-failed/{image_name}")
            raise


if __name__ == "__main__":
    toot_cat()
