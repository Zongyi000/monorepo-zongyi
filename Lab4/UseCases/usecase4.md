**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 4

<hr>

**Use Case**: Pixel Color Change on Mouse Press

**Primary Actor**: User

**Goal in Context**: To change the color of pixels on the canvas by pressing and dragging the mouse, simulating the drawing action of a pencil on paper.

**Preconditions**: The canvas is active and responsive, and a color is selected.

**Trigger**: The user presses and holds the left mouse button while moving the mouse over the canvas area.
  
**Scenario**: A user selects a color from the color palette, presses the left mouse button on the canvas, and drags the mouse to draw on the canvas. The pixels under the path of the mouse pointer change to the selected color.
 
**Exceptions**: The canvas may not register color changes if it becomes unresponsive, or if there is an issue with the selected color or mouse input. The user may need to reselect the color or restart the application if necessary.

**Priority**: High-priority.

**When available**: First release

**Channel to actor**: The primary actor interacts through I/O devices: a computer mouse and a display screen showing the canvas. The system should register and reflect the color change on the canvas instantly as the user moves the mouse while holding the left button.

**Secondary Actor**: N/A

**Channels to Secondary Actors**: N/A

**Open Issues**: Future updates may incorporate various drawing tools and brush effects, necessitating modifications to this use case to accommodate those additional features.

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
