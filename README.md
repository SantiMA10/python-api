# Python API

> Example python api with uv as package manager

## References
- [pmareke YouTube channel](https://www.youtube.com/@pmareke)

## Build with...
- python 3.12
- [uv](https://docs.astral.sh/uv/)
- [fastapi](https://fastapi.tiangolo.com/)
- [pytest](https://pytest.org/)
- [expects](https://expects.readthedocs.io/en/latest/)
- [doublex](https://python-doublex.readthedocs.io/en/latest/)
- [ruff](https://docs.astral.sh/ruff/)

## How to...

### init your local environment

```bash
git clone git@github.com:SantiMA10/python-api.git
cd python-api
make local-setup
```

### Run the project

```bash
make run
```

And have fun with the api 🎉

### Run the test

```bash
make test
```

### Add dependencies

```bash
make add-package package=<name of the dependency>
```

### Have ruff working in VS Code
- Install the extension from the store
- Add the following snippet to your user config:
    ```json
    {
      "[python]": {
        "editor.formatOnType": true,
        "editor.formatOnSave": true,
        "editor.defaultFormatter": "charliermarsh.ruff"
      },
    }
    ```