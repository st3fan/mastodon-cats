# mastodon-cats
_Stefan Arentz, April 2022_

Small program to post a daily (cat) photo to Mastodon. I schedule it with cron:

```
0 6 * * * /home/stefan/automation/mastodon-cats/mastodon-cats.sh
```

Change `MASTODON_ACCESS_KEY` in `mastodon-cats.sh`. You can set this up in the _Developer_ section in your Mastodon settings.

Needs [Mastodon.py](https://github.com/halcy/Mastodon.py). I run this from a _virtual env_ like:

```
$ cd mastodon-cats
$ python3 -m venv .env
$ source .env/bin/activate
(.env) $ pip install Mastodon.py
```

Drop images in `images-queued`. The program will pick one up randomly and then it moves to `images-failed` or `images-tooted` after posting.

