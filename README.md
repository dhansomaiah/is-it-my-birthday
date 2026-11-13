# is-it-my-birthday

The most efficient birthday checker in the world. It needs to be wrong once.

```python
def is_it_my_birthday():
    return MEMORY.exists() and MEMORY.read_text() == f"{date.today():%m-%d}"
```

It starts out knowing nothing, so it says no. That is correct 99.7% of the time, for anyone.

On the one day it's wrong, tell it. It writes the date down and is right from then on.

```
$ python birthday.py
No.
$ python birthday.py it is
Sorry. Happy birthday. It won't happen again.
$ python birthday.py
Yes. Happy birthday.
```

The test asks it every day for 400 years. It is wrong once.

```bash
pytest
```
