import docker
import subprocess

src_path = "/app/jobs.docx"
dest_path = "."

def cp_file():
    def get_container_id():
        client = docker.from_env()
        containers = client.containers.list()

        try:
            for container in containers:
                containerID = container.id
            cut_containerID = containerID[:12].ljust(12)
            print(f"shortened Container ID: {cut_containerID}")
            return(cut_containerID)
        except:
            print("No containers running currently")


    cutId = get_container_id()

    def docker_cp(container_id, src_path, dest_path):
        command = f"docker cp {container_id}:{src_path} {dest_path}"
        subprocess.run(command, shell=True)

    docker_cp(cutId, src_path, dest_path)

if __name__ == '__main__':
    cp_file()