# ipython_infer_underscore
An ipython *input transformer* that allows for quicker numerical calculations in an ipython or qtconsole shell by automatically inferring the "_" character (previous result) whenever an operation occurs as the first character. This is similar to many calculator programs that infer "ans" or the previous result if the first character is a operator.

Supported operators include `+`, `-`, `*`, `/`, `.`

A special case is if a numeric character immediately follows a period (`.`). In this case, we're not calling a subclass or function but instead entering a decimal (e.g. `.5 == 0.5` but `.callable() == _.callable()`)

## Examples
```
5.0
Out[1]: 5.0

/2
Out[2]: 2.5

+1
Out[3]: 3.5
```

This also works with subclass operators:
```
12.4*u.mm
Out[1]: 12.4 <Unit('millimeter')>

.to(u.inch)
Out[2]: 0.48818897637795283 <Unit('inch')>
```

## Usage
To use this input transformer we must register the module as an input transformer in `ipython_config.py`. The recommended way to do this is by appending it to the list of transformers when ipython starts up.

First, add infer_underscore.py to the list of files to run upon ipython startup. In `ipython_config.py` add the following line:
```
c.InteractiveShellApp.exec_files = ["FULL//PATH//TO//ipython_infer_underscore//infer_underscore.py"]
```

Next add the following python code lines below that to execute upon ipython startup. If you already have some code to execute, simply add these lines at the end of the list.
```
c.InteractiveShellApp.exec_lines = [
    # Automatically infer underscore when missing
    'import sys',
    'sys.path.append("PATH//TO//ipython_infer_underscore")',
    'from infer_underscore import *',
    'ip = get_ipython()',
    'ip.input_transformers_cleanup.append(infer_underscore)'
]
```
