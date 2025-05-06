# Google Cloud Configuration Guide

## Prerequisites

1. Install the Google Cloud SDK
2. Have a Google Cloud account
3. Create a new project in Google Cloud Console

## Installation

1. Download and install the Google Cloud SDK:
   - [Windows](https://cloud.google.com/sdk/docs/install-sdk#windows)
   - [macOS](https://cloud.google.com/sdk/docs/install-sdk#mac)
   - [Linux](https://cloud.google.com/sdk/docs/install-sdk#linux)

## Authentication

Run the following commands to authenticate and set your project:

```bash
gcloud auth login
gcloud config set project gen-lang-client-0739218991
```

## Project Configuration

**Note:** Ensure that you have correctly set your project ID. If you encounter issues with accessing resources or enabling APIs, double-check that the project ID is correctly configured.

1. List your projects:
```bash
gcloud projects list
```

2. Set your default project:
```bash
gcloud config set project YOUR_PROJECT_ID
```

**Troubleshooting:** If the project is not set correctly, you may encounter errors when trying to enable APIs or access resources. Verify the project by running `gcloud config get-value project`. If it's incorrect, use the command in step 2 to set it to the correct project ID.

3. Set your default region and zone:
```bash
gcloud config set compute/region us-central1
gcloud config set compute/zone us-central1-a
```

## Verify Configuration

Check your current configuration:
```bash
gcloud config list
```

## Next Steps

1. Enable necessary APIs for your project
```bash
gcloud services enable workstations.googleapis.com
```
   (and ensure the `workstations.workstations.use`, `compute.disks.createSnapshot`, and `compute.snapshots.useReadOnly` permissions are granted)
2. Set up service accounts if needed

To create a service account, run the following command:

```bash
gcloud iam service-accounts create workstation-resources \
    --description="A descriptive name for your service account" \
    --display-name="My Cool Service Account"
```

3. Configure any specific services you plan to use (Compute Engine, Cloud Storage, etc.)
