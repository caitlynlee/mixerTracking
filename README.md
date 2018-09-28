# mixerTracking
GUI made to track individuals in a party, built using processing, python mode.

### Before use
Processing 3 must be downloaded and installed before using this program. You can download processing here:
https://processing.org/download/


### Usage
Video files (assuming .mp4 format) must be placed in the "data" directory, inside the "tracking" directory.

Click to add individuals, once an individual is added, click the circle to toggle that individual (they will change from white to red). While an individual is selected:  
- use the left/right arrow keys to change the shoulder angle and drag to move position.
- **FULL KEYBOARD CONTROLS**: i/j/k/l keys to move dot/triangle up/left/down/right and a/d keys to rotate.
- 't' to toggle whether individual is speaking or not.
- type in custom subject ID and press Enter to save. (Pressing 'h' to hide the video will show subject IDs to confirm custom ID was added/saved)
- Backspace to delete the triangle  

Click the individual's circle again to deselect.

Spacebar to pause/play video. 'h' to toggle show/hide video. When video is hidden, tracking subject IDs will be shown.

Down arrow key to go back 10 seconds (all the data that was collected in that 10 seconds will be deleted and need to be re-done).

'q' to export data to csv.
