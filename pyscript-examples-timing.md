# PyScript Example Timing Data

## TL;DR

Parsing the AST is slower than `'asyncio' in source` by only a matter of milliseconds.

## Justificaiton

This project was started as a possible improvement to [PyScript](https://github.com/pyscript/pyscript). PyScript needs to determine whether to run each code chunk with Pyodide's [runPython](https://github.com/pyodide/pyodide/blob/6ca76fb725161dacf1940406f5996bc817ac00bb/src/js/api.ts#L72-L81) or [runPythonAsync](https://github.com/pyodide/pyodide/blob/6ca76fb725161dacf1940406f5996bc817ac00bb/src/js/api.ts#L173-L182) functions. 

As of PyScript 2022.06.1, this is done simply be detecting whether the string '*asyncio*' is present in the source code. This is fast, but ultimately missses some situations where top-level await is necessary. This library presents a solution which parses the source into an Abstract Syntax Tree, and detects if any `await`, `await for`, or `await with` statements exist outside of `async def` blocks, which is the definition of requiring top-level await.

## Timing

### Discussion

Using TopLevelAsyncFinder() to parse the code and determine if it requires to level await is more correct, but takes longer. The following is a comparison of the time required to detect if 'asyncio' is present in the source, versus using TopLevelAsyncFinder, for most of the current PyScript examples. 

This was done by surrounding the relevant code in `console.time()` and `console.timeEnd()`. Each method was tried three times for each example and the results averaged. *Not all examples ended up being tesed with the string-inclusion method, since the longest were less than 10 microseconds.*

### Conclusion

The longest current example, [WebGL Raycaster](https://github.com/pyscript/pyscript/tree/main/examples/webgl/raycaster), takes just over 7 milliseconds to parse and determine whether it requires top-level await. The shortest examples take less than a millisecond. Given that PyScript takes several seconds to load under typical conditions, this seems acceptable.

### Data

| Example                  | "asyncio" in source (ms)| TopLevelAsyncFinder (ms)|
|--------------------------|-------------------|---------------|
| Hello World              |                   |  0.401 |
| Simple Clock             |                   |  0.344 |
| Todo                     |                   |   1.935 |
| Pyscript Native Todo     |                   |  0.589 |
| Matplotlib               |                   |   1.935 |
| Altair                   |                   |   1.500 |
| Folium                   |                   |   1.048 |
| D3                       |                   |    2.765 |
| Webgl                    |            0.0076 |   6.546 |
| Simple Static Bokeh Plot |                   |  0.914 |
| Bokeh Interative         |                   |   1.923 |
| KMeans                   |                   |    4.144 |
| Streaming                |                   | -             |
| Simple Panel             |                   |  0.741 |
| NYC Taxi                 |                   | -             |
| Freedom Units            |                   |  0.425 |
| Fractals                 |    0.0067 |   5.76 |