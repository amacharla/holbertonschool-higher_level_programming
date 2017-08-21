  <p>Write a function that prints <code>x</code> elements of a list.</p>

<ul>
<li>Prototype: <code>def safe_print_list(my_list=[], x=0):</code></li>
<li><code>my_list</code> can contain any type (integer, string, etc.)</li>
<li>All elements must be printed on the same line followed by a new line.</li>
<li><code>x</code> represents the number of elements to print</li>
<li><code>x</code> can be bigger than the length of <code>my_list</code></li>
<li>Returns the real number of elements printed</li>
<li>You have to use <code>try: / except:</code> </li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>len()</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x05$ cat 0-main.py
#!/usr/bin/python3
safe_print_list = __import__(&#39;0-safe_print_list&#39;).safe_print_list

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print(&quot;nb_print: {:d}&quot;.format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print(&quot;nb_print: {:d}&quot;.format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print(&quot;nb_print: {:d}&quot;.format(nb_print))

guillaume@ubuntu:~/0x05$ ./0-main.py
12
nb_print: 2
12345
nb_print: 5
12345
nb_print: 5
guillaume@ubuntu:~/0x05$ 
</code></pre>

 <p>Write a function that prints an integer with <code>&quot;{:d}&quot;.format()</code>.</p>

<ul>
<li>Prototype: <code>def safe_print_integer(value):</code></li>
<li><code>value</code> can be any type (integer, string, etc.)</li>
<li>The integer should be printed followed by a new line</li>
<li>Returns <code>True</code> if <code>value</code> has been correctly printed (it means the <code>value</code> is an integer)</li>
<li>Otherwise, returns <code>False</code></li>
<li>You have to use <code>try: / except:</code> </li>
<li>You have to use <code>&quot;{:d}&quot;.format()</code> to print as integer</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>type()</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x05$ cat 1-main.py
#!/usr/bin/python3
safe_print_integer = __import__(&#39;1-safe_print_integer&#39;).safe_print_integer

value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print(&quot;{} is not an integer&quot;.format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print(&quot;{} is not an integer&quot;.format(value))

value = &quot;Holberton&quot;
has_been_print = safe_print_integer(value)
if not has_been_print:
    print(&quot;{} is not an integer&quot;.format(value))

guillaume@ubuntu:~/0x05$ ./1-main.py
89
-89
Holberton is not an integer
guillaume@ubuntu:~/0x05$ 
</code></pre>

 <p>Write a function that prints the first <code>x</code> elements of a list and only integers.</p>

<ul>
<li>Prototype: <code>def safe_print_list_integers(my_list=[], x=0):</code></li>
<li><code>my_list</code> can contain any type (integer, string, etc.)</li>
<li>All integers have to be print in the same line followed by a new line.</li>
<li><code>x</code> represents the number of elements to access in <code>my_list</code></li>
<li><code>x</code> can be bigger than the length of <code>my_list</code></li>
<li>Returns the real number of integers printed</li>
<li>You have to use <code>try: / except:</code> </li>
<li>You have to use <code>&quot;{:d}&quot;.format()</code> to print an integer</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>len()</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x05$ cat 2-main.py
#!/usr/bin/python3
safe_print_list_integers = \
    __import__(&#39;2-safe_print_list_integers&#39;).safe_print_list_integers

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print(&quot;nb_print: {:d}&quot;.format(nb_print))

my_list = [1, 2, 3, &quot;Holberton&quot;, 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print(&quot;nb_print: {:d}&quot;.format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print(&quot;nb_print: {:d}&quot;.format(nb_print))

guillaume@ubuntu:~/0x05$ ./2-main.py
12
nb_print: 2
12345
nb_print: 5
12345Traceback (most recent call last):
  File &quot;./2-main.py&quot;, line 14, in &lt;module&gt;
    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
  File &quot;/0x05/2-safe_print_list_integers.py&quot;, line 7, in safe_print_list_integers
    print(&quot;{:d}&quot;.format(my_list[i]), end=&quot;&quot;)
IndexError: list index out of range
guillaume@ubuntu:~/0x05$ 
</code></pre>

 <p>Write a function that divides element by element 2 lists.</p>

<ul>
<li>Prototype: <code>def list_division(my_list_1, my_list_2, list_length):</code></li>
<li><code>my_list_1</code> and <code>my_list_2</code> can contain any type (integer, string, etc.)</li>
<li><code>list_length</code> can be bigger than the length of both lists</li>
<li>Returns a new list (length = <code>list_length</code>) with all divisions</li>
<li>If 2 elements can&#39;t be divided, the division result should be equal to <code>0</code></li>
<li>If an element is not an integer or float:

<ul>
<li>print: <code>wrong type</code></li>
</ul></li>
<li>If the division can&#39;t be done (<code>/0</code>):

<ul>
<li>print: <code>division by 0</code></li>
</ul></li>
<li>If <code>my_list_1</code> or <code>my_list_2</code> is too short

<ul>
<li>print: <code>out of range</code></li>
</ul></li>
<li>You have to use <code>try: / except: / finally:</code> </li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x05$ cat 4-main.py
#!/usr/bin/python3
list_division = __import__(&#39;4-list_division&#39;).list_division

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print(&quot;--&quot;)

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, &quot;H&quot;, 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

guillaume@ubuntu:~/0x05$ ./4-main.py
[5.0, 2.0, 1.0]
--
division by 0
wrong type
out of range
[5.0, 0, 0, 2.0, 0]
guillaume@ubuntu:~/0x05$ 
</code></pre>

 <p>Write a function that raises a type exception.</p>

<ul>
<li>Prototype: <code>def raise_exception():</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x05$ cat 5-main.py
#!/usr/bin/python3
raise_exception = __import__(&#39;5-raise_exception&#39;).raise_exception

try:
    raise_exception()
except TypeError as te:
    print(&quot;Exception raised&quot;)

guillaume@ubuntu:~/0x05$ ./5-main.py
Exception raised
guillaume@ubuntu:~/0x05$ 
</code></pre>

 <p>Write a function that raises a name exception with a message.</p>

<ul>
<li>Prototype: <code>def raise_exception_msg(message=&quot;&quot;):</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x05$ cat 6-main.py
#!/usr/bin/python3
raise_exception_msg = __import__(&#39;6-raise_exception_msg&#39;).raise_exception_msg

try:
    raise_exception_msg(&quot;C is fun&quot;)
except NameError as ne:
    print(ne)

guillaume@ubuntu:~/0x05$ ./6-main.py
C is fun
guillaume@ubuntu:~/0x05$ 
</code></pre>
