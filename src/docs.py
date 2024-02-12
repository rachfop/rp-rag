import logging
import os

import requests

# Set up basic logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def download_file(file_url, file_path):
    """
    Download a file from a given URL to a specified local file path.
    """
    response = requests.get(file_url)
    if response.status_code == 200:
        with open(file_path, "wb") as file:
            file.write(response.content)
        logging.info(f"Downloaded {file_path}")
    else:
        logging.error(f"Failed to download file. Status code: {response.status_code}")


def process_github_folder(api_url, target_dir):
    """
    Recursively process and download .md files from a GitHub folder.
    """
    response = requests.get(api_url)
    if response.status_code == 200:
        items = response.json()
        for item in items:
            if item["type"] == "file" and item["name"].endswith(".md"):
                # Construct local file path
                file_path = os.path.join(target_dir, item["path"])
                # Make sure target directory exists
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                # Download the file
                download_file(item["download_url"], file_path)
            elif item["type"] == "dir":
                # Recursively process the directory
                new_target_dir = os.path.join(target_dir, item["path"])
                process_github_folder(item["url"], new_target_dir)
    else:
        logging.error(
            f"Failed to list folder contents. Status code: {response.status_code}"
        )


def download_github_folder(repo_url, branch, folder_path, target_dir):
    """
    Download all *.md files from a specific folder and its subfolders in a GitHub repo.

    Parameters:
    - repo_url: URL of the GitHub repository (e.g., 'https://github.com/user/repo')
    - branch: The branch from which to download (e.g., 'main' or 'master')
    - folder_path: Path to the folder within the repository (e.g., 'src/utils')
    - target_dir: Local directory to save the downloaded .md files
    """
    # Extract owner and repo name from URL
    parts = repo_url.split("/")
    owner, repo = parts[-2], parts[-1]

    # Adjust folder_path for API usage
    if folder_path.startswith("/"):
        folder_path = folder_path[1:]

    # GitHub API URL for contents of the folder
    api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{folder_path}?ref={branch}"

    # Process the folder
    process_github_folder(api_url, target_dir)


# Example usage
repo_url = "https://github.com/runpod/docs"
branch = "main"
folder_path = "docs/"
target_dir = "src/docs"
download_github_folder(repo_url, branch, folder_path, target_dir)
