# 2. Clone a Robot Repository and Make a Branch
All of our robot code lives on GitHub in the **Team-4536** organization. In this tutorial you will copy ("clone") a robot code repository onto your laptop, then make your own branch to work in.

## Goal
By the end you will have a team repository open in VS Code on your own published branch, and you will know how to save ("commit") your work and send it ("push") to GitHub.

## Prerequisites
* [1. Laptop Setup](../01_LaptopSetup/laptopSetup.md)
* A GitHub account that has been added to the Team-4536 organization (ask a mentor)
* Read [using GitHub tutorial](../../using%20GitHub%20tutorial.md) for what GitHub, repositories and issues are

> If you already cloned **mb-tutorials** with the [main README](../../README.md), you already know most of this. The steps are the same for any robot repository.

***
## Vocabulary
* **Repository ("repo")**: a project folder that Git keeps a history of. For example, `mb-tutorials` or this year's robot code repo.
* **Clone**: download a copy of a repo onto your laptop.
* **Branch**: your own copy of the code inside the repo. Changes on your branch don't affect anybody else until they are merged.
* **Commit**: a saved snapshot of your changes, with a message that describes them.
* **Push / Publish**: send your commits up to GitHub, so they are safe and other people can see them.
* **Pull**: get other people's new commits from GitHub.

***
## Step 1. Clone the repository
1. On GitHub, go to the repository you want (ask which one; this season's robot repo is in [github.com/Team-4536](https://github.com/Team-4536)).
1. Click the green **<> Code** button and copy the **HTTPS** link.
1. In VS Code, open a new window (**File --> New Window**) and click **Clone Git Repository...**
1. Paste the link and press enter.
1. Choose `C:\repos` as the place to save it. (Make the `repos` folder if it doesn't exist. No spaces, no punctuation.)
1. When VS Code asks **"Would you like to open the cloned repository?"**, click **Open**.

> **Important:** keep repos in `C:\repos`, **not** in OneDrive, Desktop or Documents. OneDrive syncing can lock files and break Git and the robot tools.

***
## Step 2. Make your own branch
1. Click the **Source Control** icon on the left side bar (it looks like a tree with three dots).
1. Click the **...** (three dots) at the top, then **Branch --> Create Branch...**
1. Type a name like `yourName-practice` and press enter.
1. Click **Publish Branch**.

Look at the bottom left corner of VS Code. It shows which branch you are on. **Always check it before you start working.**

***
## Step 3. Save your work (commit and push)
Do this every time you finish a chunk of work, and **always** before you leave for the day.

1. Click the **Source Control** icon. Your changed files are listed under **Changes**.
1. Type a short message in the box that says what you did. For example: `Added teleop timer`.
1. Click **Commit**. If VS Code asks "stage all your changes?", click **Yes**.
1. Click **Sync Changes** (or **Publish Branch** if you haven't published yet).

> If you don't push your commits, your work is only on that one laptop. When you switch laptops (or someone else uses yours), it is gone!

***
## Step 4. Get the newest code (pull)
When you sit down to work, click **Sync Changes** in Source Control (or the circular arrows next to the branch name at the bottom left). This gets new commits from GitHub for your branch.

***
## Challenge
1. Clone **mb-tutorials** (if you haven't already) and make a branch named `yourName-robot`.
1. Make a new file in your branch called `yourName.txt` and write one sentence about what you want to program on the robot.
1. Commit it with a good message and push it.
1. Show a mentor or captain your commit on GitHub (in the repo, click the branch dropdown, choose your branch, then click **Commits**).

**Next:** [3. Your First Robot Project](../03_FirstRobotProject/firstRobotProject.md)
