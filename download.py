# MIT License

# Copyright (c) 2018 Rene Jean Corneille

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from os import path, makedirs
from requests import get

if not path.exists('papers'):
    makedirs('papers')

cd = path.abspath(path.dirname(__file__))

with open(path.join(cd, 'README.md'), encoding='utf-8') as f:
    readme = f.readlines()

for line in readme:
    if '[[pdf]]' in line:
        url = line.split('[[pdf]]')[1][:-3][1:]
        filename = '%s%s.pdf' % (path.join(cd, 'papers/'),line.split('[[pdf]]')[0])
        r = get(url, allow_redirects=True)
        open(filename, 'wb').write(r.content)
