#!/usr/bin/env bash
# Builds a signed release AAB and verifies it is uploadable.
# Does NOT upload - that is a manual Play Console step.
#
# Requires keystore.properties and the .jks beside it, both at this directory.
# If they are missing the build fails at configuration time, before any task runs.
set -euo pipefail

export JAVA_HOME="$(/usr/libexec/java_home -v 17)"
cd "$(dirname "$0")"

echo "==> Building signed release AAB"
./gradlew clean bundleRelease

AAB="app/build/outputs/bundle/release/app-release.aab"

echo "==> Checking artifact"
[ -f "$AAB" ] || { echo "FAIL: $AAB not found"; exit 1; }

echo "==> Checking signature"
keytool -printcert -jarfile "$AAB" > /dev/null || { echo "FAIL: AAB is not signed"; exit 1; }

echo "==> Checking version"
python3 - <<'PY'
import json, glob
found = []
for p in glob.glob('app/build/**/output-metadata.json', recursive=True):
    d = json.load(open(p))
    if d['elements'] and 'versionCode' in d['elements'][0]:
        el = d['elements'][0]
        found.append((d['artifactType']['type'], el.get('versionCode'), el.get('versionName')))
if not found:
    raise SystemExit("FAIL: no versioned output-metadata.json - did the build run?")
codes = {(c, n) for _, c, n in found}
if len(codes) != 1:
    raise SystemExit(f"FAIL: artifacts disagree on version: {found}")
code, name = codes.pop()
print(f"    versionCode={code} versionName={name}  (agreed across {len(found)} artifacts)")
PY

echo
echo "OK - upload this file: $AAB"
