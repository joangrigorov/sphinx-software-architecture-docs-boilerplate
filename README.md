# {PROJECT_NAME} Software Architecture Documentation

# Recommended: run `./init` after cloning this repository so you can set project name and author.

This is the repository containing the software architecture documentation sources of {PROJECT_NAME}.
Documentation is maintained by {AUTHOR}.

## Building the documentation

### HTML version (with autobuild)
To build the documentation in an HTML variant run:

```shell
./sphinx autobuild
```

The documentation will run via a webserver on port 8000. A web browser window will open.

### PDF version
To build a PDF version you can run:

```shell
./sphinx
```

The output PDF file can be found in `build/latex` path.
