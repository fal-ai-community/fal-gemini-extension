import hashlib
import json
import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('bundle_validator', ROOT / 'scripts/validate.py')
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class BundleIntegrity(unittest.TestCase):
    def snapshot(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        destination = Path(temporary.name) / 'bundle'
        shutil.copytree(ROOT, destination, ignore=shutil.ignore_patterns('.git', '__pycache__'))
        return destination

    def test_complete_payload(self):
        skills, files = validator.validate()
        self.assertEqual(skills, 6)
        self.assertGreater(files, skills)

    def test_full_bundle_metadata_is_rejected_even_with_updated_hash(self):
        root = self.snapshot()
        source_path = root / 'skills-source.lock.json'
        source = json.loads(source_path.read_text())
        source['bundle'] = 'full'
        source_path.write_text(json.dumps(source, indent=2) + '\n')
        lock_path = root / 'bundle-source.lock.json'
        lock = json.loads(lock_path.read_text())
        lock['files']['skills-source.lock.json'] = hashlib.sha256(source_path.read_bytes()).hexdigest()
        lock_path.write_text(json.dumps(lock, indent=2) + '\n')
        with self.assertRaisesRegex(ValueError, 'hybrid'):
            validator.validate(root)

    def test_changed_generated_content_is_rejected(self):
        root = self.snapshot()
        with (root / 'GEMINI.md').open('a', encoding='utf-8') as stream:
            stream.write('\nChanged content\n')
        with self.assertRaises(ValueError):
            validator.validate(root)

    def test_unindexed_skill_file_is_rejected(self):
        root = self.snapshot()
        (root / 'skills' / 'unexpected.txt').write_text('Unexpected payload', encoding='utf-8')
        with self.assertRaises(ValueError):
            validator.validate(root)

    def test_missing_skill_asset_is_rejected(self):
        root = self.snapshot()
        (root / 'skills/product-ad-campaign/SKILL.md').unlink()
        with self.assertRaises(ValueError):
            validator.validate(root)


if __name__ == '__main__':
    unittest.main()
