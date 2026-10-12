#!/usr/bin/env python3
"""Looks up the CURRENT Fabric loader / Loom / Fabric API versions for Minecraft 26.3 and writes them into gradle.properties.
Needs internet. Standard library only."""
import json, re, sys, urllib.parse, urllib.request

MC = "26.3"

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "flatverity-build/1.0"})
    return urllib.request.urlopen(req, timeout=30).read().decode()

loader = next(v["version"] for v in json.loads(get("https://meta.fabricmc.net/v2/versions/loader")) if v.get("stable", True))

q = urllib.parse.urlencode({"game_versions": json.dumps([MC]), "loaders": json.dumps(["fabric"])})
versions = json.loads(get("https://api.modrinth.com/v2/project/fabric-api/version?" + q))
if not versions:
    sys.exit("No Fabric API build for Minecraft %s exists yet. Check https://fabricmc.net/develop" % MC)
fabric_api = versions[0]["version_number"]

meta = get("https://maven.fabricmc.net/net/fabricmc/fabric-loom/maven-metadata.xml")
loom = re.search(r"<release>(.*?)</release>", meta).group(1)

text = open("gradle.properties").read()
for key, val in (("loader_version", loader), ("loom_version", loom), ("fabric_version", fabric_api), ("minecraft_version", MC)):
    text = re.sub(r"^%s=.*$" % key, "%s=%s" % (key, val), text, flags=re.M)
open("gradle.properties", "w").write(text)
print("loader", loader, "| loom", loom, "| fabric-api", fabric_api)
