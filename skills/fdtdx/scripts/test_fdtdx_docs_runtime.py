"""Hermetic CLI checks: no FDTDX, JAX, network, or solver is required."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


class RuntimeLookupTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.script = self.root / 'scripts/fdtdx_docs.py'
        self.script.parent.mkdir()
        shutil.copyfile(Path(__file__).with_name('fdtdx_docs.py'), self.script)
        corpus = self.root / 'doc'
        corpus.mkdir()
        (corpus / 'api-index.json').write_text(json.dumps({
            'metadata': {'commit': 'snapshot-only'},
            'entries': [{'name': 'SimulationConfig', 'qualified_name': 'fdtdx.SimulationConfig',
                         'signature': '(snapshot_argument)', 'kind': 'class'}]
        }), encoding='utf-8')
        self.package = self.script.parent / 'fdtdx.py'

    def run_cli(self, *args):
        return subprocess.run([sys.executable, '-S', '-B', str(self.script), 'api', *args],
                              capture_output=True, text=True, encoding='utf-8', timeout=15)

    def test_two_runtime_signatures_and_member(self):
        for argument in ('grid', 'resolution'):
            self.package.write_text(f'''__version__ = "test-{argument}"
class SimulationConfig:
    def __init__(self, *, {argument}):
        raise RuntimeError("must not instantiate")
    def place(self, *, offset):
        raise RuntimeError("must not call")
''', encoding='utf-8')
            result = self.run_cli('SimulationConfig', '--source', 'installed')
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn(f'(*, {argument})', result.stdout)
            self.assertIn(str(self.package), json.loads(result.stdout.splitlines()[0])['module_path'])
            self.assertNotIn('snapshot_argument', result.stdout)
        result = self.run_cli('SimulationConfig', '--member', 'place', '--source', 'installed')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('(self, *, offset)', result.stdout)

    def test_snapshot_does_not_import_broken_runtime(self):
        self.package.write_text('raise RuntimeError("broken installation")', encoding='utf-8')
        for suffix in ((), ('--source', 'snapshot')):
            result = self.run_cli('SimulationConfig', *suffix)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout.splitlines()[0])['source'], 'snapshot')
            self.assertIn('snapshot_argument', result.stdout)
        result = self.run_cli('SimulationConfig', '--source', 'installed')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('No snapshot fallback', result.stderr)
        self.assertNotIn('snapshot_argument', result.stdout)

    def test_missing_package_fails(self):
        result = self.run_cli('SimulationConfig', '--source', 'installed')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('No snapshot fallback', result.stderr)

    def test_missing_symbol_and_member_fail(self):
        self.package.write_text('class SimulationConfig: pass', encoding='utf-8')
        for args in (('Missing',), ('SimulationConfig', '--member', 'missing')):
            result = self.run_cli(*args, '--source', 'installed')
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('No snapshot fallback', result.stderr)
            self.assertNotIn('snapshot_argument', result.stdout)


if __name__ == '__main__':
    unittest.main()
