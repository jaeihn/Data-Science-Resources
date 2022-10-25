---
layout: default
title:  "bash"
---

# bash commands

<table>
    <thead>
        <tr>
            <th>Command</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>pwd</code></td>
            <td>print working directory</td>
        </tr>
        <tr>
            <td><code>ls</code></td>
            <td>list contents</td>
        </tr>
        <tr>
            <td><code>cd</code></td>
            <td>change directory</td>
        </tr>
        <tr>
            <td><code>mkdir {dirname}</code></td>
            <td>make directory</td>
        </tr>
        <tr>
            <td><code>rm {filename}</code></td>
            <td>delete file</td>
        </tr>
        <tr>
            <td><code>mv {path1} {path2}</code></td>
            <td>move files; rename files</td>
        </tr>
        <tr>
            <td><code>cp {filename}</code></td>
            <td>copy files</td>
        </tr>
        <tr>
            <td><code>man {command}</code></td>
            <td>look up manual</td>
        </tr>
        <tr>
            <td><code>history</code></td>
            <td>show history of commands</td>
        </tr>
        <tr>
            <td><code>grep "{str}" {file}</code></td>
            <td>search for pattern str in a file</td>
        </tr>
        <tr>
            <td><code>{command1} | {command2}</code></td>
            <td>piping; output of command1 into command2</td>
        </tr>
        <tr>
            <td><code>wc -l {filename}</code></td>
            <td>count how many lines are in file</td>
        </tr>
        <tr>
            <td><code>head -n 10 {filename}</code></td>
            <td>show first 10 lines of file</td>
        </tr>
        <tr>
            <td><code>tail -n 10 {filename}</code></td>
            <td>show last 10 lines of file</td>
        </tr>
    </tbody>
</table>



# conda commands


<table>
    <thead>
        <tr>
            <th>Command</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>conda info --envs</code></td>
            <td>Show list of environments</td>
        </tr>
        <tr>
            <td><code>conda env list</code></td>
            <td>Show list of environments</td>
        </tr>
        <tr>
            <td><code>conda create --name {env-name}</code></td>
            <td>Create an environment</td>
        </tr>
        <tr>
            <td><code>conda env create -f {environment}.yml</code></td>
            <td>Create an environment from .yml file</td>
        </tr>
        <tr>
            <td><code>activate {env-name}</code></td>
            <td>For macOS and Linux, <code>activate {env-name}</code></td>
        </tr>
        <tr>
            <td><code>conda remove --name {env-name} --all</code></td>
            <td>Remove an environment</td>
        </tr>
        <tr>
            <td><code>conda env remove --name {env-name}</code></td>
            <td>Remove an environment</td>
        </tr>
    </tbody>
</table>


## Adding <code>alias</code> 
Common commands can be added as alias into .bash_profile.
