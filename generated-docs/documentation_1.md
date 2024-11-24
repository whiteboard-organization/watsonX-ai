
# A variable to store the prefix for the resource group, environment, and subnet names
variable "prefix" {
  type    = string
  default = "lz"
}

# A variable to store the location for the resource group and subnets
variable "location" {
  type    = string
  default = "westus2"
}

# A variable to store the address space for the virtual network
variable "address_space" {
  type    = list(string)
  default = ["10.0.0.0/16"]
}

# A variable to store the DNS servers for the virtual network
variable "dns_servers" {
  type    = list(string)
  default = ["10.0.1.1", "10.0.0.1"]
}

# A variable to store a list of subnet names
variable "subnet_names" {
  type    = list(string)
  default = ["subnet1", "subnet2"]
}<|endoftext|>