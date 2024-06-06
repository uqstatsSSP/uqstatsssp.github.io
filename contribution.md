# Contribution Guidelines

Thank you for your interest in contributing to our UQ Stats SSP project! We welcome all contributions and appreciate your effort. Here are the guidelines for contributing to this project.

## How the project works

This project is setup using the jupyterbook framework. It takes in jupyter notebooks from the folder "./book/statistics" and "/book/Machine_Learning/" and render them as html files on the fly. New folders can be added based on the future requirements of the project.

A workflow file ".github/workflows/book.yml" is used to render the project. After each commit to the main branch, it runs the workflow and outputs rendered htmls in another branch named "gh-pages". Later, we serve the website from the "gh-pages" branch in the settings.

## Reporting Issues

If you find any bugs, inconsistencies or areas of improvement, please report them by creating a new issue in the GitHub repository. When creating an issue, please provide as much context as possible, including steps to reproduce the issue, the expected outcome, and the actual outcome.

## Proposing Enhancements

We welcome ideas for enhancements! If you have an idea for a new feature or an improvement to an existing feature, please create a new issue describing your proposal. Be sure to include as much detail as possible, including your rationale for the proposal and any potential implementation details.

## Code Contributions

If you'd like to contribute code to fix a bug, add a new feature, or otherwise improve the project, please follow these steps:

1. Fork the repository and clone it locally.

    ```git clone https://github.com/<your-username>/<repository-name.git>```

    ```cd repository-name```
2. Create a new branch for your changes.

    ```git checkout -b my-branch```
3. Make your changes in your branch.
4. Test your changes to ensure they work as expected and don't introduce new bugs.
5. Commit your changes and push your branch to your fork.

    ```git add .```

    ```git commit -m "Add your commit message here"```

    ```git push origin my-branch```
6. Create a pull request describing your changes.

## Jupyter Notebook Contributions

If you have a Jupyter notebook that you'd like to add to the JupyterBook project, please follow these steps:

1. Ensure your Jupyter notebook is in a finished state, with all code cells executed and output visible.
2. Fork the project repository to your own GitHub account and clone it to your local machine.

    ```git clone https://github.com/<your-username>/<repository-name.git>```

    ```cd repository-name```
3. Create a new branch for your changes.

    ```git checkout -b my-branch```
4. Add your Jupyter notebook to the appropriate directory ```/book/<your-appropiate-dir>```.

    **NOTE: YOU CAN ALSO UPLOAD AN MD FILE INSTEAD OF THE JUPYTER FILE!**
5. Update the `./book/_toc.yml` file to include your notebook. Put path to appropiate files under appropiate captions.
6. Commit your changes and push them to your fork on GitHub.

    ```git add .```

    ```git commit -m "Add your commit message here"```

    ```git push origin my-branch```
7. Create a pull request explaining what your notebook is about and why it should be included in the project.

## Documentation Contributions

Improvements to the documentation are just as important as code changes! If you'd like to improve the documentation, whether it's fixing a typo, adding a new section, or improving an existing section, please follow the same process as for code contributions.

## Code of Conduct

We expect all contributors to follow our Code of Conduct, which is designed to ensure a welcoming and respectful environment for everyone. Please take a moment to read it before participating.

Thank you for your contributions!