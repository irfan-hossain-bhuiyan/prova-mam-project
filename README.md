# Math-1213 project
Our project is about shift of axis.Means how a equation will change after I want to change the point (0,0) to  point (a,b).

## Setted Goal
In our project,we set this goal,

1. Taking an equation as a user input.
2. Taking input of where you want to shift the equation in the x axis and y axis.
3. and return output with the modified equation.
4. Visualize the change in a graph to see,how the graph changes with the shift of axis.
5. Being simple

We did touched every one of those,We could add more,by the time being we restricted ourselve in simple.
Now first see what our program can do,

![Program video](doc_images/run_program.gif)

## Architure of the project

I am using python in my project.

### File structure
```
.
├── README.md
├── doc_images
├── equation
│   ├── __init__.py
├── external_dependencies
│   ├── __init__.py
│   └── color.py
├── main.py
└── ui
    ├── __init__.py
    ├── graph_ui.py
    ├── input_box.py
    ├── input_box_temp.py
    └── ui_component_trait.py
```
So there are a lot of files.

### Dependencies
The dependencies I am using in the project:

1. pygame *this is a game library I am using for the ui.Being so basic it gives me a lot of freedom.*
2. numpy *Numpy is a matrix library. To  do fast numarical calculation numpy is a must.*
3. contourpy *This is a library to get 2d intersection point of the 3d graph.It is really performant*
4. sympy *As the document says It is a computer algebric system.*

### Project explaination
In the start of the project,There are 3 folder and 1 file.

1. ui (*This handle all ui component like graph,text_box*)
2. equation (*This handle converting the user input to equation so I can evalute the equation as function of x,y in 3 dimension.Also it intersect the 3d geometry and intersect it with **xy** plane.*)
3. external_dependencies (*I separated this one for external dependencies.But I rarely needed it.*
4. ```main.py``` (*This is the main file you need to run.*)

### Running the program.
There is already a precompiled program in the dist folder.

Also it can be compiled to source.
To do that,
1. Install python 
2. Run in the command promt:
```bash
pip install numpy pygame contourpy sympy
```
3. After you run the program by running the ```main.py```


