"""Portable setup checks; media playback requires the separate render check."""
import json
from pathlib import Path
import tempfile
import unittest
from create_imessage_starter import create, FILES

class StarterTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        cfg = {'privacy_reviewed': True}
        for key, filename in FILES.items():
            p = self.root / filename
            p.write_bytes(b'local fixture - not playable media')
            cfg[key] = filename
        self.config = self.root / 'inputs.json'
        self.config.write_text(json.dumps(cfg))
        self.captions = self.root / 'captions.json'
        self.captions.write_text(json.dumps([{'text':'<hello>&','start':0,'end':.5}]))
        self.out = self.root / 'project'

    def test_portable_build_and_action_audio(self):
        create(self.config, self.captions, self.out)
        html = (self.out / 'index.html').read_text(encoding='utf-8')
        self.assertIn('&lt;hello&gt;&amp;', html)
        self.assertNotIn(str(self.root), html)
        cues = json.loads((self.out / 'sound-cues.json').read_text())
        targets = {c['visual_target']:c for c in cues}
        self.assertEqual(targets['example-one']['start'], 3.52)
        self.assertEqual(targets['example-two']['start'], 4.56)
        self.assertEqual(targets['buddy-typing']['family'], 'typewriter')
        self.assertEqual(targets['cta-writing']['family'], 'draw')
        self.assertAlmostEqual(targets['text-underline']['end']-targets['text-underline']['start'], .42)
        for item in FILES.values(): self.assertTrue((self.out/'assets'/item).is_file())
        with self.assertRaises(ValueError): create(self.config, self.captions, self.out)

    def test_privacy_attestation_required(self):
        cfg = json.loads(self.config.read_text()); cfg['privacy_reviewed'] = False
        self.config.write_text(json.dumps(cfg))
        with self.assertRaises(ValueError): create(self.config, self.captions, self.out)
        self.assertFalse(self.out.exists())

    def test_caption_overlap_rejected(self):
        self.captions.write_text(json.dumps([{'text':'a','start':0,'end':1},{'text':'b','start':.5,'end':2}]))
        with self.assertRaises(ValueError): create(self.config, self.captions, self.out)

    def test_out_of_range_rejected(self):
        self.captions.write_text(json.dumps([{'text':'a','start':0,'end':46}]))
        with self.assertRaises(ValueError): create(self.config, self.captions, self.out)

if __name__ == '__main__': unittest.main()
