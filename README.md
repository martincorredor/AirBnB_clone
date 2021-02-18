# AirBnB clone - The console

## Description
In this repository I develop the first step for AirBnB clone.
This step consists of creating a shell to manage AirBnB objects. As a command interpreter take the Shell example, but limited to a specific case. In this case, you want to be able to manage the project objects:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

**This project is part of the Holberton School Full-Stack Software Engineer program.**

### How to install it? :question: ###
To have this repository and its content, you must execute the following on your terminal:
~~~
$ git clone https://github.com/martincorredor/AirBnB_clone.git
$cd AirBnB_Clone
~~~
## How use it
- You can run the console mode:
### Interactive
```python
$ ./console.py
(hbnb)
```
### Non-Interactive
```python
$ echo "help" | ./console.py
(hbnb)
```

## Content
| Filename | Description |
| ---- | ---- |
| AUTHORS | List all individuals having contributed content to the repository. Docker's format reference |
| LICENSE | MIT LICENSE AND COPYTIGHT NOTICE |
| console.py | Contains the entry point of the command interpreter `./console.py`|
| base_model.py | Defines all common attributes/methods - contains BaseModel class, constructor and methods |
| `__init__.py` | File to convert directories into python modules, one of them contains reload method from FileStorage class |
| file_storage.py | Serializes/deserializes into JSON/PYTHON format - contains FileStorage class and methods |
| user.py | Inherits from BaseModel - contains class attributes like email, password, first_name and last_name |
| state.py | Inherits from BaseModel - contains class attributes like name |
| city.py | Inherits from BaseModel - contains class attributes like state_id and name |
| amenity.py | Inherits from BaseModel - contains class attributes like state_id and name |
| place.py | Inherits from BaseModel - contains class attributes like city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude and amenity_ids |
| review.py | Inherits from BaseModel - contains class attributes like place_id, user_id and text |
| README.md | Description of the proyect and command interpreter |

## BaseModel Methods
| Class | Methods |
| ---- | ---- |
| `__str__()` | returns string format of the object, with class.name id and dict |
| save() | updates instance attribute updated_at and save string into file.json |
| to_dict() | returns a dictionary with isoformat, class name and all keys/values |

## FileStorage Methods
| Class | Methods |
| ---- | ---- |
| all() | returns a dictionary `__objects` |
| new() | sets the argument given as a value in the dictionary |
| save() | serializes from string to json and store it in file.json |
| reload() | deserializes from json to string and store it in file.json using save |

## Tests
- The code of this project is tested with the **unittest** module, to run it type:
```python
$ python3 -m unittest discover tests
```
## Environment
* Language: Python3
* OS: Ubuntu 14.04 LTS
* Style guide for Python code: [PEP8](https://www.python.org/dev/peps/pep-0008/)

## Authors
* [Martin Corredor](https://twitter.com/Richi_Corredor)