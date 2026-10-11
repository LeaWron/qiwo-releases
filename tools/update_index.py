"""Publish stable metadata and opt-in Android previews without client REST calls."""
import json
from pathlib import Path
import subprocess


def build_index(pages):
    releases = []
    seen = set()
    for page in pages:
        for release in page:
            if release.get('draft'):
                continue
            if release.get('prerelease') and not release['tag_name'].startswith(('android-v', 'companion-android-v')):
                continue
            tag = release['tag_name']
            if tag in seen:
                raise ValueError('duplicate release tag: ' + tag)
            seen.add(tag)
            releases.append({key: release[key] for key in ('tag_name', 'html_url', 'draft', 'prerelease')} | {
                'assets': [{key: asset.get(key) for key in ('name', 'size', 'digest', 'browser_download_url')}
                           for asset in release['assets']]
            })
    return {'schema': 1, 'releases': releases}


if __name__ == '__main__':
    pages = json.loads(subprocess.check_output([
        'gh', 'api', '--paginate', '--slurp',
        'repos/LeaWron/qiwo-releases/releases?per_page=100',
    ]))
    data = json.dumps(build_index(pages), ensure_ascii=False, indent=2) + '\n'
    if len(data.encode()) > 1024 * 1024:
        raise ValueError('index exceeds assistant metadata limit')
    destination = Path('updates/releases.json')
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(data, encoding='utf-8')
