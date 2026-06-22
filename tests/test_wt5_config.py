from pathlib import Path
import tempfile
import unittest

from wt5_config import load_configs, load_site_config


class ConfigEncodingTests(unittest.TestCase):
    def test_bom_marked_ini_loads(self):
        content = (
            "[site]\n"
            "latitude = -32.724\n"
            "longitude = 152.130167\n"
            "\n"
            "[antenna:East]\n"
            "port = /dev/ttyUSB0\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "wt5.ini"
            path.write_text(content, encoding="utf-8-sig")
            site = load_site_config(path)
            configs = load_configs(path)
        self.assertAlmostEqual(site.latitude, -32.724)
        self.assertIn("East", configs)
        self.assertEqual(configs["East"].port, "/dev/ttyUSB0")


if __name__ == "__main__":
    unittest.main()
