#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys
import urllib.request

SOURCE_URL = "https://raw.githubusercontent.com/qwerttvv/Beijing-IPTV/master/IPTV-Unicom-Multicast.m3u"
UNICAST_BASE = "http://192.168.100.1:9999/rtp/"


def fetch_source(url: str) -> str:
    with urllib.request.urlopen(url) as resp:
        return resp.read().decode("utf-8", errors="ignore")


def convert_multicast_to_unicast(m3u_text: str) -> str:
    def repl(match: re.Match) -> str:
        multicast = match.group(1)
        return f"{UNICAST_BASE}{multicast}"

    pattern = re.compile(r"(?:rtp|udp)://([\d.]+:\d+)")
    return pattern.sub(repl, m3u_text)


def main() -> None:
    raw = fetch_source(SOURCE_URL)
    converted = convert_multicast_to_unicast(raw)
    sys.stdout.write(converted)


if __name__ == "__main__":
    main()
