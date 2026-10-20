"""Portable scaffold checks; actual renderer validation is a separate project check."""
import json, tempfile, unittest, re
from pathlib import Path
from create_starter import create, REQUIRED

class StarterTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.inputs = self.root/'inputs.json'; self.words = self.root/'captions.json'
        config = {}
        for key, name in REQUIRED.items():
            path = self.root/name; path.write_bytes(b'local input fixture')
            config[key] = name
        self.inputs.write_text(json.dumps(config),encoding='utf-8')
        self.words.write_text(json.dumps([{'text':'<idea & evidence>','start':0,'end':.5}]),encoding='utf-8')

    def test_portable_assets_caption_escaping_and_source_offset(self):
        out = create(self.inputs,self.words,self.root/'new project',2.5)
        page = (out/'index.html').read_text(encoding='utf-8')
        self.assertIn('&lt;idea &amp; evidence&gt;',page)
        self.assertEqual(page.count('data-media-start="2.500000"'),2)
        self.assertEqual(page.count('<audio id="draw-'),3)
        self.assertNotIn('SIGNATURE_CAPTIONS',page)
        self.assertNotIn('data-media-start="28.2"',page)
        for asset in re.findall(r'(?:src="|url\(\x27)(assets/[^"\x27]+)',page):
            self.assertTrue((out/asset).is_file(),asset)

    def test_existing_project_is_preserved(self):
        out=self.root/'existing';out.mkdir();sentinel=out/'index.html';sentinel.write_text('keep me')
        with self.assertRaises(ValueError):create(self.inputs,self.words,out)
        self.assertEqual(sentinel.read_text(),'keep me')

    def test_invalid_timing_creates_no_output(self):
        self.words.write_text(json.dumps([{'text':'wrong','start':9.5,'end':10}]))
        out=self.root/'bad'
        with self.assertRaises(ValueError):create(self.inputs,self.words,out)
        self.assertFalse(out.exists())

if __name__=='__main__':unittest.main()
