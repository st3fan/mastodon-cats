#!/bin/sh

export MASTODON_ACCESS_TOKEN="REPLACE_ME_WITH_YOUR_ACCESS_TOKEN"
export MASTODON_API_BASE_URL="https://mastodon.social"

cd "$(dirname "$0")"
.env/bin/python mastodon-cats.py
