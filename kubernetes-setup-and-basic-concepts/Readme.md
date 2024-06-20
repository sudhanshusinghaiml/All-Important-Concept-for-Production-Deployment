# Local Kubernetes Setup Options
There are multiple options to create a local Kubernetes cluster on a Windows environment, such as: 
- **Minikube** - This is the most widely used feature-packed tool to implement local Kubernetes clusters on Windows, Linux, or Mac environments.
- **Docker Desktop** - Docker Desktop for Windows is the simplest solution that comes bundled with the ability to spin up a local Kubernetes cluster.
- **Kind** - This is a tool to create Kubernetes clusters using docker containers as nodes. The primary focus of this tool is to test Kubernetes, while it can also be used for other purposes such as application deployments, testing, etc.

However, I prefer Minikube over others as it is a standalone solution with a lot of features useful for managing a local Kubernetes cluster.


## How to Install Minikube - Prerequisite
- Minikube depends on a container or a virtual machine manager to deploy a Kubernetes cluster. The virtual machine managers it supports are Docker, Hyper kit, Hyper-V, KVM, Parallels, Podman, VirtualBox, and VMWare. Most Windows 10 Pro will use Hyper-V since it is built in, but since we are using Windows 10 Home, we will need to install a 
 third-party hypervisor. This walkthrough will use VirtualBox, but first, let’s install Minikube itself.

### Setup Kubernetes
Other common backends for distributed training include:
- **Install minikube** Run `winget install minikube` to install minikube and kubectl on your machine.

- **Install kubectl** Even with Minikube, we need the Kubernetes-CLI (kubectl) installed locally to connect and communicate with the Kubernetes cluster. Kubernetes offers two methods to install kubectl.
	- Download the kubectl binary and add it manually to the windows path
	- Use a package manager like Chocolatey or Scoop to install the kubectl and get it added to the path automatically. (Currently, Winget does not support installing kubectl)
	- Run `winget install -e --id Kubernetes.kubectl` to install kubectl on windows using winget package manager.
	- Run `kubectl version --client` to ensure the version you installed is up-to-date.
	- Navigate to your home directory: `cd ~`
	- Create the `.kube` directory: `mkdir .kube`
	- Navigate to the `.kube` directory you just created: `cd .kube`
	- `New-Item config -type file`: Configure kubectl to use a remote Kubernetes cluster
	
- You should download and install VirtualBox if you don’t have it installed already. Click the link on the download page for Windows hosts under platform packages and follow the installation instructions of the setup wizard.

### Create a Kubernetes Cluster using Minikube
- After the installation, we can use the start command to spin up a single-node Kubernetes cluster. This will create a Kubernetes cluster with the default values. Minikube automatically detects and selects a driver that is installed on your system.

- You can configure your preferred driver using the --driver flag or set the default driver using 
`minikube config set driver <driver>`

- You can check for the driver configuration options  **[driver configuration options](https://minikube.sigs.k8s.io/docs/drivers/ "minikube documentation")**

- Run `minikube start` to start single node Kubernetes cluster.

### Starting Minikube with Custom Options
- We need to specify custom options to match the Kubernetes cluster with the local Windows environment. The most commonly specified options are resource usage and network connectivity.

	- `minikube start --driver=virtualbox --cpus=2 --memory=2000m --disk-size="20000mb"`
	
- We explicitly provide the following options in the above startup string when creating the Kubernetes cluster.

	- `--driver=virtualbox` - Enforce VirtualBox as the driver
	- `--cpus=2` - Limit the CPU count
	- `--memory=2000m` - Limit the memory to 2GB
	- `--disk-size=”20000mb”` - Define a disk size of 30GB
	
- This will create a single-node Kubernetes cluster with user-configured options. In addition, we can customize the Kubernetes cluster further using the **[startup] (https://minikube.sigs.k8s.io/docs/commands/start/ "minikube documentation")** options offered by minikube.

- If we look at the Virtual Box manager, we can see that a single minikube instance has been created.


### Verify the Kubernetes Cluster configuration

- We can simply run the kubectl to get the system pods of the Kubernetes cluster and thereby identify a successful configuration.

- `kubectl get pods -n kube-system`


### Create a Multi-Node Kubernetes Cluster

- We can use the --nodes option to create a multi-node cluster if we need to simulate a multi-node Kubernetes installation. There, the only consideration is the availability of resources in the local machine.

- `minikube start --cpus=2 --memory=2000m --disk-size=20000mb --nodes=3`

- We can see that three separate minikube nodes are created in the VirtualBox manager.

- With kubectl we can see the three nodes are present in the cluster: `kubectl get nodes`


### Mounting Folders to Kubernetes Cluster
- Since we are using a hypervisor (Hyper-V), the Kubernetes nodes do not have access to the host machine. Therefore, Minikube provides users with the mount option to map a host directory to the Kubernetes cluster.

- We are mounting the `C:/data` directory to the Kubernetes cluster as `/data/user_data/`

- `minikube mount C:/data:/data/user_data`

- The above command will prompt users with a message from the Windows Firewall to allow access to Minikube through the firewall. Here, you have to allow access, or otherwise, the mount will fail. (Grant permissions according to the network configuration)

- In the end, Minikube will notify a successful mount. However, this mount is not permanent, and the user needs to keep the PowerShell window open (process running) to maintain the mount.

- Identify the firewall rules created by running the following command through Powershell.
	`Get-NetFirewallRule | Where-Object { $_.Name -match "minikube" }`
	
- To verify the mount, run `minikube ssh` command on a PowerShell window. It will establish an ssh connection to minikube. Next, view the directory listing with the ls command.

	- `minikube ssh`
	- `ls -al /data/user_data/`