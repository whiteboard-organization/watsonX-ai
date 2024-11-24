
# Terraform Configuration for Azure Resource Manager

This Terraform configuration creates and manages a Linux virtual machine scale set with auto-scaling capabilities in an Azure resource group.

## Variables

```hcl
variable "resource_group_name" {
  type    = string
  default = "my-resource-group"
}

variable "location" {
  type    = string
  default = "westus2"
}

variable "name" {
  type    = string
  default = "my-vmss"
}

variable "instances" {
  type    = number
  default = 1
}

variable "source_image_id" {
  type    = string
  default = "ubuntu-latest"
}

variable "boot_diagnostics_uri" {
  type    = string
  default = ""
}

variable "admin_username" {
  type    = string
  default = "ubuntu"
}

variable "admin_ssh_public_key" {
  type    = string
  default = ""
}

variable "additional_ssh_keys" {
  type    = list(string)
  default = []
}

variable "subnet_id" {
  type    = string
  default = ""
}

variable "vm_size" {
  type    = string
  default = "Standard_B1ls"
}

variable "identity_id" {
  type    = string
  default = ""
}

variable "storage_account_type" {
  type    = string
  default = "Standard_LRS"
}

variable "autoscale" {
  type    = list(object)
  default = []
}

```

## Resources

```hcl
resource "azurerm_resource_group" "example" {
  name     = var.resource_group_name
  location = var.location
}

resource "azurerm_linux_virtual_machine_scale_set" "vmss" {
  name                = var.name
  resource_group_name = azurerm_resource_group.example.id
  location            = var.location
  tags                = var.tags

  sku                          = var.vm_size
  instances                    = var.instances
  proximity_placement_group_id = var.proximity_placement_group_id

  lifecycle {
    ignore_changes = [
      instances,
    ]
  }

  admin_username = var.admin_username

  admin_ssh_key {
    username   = var.admin_username
    public_key = var.admin_ssh_public_key
  }

  source_image_id = var.source_image_id

  os_disk {
    storage_account_type = var.storage_account_type
    caching              = "ReadWrite"
  }

  network_interface {
    name                          = "primary-nic"
    primary                       = true
    enable_accelerated_networking = false
    network_security_group_id     = null

    ip_configuration {
      name      = "internal"
      primary   = true
      subnet_id = azurerm_subnet.subnet.id
      public_ip_address_allocation = "Static"
    }
  }

  upgrade_mode = "Manual"

  boot_diagnostics {
    enabled = var.boot_diagnostics_uri != null
    storage_account_uri = var.boot_diagnostics_uri
  }

  dynamic "boot_diagnostics" {
    for_each = toset(var.boot_diagnostics.length > 0 ? [1] : [])

    content {
      storage_account_uri = var.boot_diagnostics.value
    }
  }

  dynamic "identity