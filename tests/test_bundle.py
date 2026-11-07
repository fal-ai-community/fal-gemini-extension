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
        self.assertEqual(skills, 36)
        self.assertGreater(files, skills)

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
        (root / 'skills/product-ad-campaign/assets/plan.json').unlink()
        with self.assertRaises(ValueError):
            validator.validate(root)


if __name__ == '__main__':
    unittest.main()
