# azure.tcl
# Simple Azure CLI wrapper in Tcl

# Check if Azure CLI is installed
proc check_azure_cli {} {
    if {[catch {exec az --version 2>&1} result]} {
        puts "Azure CLI not found. Please install Azure CLI first."
        exit 1
    }
}

# Login to Azure
proc azure_login {} {
    puts "Logging in to Azure..."
    if {[catch {exec az login 2>&1} result]} {
        puts "Azure login failed: $result"
        exit 1
    } else {
        puts "Azure login successful."
    }
}

# List Azure subscriptions
proc list_subscriptions {} {
    puts "Fetching Azure subscriptions..."
    if {[catch {exec az account list --output table 2>&1} result]} {
        puts "Failed to list subscriptions: $result"
    } else {
        puts $result
    }
}

# Main
check_azure_cli
azure_login
list_subscriptions