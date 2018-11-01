# Jupyter Notebook Task List

A small repo for creating and storing a task list in a jupyter notebook. I have
on several occasions wanted to have a task list in a jupyter notebook as well
wanted to start playing around with jupyter widgets. Using the ``TaskList``
class, you can easily create a task list and store it in a json file so when
you come back to the notebook, it starts exactly where you left off.

See ``JNTaskListExample.ipynb`` to see it in action.

I do not plan to release it on pypi since I do not plan on maintaining it long
term or writing any tests. If I see good opportunity to extend it or play
around more with widgets then maybe I will.

License under MIT License.

## Install

python 3.5 and greater.

Must have ``jupyter`` and ``ipywidgets`` installed and enabled. See
[jupyter's documentation](https://ipywidgets.readthedocs.io/en/stable/user_install.html)
on using widgets.

Fork to your local github, clone a fork, cd into your clone, then
``pip install -e .``

## Contributing

Feel free to post an issue or submit a pull request. I cannot guarantee that I
will respond promptly or at all. I mainly posted this for myself to use on
different machines and for anyone wanting a simple task list that can persist
state when restarting the notebook.
