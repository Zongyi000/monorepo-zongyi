**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 1

<hr>

**Use Case**: Canvas Size Initialization

**Primary Actor**: System

**Goal in Context**: To initialize the application window with a drawable canvas of specified size (600 pixels wide by 400 pixels high).

**Preconditions**: Application is launched and system resources are available for allocation.

**Trigger**: Application starting event initiated by the user or system.
  
**Scenario**: Upon application startup, the system initializes a window with a drawable canvas sized 600x400 pixels.
 
**Exceptions**: The system might not have sufficient resources to initialize the application window. In this case, an error message is displayed to the user, prompting them to free up resources or try again later.

**Priority**: High-priority.

**When available**: First release

**Channel to actor**:System's internal processes and mechanisms handle the canvas initialization automatically without direct user input for this use case. User interacts with the initialized canvas for further operations.

**Secondary Actor**: User 

**Channels to Secondary Actors**: The User observes the system initialized canvas and interacts with it through I/O devices like the mouse and keyboard.

**Open Issues**: Future versions might require resizable canvases, which will necessitate adjustments to this use case to incorporate user-defined sizes.

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
