from prefect import flow, get_run_logger

@flow
def main(**kwargs):
    import subprocess
    logger = get_run_logger()
    out = subprocess.run(
        "id; nproc; free -m | sed -n 2p",
        shell=True, capture_output=True, text=True, timeout=120)
    logger.info("KFOUT_START " + out.stdout + " KFOUT_END " + out.stderr[:300])
