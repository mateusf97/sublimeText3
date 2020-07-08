import sublime
import sublime_plugin


class EventListener( sublime_plugin.EventListener ):

  def on_load ( self, view ):
    path = (view.file_name())
    folders = path.split("\\")
    public_folder = folders[len(folders)-2]
    print(public_folder)
    if public_folder == "routes":
      view.run_command ( "fold_by_level", { "level": 1 } )
    else:
      view.run_command ( "fold_by_level", { "level": 2 } )