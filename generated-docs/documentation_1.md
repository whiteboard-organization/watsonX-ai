# Azure Resource Manager template for creating an SMTP Autoscale Setting

This template creates an SMTP Autoscale Setting resource in Azure Resource Manager. The autoscale setting is used to automatically scale the number of virtual machines in a virtual machine scale set based on the available memory of the VMs.

The autoscale setting has two rules: one for scale-up and one for scale-down. The scale-up rule increases the number of VMs when the available memory is less than 2 GB, and the scale-down rule decreases the number of VMs when the available memory is greater than 3 GB.

The metric trigger for both rules uses the metric "Available Memory Bytes" with a time grain of 1 minute, average statistic, and a time window of 5 minutes. The threshold for the scale-up rule is set to 573741824 (2 GB), and the threshold for the scale-down rule is set to 1047483648 (3 GB).

The virtual machine scale set is created using the azurerm\_resource\_group resource, and the target resource ID is set to the id of the virtual machine scale set. The location and resource group name are also passed in as parameters.

The autoscale setting is enabled and configured with a capacity profile that specifies the default, minimum, and maximum number of VMs.

## Properties

- `name`: The name of the autoscale setting.
- `location`: The location of the resource group.
- `resource_group_name`: The name of the resource group.
- `target_resource_id`: The ID of the virtual machine scale set.
- `enabled`: A boolean value indicating whether the autoscale setting is enabled or not.
- `profile`: The capacity profile for the autoscale setting.
  - `name`: The name of the capacity profile.
  - `capacity`: The capacity profile settings.
    - `default`: The default number of VMs.
    - `minimum`: The minimum number of VMs.
    - `maximum`: The maximum number of VMs.

## Rules

- `rule`: The rule for the autoscale setting.
  - `scale_action`: The action to take when the condition is met.
    - `direction`: The direction of the scale action (increase or decrease).
    - `type`: The type of the scale action (change count or metric).
    - `value`: The value for the scale action.
    - `cooldown`: The cooldown period for the scale action.
  - `metric_trigger`: The metric trigger for the rule.
    - `metric_name`: The name of the metric.
    - `metric_resource_id`: The ID of the resource for the metric.
    - `metric_namespace`: The namespace of the metric.
    - `time_grain`: The time grain for the metric.
    - `statistic`: The statistic for the metric.
    - `time_window`: The time window for the metric.
    - `time_aggregation`: The time aggregation for the metric.
    - `operator`: The operator for the metric.
    - `threshold`: The threshold for the metric.

## Example Usage

To use this template, replace the placeholders with the desired values. For example, to create an SMTP Autoscale Setting with the name "smtp\_autoscale" in the resource group "smtp" in the West US 2 region, you can use the following command:

```
azuredeploy.json
```

You can also specify the parameters in the JSON file itself. Here's an example:

```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "location": {
      "type": "string",
      "value": "westus2"
    },
    "resourceGroupName": {
      "type": "string",
      "value