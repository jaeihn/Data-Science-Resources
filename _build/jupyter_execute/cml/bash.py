#!/usr/bin/env python
# coding: utf-8

# # bash

# <table>
#     <thead>
#         <tr>
#             <th>Command</th>
#             <th>Description</th>
#         </tr>
#     </thead>
#     <tbody>
#         <tr>
#             <td><code>whoami</code></td>
#             <td>print username</td>
#         </tr>
#         <tr>
#             <td><code>pwd</code></td>
#             <td>print working directory</td>
#         </tr>
#         <tr>
#             <td><code>ls -a </code></td>
#             <td>list contents; <code>-all</code> include hidden files; <code>-Format</code>decorate with file type <code>/</code> = directory, <code>*</code> = executable; <code>-long</code>include file information; <code>-t</code> sort files by time; <code>-r</code> sort in reverse order</td>
#         </tr>
#         <tr>
#             <td><code>cd</code></td>
#             <td>change directory</td>
#         </tr>
#         <tr>
#             <td><code>mkdir {dirname}</code></td>
#             <td>make directory</td>
#         </tr>
#         <tr>
#             <td><code>rm {filename}</code></td>
#             <td>delete file</td>
#         </tr>
#         <tr>
#             <td><code>mv {path1} {path2}</code></td>
#             <td>move files; rename files</td>
#         </tr>
#         <tr>
#             <td><code>mv -i -v</code></td>
#             <td>-interactive (asks for confirmation); -verbose</td>
#         </tr>
#         <tr>
#             <td><code>cp {filename}</code></td>
#             <td>copy files</td>
#         </tr>
#         <tr>
#             <td><code>cp {dirname} -r</code></td>
#             <td>copy directory with file contents, -recursively</td>
#         </tr>
#         <tr>
#             <td><code>man {command}</code> or <code>{command} --help</code></td>
#             <td>look up manual; <code>space</code> to advance, <code>b</code> to back up, <code>q</code> to quit, <code>/</code> to search, <code>n</code> to next match <code>shift</code>+<code>n</code> to previous match</td>
#         </tr>
#         <tr>
#             <td><code>history</code></td>
#             <td>show history of commands</td>
#         </tr>
#         <tr>
#             <td><code>history | grep "{command}"</code></td>
#             <td>search command history</td>
#         </tr>
#         <tr>
#             <td><code>grep "{str}" {file}</code></td>
#             <td>search for pattern str in a file</td>
#         </tr>
#         <tr>
#             <td><code>{command1} | {command2}</code></td>
#             <td>piping; output of command1 into command2</td>
#         </tr>
#         <tr>
#             <td><code>wc -l {filename}</code></td>
#             <td>count how many lines are in file</td>
#         </tr>
#         <tr>
#             <td><code>head -n 10 {filename}</code></td>
#             <td>show first 10 lines of file</td>
#         </tr>
#         <tr>
#             <td><code>tail -n 10 {filename}</code></td>
#             <td>show last 10 lines of file</td>
#         </tr>
#     </tbody>
# </table>
# 

# ## Adding <code>alias</code> 
# 
# Common commands can be added as alias into .bash_profile. This creates a shorthand for commands with lots of flags or a long series of pipes that you use often. 
# 
# <code>alias l="ls -aFltr"</code>
# 

# In[ ]:




