## To install Homebrew (a package manager for macOS), follow these steps:
- Open Terminal
- Install Homebrew
Run the following command in your Terminal to install Homebrew:
```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
  - add this following line to ~/.zshrc  - For Zsh (default shell in recent macOS versions):
```sh
    eval "$(/opt/homebrew/bin/brew shellenv)"
```
  - For Bash:
```sh
    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.bash_profile
    source ~/.bash_profile
```
- Verify Homebrew Installation
  ```sh
    brew --version
  ```
- Update
  ```sh
    brew update
  ```
- Install bash
  ```sh
    brew install bash
  ```
- check current shell
  ```sh
    echo $SHELL
  ```
- Optional: Change the Shell for a Specific User
  ```bash
  sudo chsh -s /bin/bash username
  ```
- Change your default shell to the new Bash:
  ```bash
  chsh -s /opt/homebrew/bin/bash
  ```
- Install Docker
  ```bash
  brew install --cask docker
  ```
  
