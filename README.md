Code (and tests) to determine whether a given Python script requires ast.PyCF_ALLOW_TOP_LEVEL_AWAIT to compile, i.e. whether it uses "Top Level Await."

## Usage

### Command Line

```bash
python asyncfinder.py (filename)

# Example:
>>> python asyncfinder.py ./this_uses_toplevel_await.py
File .\async_finder_tests\naked_asyncFor.py uses top level await
```

### Code

```python
from asyncfinder import TopLevelAwaitFinder

# Python file of interest:
my_file = '/path/to/my/file.py'

with open(my_file, 'r') as f:
    source = f.read()

does_it_need_toplevel_await = TopLeveLAwaitFinder().is_source_async(source)
```

### Testing

With pytest in your environment, run `pytest`.