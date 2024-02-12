---
title: Secrets
description: Learn to manage Secrets in your Pods.
sidebar_position: 4
---

You can add Secrets to your Pods and templates.
Secrets are encrypted strings of text that are used to store sensitive information, such as passwords, API keys, and other sensitive data.

## Create a Secret

You can create a Secret using the RunPod Web interface or the RunPod API.

1. Login into the RunPod Web interface and select [Secrets](https://www.runpod.io/console/user/secrets).
2. Choose **Create Secret** and provide the following:
   1. **Secret Name**: The name of the Secret.
   2. **Secret Value**: The value of the Secret.
   3. **Description**: (optional) A description of the Secret.
3. Select **Create Secret**.

:::note

Once a Secret is created, its value cannot be viewed.
If you need to change the Secret, you must create a new one or [modify the Secret Value](#modify-a-secret).

:::

## Modify a Secret

You can modify an existing Secret using the RunPod Web interface.

1. Login into the RunPod Web interface and select [Secrets](https://www.runpod.io/console/user/secrets).
2. Select the name of the Secret you want to modify.
3. Select the configuration icon and choose **Edit Secret Value**.
   1. Enter your new Secret Value.
4. Select **Save Changes**.

## View Secret details

You can view the details of an existing Secret using the RunPod Web interface.
You can't view the Secret Value.

1. Login into the RunPod Web interface and select [Secrets](https://www.runpod.io/console/user/secrets).
2. Select the name of the Secret you want to view.
3. Select the configuration icon and choose **View Secret**.

## Use a Secret in a Pod

With your Secrets setup, you can now reference them in your Pods.

You can reference your Secret directly or select it from the Web interface when creating or modifying a Pod template.

**Reference your Secret directly**

You can reference your Secret directly in the [Environment Variables](/pods/references/environment-variables) section of your Pod template.
To reference your Secret, reference it's key appended to the `RUNPOD_SECRET_` prefix.
For example:

```yml
{{ RUNPOD_SECRET_hello_world }}
```

Where `hello_world` is the value of your Secret Name.

**Select your Secret from the Web interface**

Alternatively, you can select your Secret from the Web interface when creating or modifying a Pod template.

## Delete a Secret

You can delete an existing Secret using the RunPod Web interface.

1. Login into the RunPod Web interface and select [Secrets](https://www.runpod.io/console/user/secrets).
2. Select the name of the Secret you want to delete.
3. Select the configuration icon and choose **Delete Secret**.
4. Enter the name of the Secret to confirm deletion.
5. Select **Confirm Delete**.
