#!/usr/bin/python3
"""Script that starts a Flask web application"""


from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown_data(self):
    """remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ return all states in the db  """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ return all cities in the db  """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """display the states and cities listed in alphabetical order"""
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
