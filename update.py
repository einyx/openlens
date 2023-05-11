import json
import os
import platform
from pathlib import Path

# Read the package.json file
with open('/home/alessio/code/lens/packages/open-lens/package.json', 'r') as file:
    packagejson = json.load(file)

# Update packagejson
packagejson['build']['publish'] = [
    {
        "url": "https://github.com/einyx/releases/download/Latest",
        "provider": "generic",
    }
]

packagejson['build']['win']['artifactName'] = "OpenLens.Setup.${version}.${ext}"

if platform.system() != "Windows":
    # build both x86_64 and arm64 for Linux and Darwin
    packagejson['scripts']['build:app'] = "electron-builder --publish onTag --x64 --arm64"

# Write the updated package.json file
with open('/home/alessio/code/lens/packages/open-lens/package.json', 'w') as file:
    json.dump(packagejson, file, indent=2)

# Read and modify the .npmrc file
npmrc_path = Path('../lens/.npmrc')
npmrc = npmrc_path.read_text()

npmrc = npmrc.replace('disturl "', 'disturl = "')
npmrc = npmrc.replace('target "', 'target = "')
npmrc = npmrc.replace('runtime "', 'runtime = "')

# Write the updated .npmrc file
npmrc_path.write_text(npmrc)
