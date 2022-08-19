Code (and tests) to determine whether a given Python script requires ast.PyCF_ALLOW_TOP_LEVEL_AWAIT to compile, i.e. whether it uses "Top Level Await"

## Usage

### Command Line

```
python asyncfinder.py (filename)

Example:
>>> python asyncfinder.py ./this_uses_toplevel_await.py
File .\async_finder_tests\naked_asyncFor.py uses top level await
```

### Code

```
from asyncfinder import TopLevelAwaitFinder