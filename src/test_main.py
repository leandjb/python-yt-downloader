import unittest
import tkinter
import customtkinter
from main import clear_fields, update_progress

class TestYouTubeDownloader(unittest.TestCase):
    def setUp(self):
        # Set up a minimal Tkinter root and widgets for testing
        self.root = customtkinter.CTk()
        self.link_box = customtkinter.CTkEntry(self.root)
        self.progress_txt = customtkinter.CTkLabel(self.root)
        self.progress_bar = customtkinter.CTkProgressBar(self.root)
        self.title_txt = customtkinter.CTkLabel(self.root)
        self.info_txt = customtkinter.CTkLabel(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_clear_fields(self):
        self.link_box.insert(0, "test")
        self.progress_txt.configure(text="50%")
        self.progress_bar.set(0.5)
        self.title_txt.configure(text="Test")
        self.info_txt.configure(text="Test")
        clear_fields(self.link_box, self.progress_txt, self.progress_bar, self.title_txt, self.info_txt)
        self.assertEqual(self.link_box.get(), "")
        self.assertEqual(self.progress_txt.cget("text"), "0%")
        self.assertEqual(self.title_txt.cget("text"), "YouTube Downloader")
        self.assertEqual(self.info_txt.cget("text"), "")

    def test_update_progress(self):
        class DummyStream:
            filesize = 100
        update_progress(DummyStream(), None, 50, self.progress_txt, self.progress_bar)
        self.assertEqual(self.progress_txt.cget("text"), "50%")
        self.assertAlmostEqual(self.progress_bar.get(), 0.5, places=1)

if __name__ == "__main__":
    unittest.main()
