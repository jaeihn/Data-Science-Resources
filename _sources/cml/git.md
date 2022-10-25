# git Commands

<table>
    <thead>
        <tr>
            <th>Command</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>git status</code></td>
            <td>View staging area</td>
        </tr>
        <tr>
            <td><code>git add {filename}</code></td>
            <td>add file to staging area</td>
        </tr>
        <tr>
            <td><code>git add -u</code></td>
            <td>only add updates (and deletions)</td>
        </tr>
        <tr>
            <td><code>git add -A</code></td>
            <td>add everything available to staging area</td>
        </tr>
        <tr>
            <td><code>git restore {filename}</code></td>
            <td>unstage file</td>
        </tr>
        <tr>
            <td><code>git reset</code></td>
            <td>unstage all files</td>
        </tr>
        <tr>
            <td><code>git commit -m "{message}"</code></td>
            <td>commit current staging area with message</td>
        </tr>
        <tr>
            <td><code>git commit --amend -m "{message}"</code></td>
            <td>rewrite most recent unpushed commit message</td>
        </tr>
        <tr>
            <td><code>git log</code></td>
            <td>View commit history</td>
        </tr>
        <tr>
            <td><code>git log --oneline</code></td>
            <td>View commit history (minimal)</td>
        </tr>
        <tr>
            <td><code>git log --graph --all --oneline</code></td>
            <td>draw tree graph of commit history</td>
        </tr>
        <tr>
            <td><code>git switch -c {branch}</code></td>
            <td>create and switch to branch</td>
        </tr>
        <tr>
            <td><code>git reset --hard {hash}</code></td>
            <td>reset HEAD to previous commit</td>
        </tr>
        <tr>
            <td><code>git push -f origin</code></td>
            <td>Force reset commit to remote repo (deletes any commit history in between)</td>
        </tr>
    </tbody>
</table>



### How to write a commit message and description (the proper way)
https://medium.com/@steveamaza/how-to-write-a-proper-git-commit-message-e028865e5791


### Staging deleted files
https://stackoverflow.com/questions/12373733/staging-deleted-files


### .gitignore
https://www.atlassian.com/git/tutorials/saving-changes/gitignore    