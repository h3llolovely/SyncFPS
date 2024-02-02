"""
SyncFPS

Author: Jason Schwarz (hellolovely)
Website: https://hellolovely.tv/
Name-US: SyncFPS
Version: 1.0.0
Description-US: Syncronizes active render setting framerate to the project's' framrate.

Written for Maxon Cinema 4D 2023.1.0
Python version 3.4.11

Change log:
1.0.0 (03.10.2023) - Initial release
"""

# Libraries
import c4d
from c4d import gui

# Functions
def main() -> None:
    # Called when the plugin is selected by the user. Similar to CommandData.Execute.
    doc = c4d.documents.GetActiveDocument() # Get active Cinema 4D document
    doc.StartUndo() # Start recording undos
    ProjFPS = doc.GetFps() # Get project framerate

    renderData = doc.GetActiveRenderData() # Get document render data

    rdFPS = renderData[c4d.RDATA_FRAMERATE] # Get render framerate

    doc.AddUndo(c4d.UNDOTYPE_CHANGE, renderData) # Add undo step for render data changes

    renderData[c4d.RDATA_FRAMERATE] = ProjFPS # Sync render framerate to project

    doc.SetActiveRenderData(renderData) # Set render settings

    doc.EndUndo() # Stop recording undos
    c4d.EventAdd() # Update Cinema 4D

    c4d.CallCommand(12373) # Project Settings...
    c4d.CallCommand(12161) # Edit Render Settings...
    # c4d.gui.MessageDialog("Project/Render Framerate Synced")

if __name__ == '__main__':
    main()