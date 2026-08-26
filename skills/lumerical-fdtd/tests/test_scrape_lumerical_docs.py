import importlib.util
import pathlib
import sys
import tempfile
import unittest


SCRIPT = pathlib.Path(__file__).resolve().parents[1] / "scripts" / "scrape_lumerical_docs.py"


def load_scraper():
    spec = importlib.util.spec_from_file_location("scrape_lumerical_docs", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class ScrapeLumericalDocsTest(unittest.TestCase):
    def test_slug_from_article_url_keeps_article_id_and_title(self):
        scraper = load_scraper()
        url = "https://optics.ansys.com/hc/en-us/articles/360034924173-addfdtd-Script-command"

        slug = scraper.slug_from_url(url)

        self.assertEqual(slug, "360034924173-addfdtd-script-command")

    def test_extract_article_markdown_keeps_article_body_not_navigation(self):
        scraper = load_scraper()
        html = """
        <html>
          <head><title>Ignored browser title</title></head>
          <body>
            <nav>Navigation should not appear</nav>
            <article>
              <h1>FDTD solver object</h1>
              <p>The solver controls the simulation region.</p>
              <h2>Mesh</h2>
              <ul><li>Use convergence testing.</li></ul>
              <table>
                <tr><th>Property</th><th>Meaning</th></tr>
                <tr><td>mesh accuracy</td><td>Automatic mesh setting</td></tr>
              </table>
              <pre>addfdtd;</pre>
              <p>See <a href="/hc/en-us/articles/1">related article</a>.</p>
            </article>
          </body>
        </html>
        """

        doc = scraper.extract_article("https://optics.ansys.com/hc/en-us/articles/1", html)

        self.assertEqual(doc.title, "FDTD solver object")
        self.assertIn("The solver controls the simulation region.", doc.markdown)
        self.assertIn("## Mesh", doc.markdown)
        self.assertIn("- Use convergence testing.", doc.markdown)
        self.assertIn("```", doc.markdown)
        self.assertIn("[related article](https://optics.ansys.com/hc/en-us/articles/1)", doc.markdown)
        self.assertNotIn("Navigation should not appear", doc.markdown)
        self.assertIn("mesh accuracy", doc.plain_text)
        self.assertEqual(doc.tables[0]["headers"], ["Property", "Meaning"])
        self.assertEqual(doc.tables[0]["rows"][0], ["mesh accuracy", "Automatic mesh setting"])

    def test_render_scraped_page_bounds_verbatim_excerpt(self):
        scraper = load_scraper()
        source = {
            "area": "Solver",
            "title": "FDTD solver",
            "url": "https://optics.ansys.com/hc/en-us/articles/1",
            "topic": "Solver setup",
        }
        doc = scraper.ArticleDoc(
            url=source["url"],
            title="FDTD solver",
            markdown="# FDTD solver\n\n" + "word " * 250,
            plain_text="FDTD solver " + "word " * 250,
            headings=["FDTD solver"],
            links=[],
            code_blocks=[],
            inline_codes=[],
            tables=[],
        )

        rendered = scraper.render_scraped_page(source, doc, "2026-06-21", max_excerpt_words=25)

        self.assertIn("Source URL:", rendered)
        self.assertIn("## Local Capture Summary", rendered)
        self.assertIn("## Key Terms", rendered)
        self.assertIn("Official Text Excerpt", rendered)
        self.assertNotIn("word " * 30, rendered)

    def test_render_scraped_page_includes_table_and_link_groups(self):
        scraper = load_scraper()
        source = {
            "area": "Solver",
            "title": "FDTD solver",
            "url": "https://optics.ansys.com/hc/en-us/articles/1",
            "topic": "Solver setup",
        }
        doc = scraper.ArticleDoc(
            url=source["url"],
            title="FDTD solver",
            markdown="# FDTD solver\n\nMesh PML mode source monitor.",
            plain_text="FDTD solver mesh PML mode source monitor.",
            headings=["FDTD solver"],
            links=[
                ("Mesh", "https://optics.ansys.com/hc/en-us/articles/2"),
                ("PyLumerical", "https://lumerical.docs.pyansys.com/version/stable/index.html"),
                ("Example file", "https://example.com/file.fsp"),
            ],
            code_blocks=[],
            inline_codes=["addfdtd"],
            tables=[{"headers": ["Property"], "rows": [["mesh accuracy"]]}],
        )

        rendered = scraper.render_scraped_page(source, doc, "2026-06-21", max_excerpt_words=25)

        self.assertIn("## Table Inventory", rendered)
        self.assertIn("Table 1: 1 column(s), 1 row(s)", rendered)
        self.assertIn("## Official Links Found", rendered)
        self.assertIn("## External Links Found", rendered)
        self.assertIn("mesh", rendered.lower())

    def test_discover_sources_tracks_depth_and_topic(self):
        scraper = load_scraper()
        source = {"title": "Seed", "url": "https://optics.ansys.com/hc/en-us/articles/seed", "depth": 0}
        doc = scraper.ArticleDoc(
            url=source["url"],
            title="Seed",
            markdown="",
            plain_text="",
            headings=[],
            links=[
                ("Mode source", "https://optics.ansys.com/hc/en-us/articles/360034902153-Mode-source-Simulation-object"),
                ("Community", "https://example.com/not-official"),
            ],
            code_blocks=[],
            inline_codes=[],
            tables=[],
        )

        discovered = scraper.discover_sources([(source, doc)], set(), limit=10, depth=1)

        self.assertEqual(len(discovered), 1)
        self.assertEqual(discovered[0]["depth"], 1)
        self.assertIn("Discovered from Seed", discovered[0]["topic"])

    def test_write_corpus_indexes_creates_topic_and_link_files(self):
        scraper = load_scraper()
        sources = [
            {
                "area": "Mesh",
                "title": "Mesh override",
                "url": "https://optics.ansys.com/hc/en-us/articles/1",
                "topic": "Mesh setup",
                "last_checked": "2026-06-21",
                "local_file": "scraped/1.md",
                "status": "ok",
                "word_count": "100",
                "link_count": "2",
                "table_count": "1",
                "code_count": "0",
            }
        ]
        doc = scraper.ArticleDoc(
            url=sources[0]["url"],
            title="Mesh override",
            markdown="",
            plain_text="mesh override",
            headings=["Mesh override"],
            links=[("FDTD", "https://optics.ansys.com/hc/en-us/articles/2")],
            code_blocks=[],
            inline_codes=[],
            tables=[],
        )

        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            scraper.write_corpus_indexes(sources, [(sources[0], doc)], root)

            self.assertTrue((root / "corpus-index.md").exists())
            self.assertTrue((root / "link-graph.md").exists())
            self.assertIn("Mesh", (root / "corpus-index.md").read_text(encoding="utf-8"))

    def test_write_inventory_creates_markdown_table(self):
        scraper = load_scraper()
        sources = [
            {
                "area": "Python API",
                "title": "Python API overview",
                "url": "https://optics.ansys.com/hc/en-us/articles/2",
                "topic": "Automation",
                "last_checked": "2026-06-21",
                "local_file": "scraped/2.md",
                "status": "ok",
            }
        ]

        with tempfile.TemporaryDirectory() as tmp:
            output = pathlib.Path(tmp) / "source-inventory.md"
            scraper.write_inventory(sources, output)

            text = output.read_text(encoding="utf-8")

        self.assertIn("| Python API |", text)
        self.assertIn("[Python API overview](https://optics.ansys.com/hc/en-us/articles/2)", text)
        self.assertIn("scraped/2.md", text)

    def test_source_docs_include_direct_pylumerical_usage_pages(self):
        scraper = load_scraper()
        urls = {source["url"] for source in scraper.SOURCE_DOCS}

        required_urls = {
            "https://lumerical.docs.pyansys.com/version/stable/user_guide/session_management.html",
            "https://lumerical.docs.pyansys.com/version/stable/user_guide/script_commands_as_methods.html",
            "https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html",
            "https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html",
            "https://lumerical.docs.pyansys.com/version/stable/user_guide/accessing_simulation_results.html",
            "https://lumerical.docs.pyansys.com/version/stable/api/interface_class.html",
            "https://lumerical.docs.pyansys.com/version/stable/api/simobject_class.html",
            "https://lumerical.docs.pyansys.com/version/stable/api/autodiscovery.html",
            "https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_pythonic/fdtd_example1_pythonic.html",
            "https://lumerical.docs.pyansys.com/version/stable/user_guide/photonic_inverse_design_with_lumopt2.html",
        }

        self.assertTrue(required_urls.issubset(urls))


if __name__ == "__main__":
    unittest.main()
