**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 3

<hr>

**Use Case**: Canvas Clearing

**Primary Actor**: User

**Goal in Context**: To clear the canvas entirely by filling it with the last selected color.

**Preconditions**: The canvas contains pixels and a color is selected.

**Trigger**: Pressing the space key.
  
**Scenario**: The user selects a color, then presses the space key after drawing on the canvas, resulting in the entire canvas being filled with the selected color, effectively clearing previous work.
 
**Exceptions**: The program may not respond if it's in an unresponsive state, or if no color is selected prior to pressing the space key, there may need to be a default color set to fill the canvas.

**Priority**: Medium-priority.

**When available**: First release

**Channel to actor**: The primary actor communicates through I/O devices, primarily the keyboard and possibly the mouse (for color selection). The system should respond immediately to the space key event, filling the canvas with the selected color.

**Secondary Actor**: N/A

**Channels to Secondary Actors**: N/A

**Open Issues**: In future releases, it might be necessary to implement an 'undo' functionality, allowing users to revert the canvas to its state prior to clearing.

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
