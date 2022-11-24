# Docker CLI commands - epic cheat sheet

- **docker info** - display system info
- **docker version** - display system's version
- **docker login** - login to Docker registry

---

## Running and Stopping

- **docker pull [imagename]** - pull image from registry
- **docker run [imagename]** - run containers
- **docker run -d [imagename]** - detached mode
- **docker start [containername]** - start stopped containers
- **docker ps** - list running containers
- **docker ps -a** - list all (running and stopped) containers
- **docker stop [containername]** - stop container
- **docker kill [containername]** - kill container
- **docker image inspect [imagename]** - get image info


*Difference between image name and container name?*

*Image name is the name of the image in the container registry. While container name is the name of the running instance of the docker image.*

---

## Set limits

- **docker run --memory="256m" nginx** - set memory for a container
- **docker run --cpus=".5" nginx** - set cpu for a container

---

## Attach shell

- **docker run -it nginx -- /bin/bash** - Attach shell
- **docker run -it nginx -- microsoft/powershell:nanoserver pwsh.exe** - Attach powershell
- **docker container exec -it [containername] bash** - Attach to a running container

---

## Cleaning up

- **docker rm [containername]** - remove stopped containers
- **docker rm $(docker ps -a -q)** - remove all stopped containers
- **docker images** - lists images
- **docker rmi [imagename]** - delete image
- **docker system prune -a** - remove all images not in use by any container, USE CAREFULLY

---

## Building

- **docker build -t [name:tag] .** - Build an image using a Dockerfile located in './' (same folder)
- **docker build -t [name:tag] -f [fileName]** - Build an image using a Dockerfile located in different folder
- **docker tag [imagename] [name:tag]** - Tag an existing image

---

## Volume

- **docker create volume [volumeName]** - Creates a new volume
- **docker volume ls** - Lists the volumes
- **docker volume inspect [volumeName]** - Display the volume info
- **docker volume rm [volumeName]** - Deletes a volume
- **docker volume prune** - Delets all volumes not mounted

---

## Docker compose

- **docker compose build** - Build the images specified in YAML file
- **docker compose start** - Start the containers
- **docker compose stop** - Stop the containers
- **docker compose up -d** - Build and start
- **docker compose ps** - List what's running
- **docker compose rm** - Remove from memory
- **docker compose down** - Stop and remove
- **docker compose logs** - Get the logs
- **docker compose exec [container] bash** - Run a command in a container
- **docker compose -p [projectName] up -d** - Build and run an instance as a project (Allows us to run 2 instances of the same project)
- **docker compose ls** - List running projects
- **docker compose cp [containerID]:[SRC_PATH] [DEST_PATH]** - Copy files from the container
- **docker compose cp [SRC_PATH] [containerID]:[DEST_PATH]** - Copy files to the container

---

# Kubernetes CLI commands - epic cheat sheet

## K8s Context

- **kubectl config current-context** - Get the current context
- **kubectl config get-contexts** - List all context
- **kubectl config use-context [contextName]** - Set the current context
- **kubectl config delete-context [contextName]** - Delete a context from the config file

---

## K8s Namespace

- **kubectl get namespace** - List all namespaces
- **kubectl get ns** - List all namespaces (shortcut)
- **kubectl config set-context --current --namespace=[namespaceName]** - Set the current context to use a namespace
- **kubectl create ns [namespaceName]** - Create a namespace
- **kubectl delete ns [namespaceName]** - Delete a namespace
- **kubectl get pods --all-namespace** - List all pods in all namespaces

## K8s Pods

- **kubectl create -f [pod-definition.yml]** - Create a pod
- **kubectl run [podname] --image=busybox -- /bin/sh -c "sleep 3600"** - Run a pod
- **kubectl get pods** - List the running pods
- **kubectl get pods -o wide** - List the running pods with detailed info
- **kubectl describe pod [podname]** - Show pod info
- **kubectl get pod [podname] -o yaml > file.yaml** - Extract the pod defintion in YAML and save it to a file
- **kubectl exec -it [podname] -- sh** - Interactive mode
- **kubectl delete -f [pod-definition.yml]** - Delete a pod
- **kubectl delete pod [podname]** - Delete a pod using pod name

In case of multi-container pods

- **kubectl exec -it [podname] -c [containername] -- sh** - Exec into a container of a pod
- **kubectl logs [podname] -c [containername]** -- Get the logs for a container





