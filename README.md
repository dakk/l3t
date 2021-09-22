# l3t
A tool for lisk3 node management.


## Install

```bash
sudo python3 setup.py install
```


## Usage

```bash
usage: usage: l3t [-h] action [arguments]

Lisk3 node management tool

actions:
  rebuild		      rebuild node from snapshot
  install		      install lisk-core
  save-forging	  save forging info
  update		      update lisk-core
  enable-forging	enable forging
  start		        start node
  stop		        stop node
  logs		        show node logs
  info		        show node info

optional arguments:
  -h, --help            show this help message and exit
  --base-path BASEPATH  set base path (default: /home/lisk/)
```


## License

```
MIT License

Copyright (c) 2021 Davide Gessa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```