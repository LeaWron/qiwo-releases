import unittest
from update_index import build_index


class UpdateIndexTests(unittest.TestCase):
    def release(self, **changes):
        return dict(tag_name='companion-v0.1.14', html_url='https://github.com/LeaWron/qiwo-releases/releases/tag/companion-v0.1.14',
                    draft=False, prerelease=False,
                    assets=[dict(name='manifest.json', size=42, digest='sha256:' + 'a' * 64,
                                 browser_download_url='https://github.com/LeaWron/qiwo-releases/releases/download/tag/manifest.json')],
                    **changes)

    def test_preserves_download_integrity_metadata(self):
        source = self.release()
        output = build_index([[source]])
        self.assertEqual(output['schema'], 1)
        self.assertEqual(output['releases'][0]['assets'], source['assets'])

    def test_excludes_draft_and_preview_even_with_same_tag(self):
        stable = self.release()
        draft = dict(stable, draft=True)
        preview = dict(stable, prerelease=True)
        self.assertEqual(build_index([[draft, preview], [stable]])['releases'], [stable])

    def test_duplicate_public_tags_are_rejected(self):
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            build_index([[self.release()], [self.release()]])

    def test_android_previews_are_indexed_with_channel_flag_and_integrity(self):
        preview = dict(self.release(), tag_name='android-v0.2.9-rc1', prerelease=True)
        self.assertEqual(build_index([[preview]])['releases'], [preview])
        self.assertEqual(build_index([[dict(preview, draft=True)]])['releases'], [])


    def test_android_assistant_plugin_previews_are_indexed_separately(self):
        preview = dict(self.release(), tag_name='companion-android-v0.1.18-rc1', prerelease=True)
        self.assertEqual(build_index([[preview]])['releases'], [preview])
        self.assertEqual(build_index([[dict(preview, draft=True)]])['releases'], [])


if __name__ == '__main__':
    unittest.main()
