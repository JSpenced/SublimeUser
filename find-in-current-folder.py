import sublime, sublime_plugin
import os
class FindInCurrentFolderCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        window = view.window()
        current_dir = os.path.dirname(view.file_name())
        window.run_command("show_panel", {"panel": "find_in_files", "where": current_dir})
