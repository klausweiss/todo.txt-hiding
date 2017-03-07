# todo.txt-hiding

*A [todo.txt](https://github.com/ginatrapani/todo.txt-cli) plugin for hiding tasks with specified project/context (a set of keywords).*

## Installation

1. `cd` into the addons directory
2. clone this repository into the *hiding* directory:

        git clone git@github.com:klausweiss/todo.txt-hiding.git hiding

## Usage

* To display list of the tasks not in context `@someday`:
    
        todo.sh hiding @someday

* To display list of the tasks not related with project `+todo.txt` not in the `@in` context:

        todo.sh hiding +todo.txt @in

* To display list of the tasks not containing keywords `JAVA` and `windows`

        todo.sh hiding JAVA windows

## Compatibility

Tested with *todo.txt* @DEV_VERSION@

## Credits

Mikołaj Biel, 2017
