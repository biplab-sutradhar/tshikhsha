## Prerequisites

- `node >= 20`
- `python >= 3.11`

### Install these packages for python package management

```sh
pip install poetry
poetry self add poetry-plugin-shell
```

Read more about poetry [here](https://python-poetry.org/docs/cli/).

## Install dependencies and run locally:

```sh

# clone project
git clone https://github.com/TeamShiksha/team.shiksha.git

# change directory
cd team.shiksha

# install dependencies. `postinstall` script is given in root
# `package.json` to create virutal environment for `server`.
pnpm install

# activate python virtual environment
pnpm activate
# after running the above command your terminal will something look like:
# (server-py3.13) F:\.\.\team.shiksha\packages\server>, where `server-py3.13` is virtual environment
# as given in the example above, your directory will change to `server`

# in order to run the commands from root, change the directory to `team.shiksha`
cd ..
cd ..

# Now your current working directory should be `team.shiksha`
# If yes, you are ready to run the commands from root
pnpm dev
# frontend runs on  http://localhost:3000
# backend runs on  http://localhost:8000
```

## Adding/Remove dependencies

- Frontend
```sh
# Add
pnpm --filter web add <package_name>

# Remove
pnpm --filter web remove <package_name>
```

- Backend
```sh
# Add
pnpm --filter server add-py <package_name>

# Remove
pnpm --filter server remove-py <package_name>
```

## More

Following commands are added in both frontend and backend:
- `lint` - checks for linting issues
- `format` - runs prettier
- `test` - runs tests
- `check` - run prettier check
- `coverage` - get test coverage report

`husky pre-commit` is added which runs `lint` and `check` command everytime your commit your code. Commit will fail if any of the command fails.